"""Guided PostgreSQL examples: configuration, CRUD, parameters and rollback."""

import argparse
import os
from pathlib import Path
from uuid import uuid4

try:
    import psycopg
except ImportError:
    raise SystemExit(
        "Install the driver first: .\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt"
    ) from None


def connect():
    """Read this exercise's settings; never print the password."""
    password = os.environ.get("WEEK4_DB_PASSWORD")
    if not password:
        raise ValueError("Set WEEK4_DB_PASSWORD in this terminal; see README.md.")
    port = int(os.environ.get("WEEK4_DB_PORT", "5432"))
    if not 1 <= port <= 5432:
        raise ValueError("WEEK4_DB_PORT must be between 1 and 5432.")
    return psycopg.connect(
        host="127.0.0.1",
        port=port,
        dbname="week04_bridge",
        user="week04",
        password=password,
        connect_timeout=5,
        autocommit=True,
    )


def init_products(conn) -> None:
    schema = Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
    with conn.transaction():
        conn.execute(schema)
        for product in [
            ("Notebook", 80, 10),
            ("Keyboard", 1200, 5),
            ("O'Reilly SQL Guide", 650, 3),
        ]:
            conn.execute(
                """INSERT INTO week04_products (name, price_twd, stock)
                   VALUES (%s, %s, %s) ON CONFLICT (name) DO NOTHING""",
                product,
            )
    print("Product table ready. Existing rows were kept.")


def create_product(conn, name: str, price_twd: int, stock: int):
    return conn.execute(
        """INSERT INTO week04_products (name, price_twd, stock)
           VALUES (%s, %s, %s) RETURNING id, name, price_twd, stock""",
        (name, price_twd, stock),
    ).fetchone()


def find_product(conn, name: str):
    # The one-element tuple needs its comma. %s is not Python string formatting.
    return conn.execute(
        "SELECT id, name, price_twd, stock FROM week04_products WHERE name = %s",
        (name,),
    ).fetchone()


def list_products(conn, min_price: int):
    return conn.execute(
        """SELECT id, name, price_twd, stock FROM week04_products
           WHERE price_twd >= %s ORDER BY price_twd, id""",
        (min_price,),
    ).fetchall()


def update_stock(conn, product_id: int, stock: int):
    return conn.execute(
        """UPDATE week04_products SET stock = %s WHERE id = %s
           RETURNING id, name, price_twd, stock""",
        (stock, product_id),
    ).fetchone()


def delete_product(conn, product_id: int) -> bool:
    cursor = conn.execute("DELETE FROM week04_products WHERE id = %s", (product_id,))
    return cursor.rowcount == 1


def crud_demo(conn) -> None:
    name = "O'Reilly demo " + uuid4().hex[:12]
    # autocommit=True outside; this block explicitly groups the four operations.
    with conn.transaction():
        created = create_product(conn, name, 120, 5)
        print("CREATE:", created)
        found = find_product(conn, name)
        assert found == created
        print("READ:", found)
        updated = update_stock(conn, created[0], 8)
        assert updated == (created[0], name, 120, 8)
        print("UPDATE:", updated)
        # The text is a value, so it cannot turn into a WHERE condition.
        assert find_product(conn, "' OR '1'='1") is None
        assert delete_product(conn, created[0])
        assert find_product(conn, name) is None
        print("DELETE: the newly created demo product is gone.")
    print("CRUD checks passed; only the demo's own row was deleted.")


def rollback_demo(conn) -> None:
    name = "rollback-demo-" + uuid4().hex[:12]
    try:
        with conn.transaction():
            created = create_product(conn, name, 100, 5)
            # CHECK (stock >= 0) fails after the INSERT has succeeded.
            update_stock(conn, created[0], -1)
    except psycopg.errors.CheckViolation:
        print("Expected CHECK violation: stock cannot be negative.")
    else:
        raise AssertionError("The negative stock should have failed.")

    assert find_product(conn, name) is None
    assert conn.execute("SELECT 1").fetchone() == (1,)
    print("Rollback passed: the INSERT was also undone; connection still works.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "section", choices=["check", "init", "list", "crud", "rollback"]
    )
    parser.add_argument("--min-price", type=int, default=100)
    args = parser.parse_args()
    if args.min_price < 0:
        parser.error("--min-price must be non-negative")

    try:
        with connect() as conn:
            if args.section == "check":
                print(
                    "Database / user:",
                    conn.execute("SELECT current_database(), current_user").fetchone(),
                )
                print("PostgreSQL:", conn.execute("SHOW server_version").fetchone()[0])
            elif args.section == "init":
                init_products(conn)
            elif args.section == "list":
                for row in list_products(conn, args.min_price):
                    print(row)
            elif args.section == "crud":
                crud_demo(conn)
            elif args.section == "rollback":
                rollback_demo(conn)
    except ValueError as error:
        parser.exit(1, f"Configuration error: {error}\n")
    except psycopg.OperationalError:
        parser.exit(
            1,
            "Cannot connect. Check Docker Desktop, compose status, port and password; see README.md.\n",
        )
    except psycopg.errors.UndefinedTable:
        parser.exit(1, "Run db_bridge.py init first.\n")


if __name__ == "__main__":
    main()

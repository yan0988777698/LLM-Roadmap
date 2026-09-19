"""Complete four parameterized SQL statements. Keep the checks below."""

import argparse

from db_bridge import connect, psycopg


def create_product(conn, name: str, price_twd: int, stock: int):
    # TODO 1: INSERT the three values, then RETURNING id.
    # Pass values separately in a tuple. Do not use f-strings or concatenate SQL.
    query = (
        "Insert into week04_products (name, price_twd, stock) "
        "values (%s, %s, %s) RETURNING id"
    )
    parameters = (name, price_twd, stock)
    if query is None or parameters is None:
        raise NotImplementedError("TODO 1: fill INSERT query and parameters.")
    return conn.execute(query, parameters).fetchone()[0]


def find_product(conn, name: str):
    # TODO 2: SELECT id, name, price_twd, stock by an exact name match.
    # A missing name should return None. A one-element tuple needs a comma.
    query = "Select id, name, price_twd, stock from week04_products where name = %s"
    parameters = (name,)
    if query is None or parameters is None:
        raise NotImplementedError("TODO 2: fill SELECT query and parameters.")
    return conn.execute(query, parameters).fetchone()


def update_stock(conn, product_id: int, stock: int) -> int:
    # TODO 3: UPDATE stock for just this id. rowcount is the affected row count.
    query = "Update week04_products set stock = %s where id = %s"
    parameters = (stock, product_id)
    if query is None or parameters is None:
        raise NotImplementedError("TODO 3: fill UPDATE query and parameters.")
    return conn.execute(query, parameters).rowcount


def delete_product(conn, product_id: int) -> int:
    # TODO 4: DELETE just this id, keeping all other products.
    query = "Delete from week04_products where id = %s"
    parameters = (product_id,)
    if query is None or parameters is None:
        raise NotImplementedError("TODO 4: fill DELETE query and parameters.")
    return conn.execute(query, parameters).rowcount


def check_answers(conn) -> None:
    # This connection's temporary table hides the permanent table of the same name.
    # Nothing in this practice changes the guided example's products.
    with conn.transaction(force_rollback=True):
        conn.execute("""CREATE TEMP TABLE week04_products
               (LIKE public.week04_products INCLUDING ALL) ON COMMIT DROP""")
        other = conn.execute(
            """INSERT INTO week04_products (name, price_twd, stock)
               VALUES (%s, %s, %s) RETURNING id, name, price_twd, stock""",
            ("Keep this product", 50, 9),
        ).fetchone()

        name = "O'Reilly SQL Workbook"
        product_id = create_product(conn, name, 200, 3)
        expected = (product_id, name, 200, 3)
        # Independent reads check that the answers actually change PostgreSQL.
        actual = conn.execute(
            "SELECT id, name, price_twd, stock FROM week04_products WHERE id = %s",
            (product_id,),
        ).fetchone()
        assert actual == expected, "INSERT must store the supplied values."
        assert find_product(conn, name) == expected
        assert find_product(conn, "missing product") is None
        assert find_product(conn, "' OR '1'='1") is None, "Use parameterized SQL."

        assert update_stock(conn, product_id, 7) == 1
        assert conn.execute(
            "SELECT stock FROM week04_products WHERE id = %s", (product_id,)
        ).fetchone() == (7,)

        # A nested transaction uses a savepoint; the invalid change is rolled back.
        try:
            with conn.transaction():
                update_stock(conn, product_id, -1)
        except psycopg.errors.CheckViolation:
            pass
        else:
            raise AssertionError("Negative stock must fail the database constraint.")
        assert find_product(conn, name) == (product_id, name, 200, 7)

        assert delete_product(conn, product_id) == 1
        assert find_product(conn, name) is None
        assert delete_product(conn, product_id) == 0
        assert conn.execute(
            "SELECT id, name, price_twd, stock FROM week04_products ORDER BY id"
        ).fetchall() == [other], "UPDATE / DELETE must preserve other products."

    print("All practice checks passed. Record your explanations and actual study time.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run all four CRUD checks. No positional arguments are accepted."
    )
    parser.parse_args()
    try:
        with connect() as conn:
            check_answers(conn)
    except NotImplementedError as error:
        print(error)
        raise SystemExit(1) from None
    except ValueError as error:
        raise SystemExit(f"Configuration error: {error}") from None
    except psycopg.OperationalError:
        raise SystemExit(
            "Cannot connect. Follow the database setup in README.md."
        ) from None
    except psycopg.errors.UndefinedTable:
        raise SystemExit("Run db_bridge.py init first.") from None


if __name__ == "__main__":
    main()

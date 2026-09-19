"""Run without extra packages; practise CLI arguments and environment variables."""

import argparse
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--min-price", type=int, default=100, help="Minimum price in whole TWD."
    )
    args = parser.parse_args()
    if args.min_price < 0:
        parser.error("--min-price must be non-negative")

    print("Working directory:", Path.cwd())
    print("Script directory:", Path(__file__).resolve().parent)
    print("WEEK4_MODE:", os.environ.get("WEEK4_MODE", "development"))
    print("Minimum price:", args.min_price)
    print("DB password configured:", bool(os.environ.get("WEEK4_DB_PASSWORD")))


if __name__ == "__main__":
    main()

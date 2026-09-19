"""Connection configuration and CLI regression checks; no database required."""

import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import db_bridge


class ConfigurationTests(unittest.TestCase):
    def test_valid_ports_reach_driver(self):
        for port in (1, 5432, 15432, 65535):
            with self.subTest(port=port), patch.dict(
                os.environ,
                {"WEEK4_DB_PASSWORD": "test-only", "WEEK4_DB_PORT": str(port)},
                clear=True,
            ), patch.object(db_bridge.psycopg, "connect") as driver:
                db_bridge.connect()
                self.assertEqual(driver.call_args.kwargs["port"], port)
                self.assertEqual(driver.call_args.kwargs["host"], "127.0.0.1")

    def test_invalid_ports_do_not_reach_driver(self):
        for port in ("0", "-1", "65536", "not-a-port"):
            with self.subTest(port=port), patch.dict(
                os.environ,
                {"WEEK4_DB_PASSWORD": "test-only", "WEEK4_DB_PORT": port},
                clear=True,
            ), patch.object(db_bridge.psycopg, "connect") as driver:
                with self.assertRaises(ValueError):
                    db_bridge.connect()
                driver.assert_not_called()

    def test_missing_password_does_not_reach_driver(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(
            db_bridge.psycopg, "connect"
        ) as driver:
            with self.assertRaisesRegex(ValueError, "WEEK4_DB_PASSWORD"):
                db_bridge.connect()
            driver.assert_not_called()

    def test_practice_rejects_unsupported_arguments_before_connecting(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("practice.py")), "create_product"],
            capture_output=True,
            text=True,
            env={key: value for key, value in os.environ.items() if key != "WEEK4_DB_PASSWORD"},
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("unrecognized arguments", result.stderr)


if __name__ == "__main__":
    unittest.main()

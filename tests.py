import unittest
import io
from unittest.mock import patch, Mock
import requests
from get_currency import get_currencies
from logger import logger


class TestGetCurrencies(unittest.TestCase):

    @patch("get_currency.requests.get")
    def test_ok_response(self, mock_get):
        mock_resp = Mock()
        mock_resp.json.return_value = {
            "Valute": {
                "USD": {"Value": 93.25},
                "EUR": {"Value": 101.7}
            }
        }
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        res = get_currencies(["USD", "EUR"])
        self.assertEqual(res, {"USD": 93.25, "EUR": 101.7})

    @patch("get_currency.requests.get")
    def test_network_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Connection failed")
        with self.assertRaises(ConnectionError):
            get_currencies(["USD"])

    @patch("get_currency.requests.get")
    def test_bad_json(self, mock_get):
        mock_resp = Mock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.side_effect = ValueError("Bad JSON format")
        mock_get.return_value = mock_resp
        with self.assertRaises(ValueError):
            get_currencies(["USD"])

    @patch("get_currency.requests.get")
    def test_no_valute_section(self, mock_get):
        mock_resp = Mock()
        mock_resp.json.return_value = {"Data": "something"}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp
        with self.assertRaises(KeyError):
            get_currencies(["USD"])

    @patch("get_currency.requests.get")
    def test_currency_missing(self, mock_get):
        mock_resp = Mock()
        mock_resp.json.return_value = {"Valute": {"EUR": {"Value": 100}}}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp
        with self.assertRaises(KeyError):
            get_currencies(["USD"])

    @patch("get_currency.requests.get")
    def test_wrong_value_type(self, mock_get):
        mock_resp = Mock()
        mock_resp.json.return_value = {"Valute": {"USD": {"Value": "unknown"}}}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp
        with self.assertRaises(TypeError):
            get_currencies(["USD"])


class TestLoggerDecorator(unittest.TestCase):

    def test_success_case(self):
        buf = io.StringIO()

        @logger(handle=buf)
        def calc(a, b):
            return a + b

        res = calc(5, 7)
        self.assertEqual(res, 12)

        output = buf.getvalue()
        self.assertIn("START calc", output)
        self.assertIn("SUCCESS calc", output)

    def test_error_case(self):
        buf = io.StringIO()

        @logger(handle=buf)
        def do_error():
            raise RuntimeError("Test fail")

        with self.assertRaises(RuntimeError):
            do_error()

        output = buf.getvalue()
        self.assertIn("ERROR", output)
        self.assertIn("RuntimeError", output)


class TestStreamWrite(unittest.TestCase):

    def setUp(self):
        self.buf = io.StringIO()

        @logger(handle=self.buf)
        def wrapped_call():
            return get_currencies(['USD'], url="https://invalid-url")

        self.wrapped_call = wrapped_call

    @patch("get_currency.requests.get")
    def test_error_logging(self, mock_get):
        mock_get.side_effect = requests.RequestException("Bad URL")
        with self.assertRaises(ConnectionError):
            self.wrapped_call()

        logs = self.buf.getvalue()
        self.assertIn("ERROR", logs)
        self.assertIn("ConnectionError", logs)


if __name__ == '__main__':
    unittest.main()
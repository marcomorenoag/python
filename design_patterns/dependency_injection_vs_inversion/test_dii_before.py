import unittest
from unittest.mock import patch
from dii_before import AuthorizerSMS, Order, PaymentProcessor


class TestOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.order = Order()

    def test_init(self):
        self.assertEqual(self.order.status, "open")

    def test_set_status(self):
        self.order.set_status("paid")
        self.assertEqual(self.order.status, "paid")


class TestAuthorizerSMS(unittest.TestCase):
    def setUp(self) -> None:
        self.auth = AuthorizerSMS()

    def test_init_authorized(self):
        self.assertFalse(self.auth.is_authorized())

    def test_code_decimal(self):
        self.auth.generate_sms_code()
        self.assertTrue(self.auth.code.isdecimal())

    def test_authorize_success(self):
        self.auth.generate_sms_code()
        with patch('builtins.input', return_value=self.auth.code):
            self.auth.authorize()
            self.assertTrue(self.auth.is_authorized())

    @patch('builtins.input', return_value="1234567")
    def test_authorize_fail(self, mocked_input):
        self.auth.generate_sms_code()
        self.auth.authorize()
        self.assertFalse(self.auth.is_authorized())


class TestPaymentProcessor(unittest.TestCase):
    def test_payment_success(self):
        # ???
        self.assertTrue(True)

    def test_payment_fail(self):
        # ???
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

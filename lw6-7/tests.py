import unittest
from payment_system import PaymentSystem


class TestPaymentSystem(unittest.TestCase):
    def setUp(self):
        self.payment_system = PaymentSystem(initial_balance=100)

    def test_check_balance(self):
        self.assertEqual(self.payment_system.check_balance(), 100)

    def test_make_payment_sufficient_funds(self):
        result = self.payment_system.make_payment(50)
        self.assertTrue(result)
        self.assertEqual(self.payment_system.balance, 47.5)
        self.assertEqual(self.payment_system.get_status(), "Success")

    def test_make_payment_all_funds(self):
        # Точная оплата всех средств с учётом комиссии 5%
        amount = 100 / 1.05
        result = self.payment_system.make_payment(amount)
        self.assertTrue(result)
        self.assertAlmostEqual(self.payment_system.balance, 0.0, places=5)
        self.assertEqual(self.payment_system.get_status(), "Success")

    def test_make_payment_insufficient_funds(self):
        result = self.payment_system.make_payment(150)
        self.assertFalse(result)
        self.assertEqual(self.payment_system.balance, 100)
        self.assertEqual(self.payment_system.get_status(), "Insufficient funds")

    def test_add_funds(self):
        self.payment_system.add_funds(50)
        self.assertEqual(self.payment_system.balance, 150)

    def test_set_commission_rate_positive(self):
        self.payment_system.set_commission_rate(0.1)
        self.assertEqual(self.payment_system.commission_rate, 0.1)
        self.assertIsNone(self.payment_system.get_status())

    def test_set_commission_rate_zero(self):
        self.payment_system.set_commission_rate(0)
        self.assertEqual(self.payment_system.commission_rate, 0)
        self.assertIsNone(self.payment_system.get_status())

    def test_set_commission_rate_negative(self):
        self.payment_system.set_commission_rate(-0.1)
        self.assertEqual(self.payment_system.commission_rate, 0)
        self.assertEqual(self.payment_system.get_status(), "Negative commission")

    def test_get_status_initial(self):
        self.assertIsNone(self.payment_system.get_status())

    def test_make_payment_invalid_type(self):
        invalid_amounts = ["50", {"amount": 50}, [50]]
        for invalid_amount in invalid_amounts:
            with self.subTest(invalid_amount=invalid_amount):
                with self.assertRaises(TypeError):
                    self.payment_system.make_payment(invalid_amount)

    def test_make_payment_negative_amount(self):
        with self.assertRaises(ValueError):
            self.payment_system.make_payment(-10)

    def test_add_funds_invalid_type(self):
        invalid_amounts = ["50", {"amount": 50}, [50]]
        for invalid_amount in invalid_amounts:
            with self.subTest(invalid_amount=invalid_amount):
                with self.assertRaises(TypeError):
                    self.payment_system.add_funds(invalid_amount)

    def test_add_funds_negative_amount(self):
        with self.assertRaises(ValueError):
            self.payment_system.add_funds(-10)

    def test_set_commission_rate_invalid_type(self):
        invalid_rates = ["0.1", {"rate": 0.1}, [0.1]]
        for invalid_rate in invalid_rates:
            with self.subTest(invalid_rate=invalid_rate):
                with self.assertRaises(TypeError):
                    self.payment_system.set_commission_rate(invalid_rate)

    def test_initial_balance_invalid_type(self):
        with self.assertRaises(TypeError):
            PaymentSystem("100")

    def test_initial_balance_negative(self):
        with self.assertRaises(ValueError):
            PaymentSystem(-100)


if __name__ == '__main__':
    unittest.main()
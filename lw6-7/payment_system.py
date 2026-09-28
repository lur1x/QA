class PaymentSystem:
    def __init__(self, initial_balance):
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = initial_balance
        self.commission_rate = 0.05
        self.status = None

    def check_balance(self):
        return self.balance

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        total_amount = amount * (1 + self.commission_rate)
        if self.balance >= total_amount:
            self.balance -= total_amount
            self.status = "Success"
            return True
        else:
            self.status = "Insufficient funds"
            return False

    def add_funds(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def set_commission_rate(self, rate):
        if not isinstance(rate, (int, float)):
            raise TypeError("Rate must be a number")
        if rate < 0:
            self.status = "Negative commission"
            self.commission_rate = 0
        else:
            self.commission_rate = rate

    def get_status(self):
        return self.status
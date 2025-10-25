class User:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transactions = []

from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('Jane')
        self.p2 = Account('John')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p1.get_balance() == 0
        assert self.p2.get_name() == 'John'
        assert self.p2.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(500) is True
        assert self.p1.deposit(0) is False
        assert self.p1.deposit(-1) is False
        assert self.p1.get_balance() == 500

        assert self.p2.deposit(300) is True
        assert self.p2.deposit(0) is False
        assert self.p2.deposit(-1) is False
        assert self.p2.get_balance() == 300

    def test_withdraw(self):
        self.p1.deposit(200)
        assert self.p1.withdraw(100) is True
        assert self.p1.withdraw(0) is False
        assert self.p1.withdraw(-1) is False
        assert self.p1.withdraw(600) is False
        assert self.p1.get_balance() == 100

        self.p2.deposit(200)
        assert self.p2.withdraw(100) is True
        assert self.p2.withdraw(0) is False
        assert self.p2.withdraw(-1) is False
        assert self.p2.withdraw(400) is False
        assert self.p2.get_balance() == 100

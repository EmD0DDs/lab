from account import *
from pytest import *


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
        assert self.p1.deposit(20.5) is True
        assert self.p1.get_balance() == approx(20.5, abs=0.001)

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == approx(20.5, abs=0.001)

        assert self.p1.deposit(-1) is False
        assert self.p1.get_balance() == approx(20.5, abs=0.001)

        assert self.p2.deposit(50.75) is True
        assert self.p2.get_balance() == approx(50.75, abs=0.001)

        assert self.p2.deposit(0) is False
        assert self.p2.get_balance() == approx(50.75, abs=0.001)

        assert self.p2.deposit(-1) is False
        assert self.p2.get_balance() == approx(50.75, abs=0.001)

    def test_withdraw(self):
        self.p1.deposit(200)
        assert self.p1.get_balance() == 200

        assert self.p1.withdraw(50.50) is True
        assert self.p1.get_balance() == approx(149.5, abs=0.001)

        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == approx(149.5, abs=0.001)

        assert self.p1.withdraw(-1) is False
        assert self.p1.get_balance() == approx(149.5, abs=0.001)

        assert self.p1.withdraw(600) is False
        assert self.p1.get_balance() == approx(149.5, abs=0.001)

        self.p2.deposit(200)
        assert self.p2.get_balance() == 200

        assert self.p2.withdraw(50.5) is True
        assert self.p2.get_balance() == approx(149.5, abs=0.001)

        assert self.p2.withdraw(0) is False
        assert self.p2.get_balance() == approx(149.5, abs=0.001)

        assert self.p2.withdraw(-1) is False
        assert self.p2.get_balance() == approx(149.5, abs=0.001)

        assert self.p2.withdraw(400) is False
        assert self.p2.get_balance() == approx(149.5, abs=0.001)

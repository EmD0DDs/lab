class Account:
    """
    A class representing details for account object
    """
    def __init__(self, name: str, balance=0) -> None:
        """
        function to establish account object
        :param name: first name of person
        account_balance automatically set to 0
        """
        self.__account_name = name
        self.__account_balance = balance

    def deposit(self, amount) -> float:
        """
        function to increase account_balance based on input
        :param amount: amount of $ deposited into account
        :return: True if transaction affected account, False if not
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> float:
        """
        function to decrease account_balance based on input
        :param amount: amount of money to take out of account (must be more than $0 and less than current balance)
        :return: True if transaction affected account and false if not
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        function to return account balance
        :return: current account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        function to return account name
        :return: returns name account in under
        """
        return self.__account_name


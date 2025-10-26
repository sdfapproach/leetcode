# https://leetcode.com/problems/simple-bank-system/?envType=daily-question&envId=2025-10-26
# Simple Bank System

class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = [int(x) for x in balance]
        self.n = len(balance)

    def _valid(self, account):
        return 1 <= account <= self.n    

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if not self._valid(account1) or not self._valid(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._valid(account):
            return False
        self.balance[account - 1] += money
        return True

        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._valid(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
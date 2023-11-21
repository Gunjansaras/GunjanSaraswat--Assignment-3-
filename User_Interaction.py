class Account:
    def __init__(self, accountType, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self._accountType = accountType
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance
    def getAccountNumber(self):
        return self._accountNumber
    def getAccountHolderName(self):
        return self._accountType
    def getAccountType(self):
        return self._accountType
    def getRateOfInterest(self):
        return self._rateOfInterest
    def getCurrentBalance(self):
        return self._currentBalance
    def setAccountHolderName(self, newname):
        self._accountHolderName = newname
    def setRateOfInterest(self, newROI):
        self._rateOfInterest = newROI
    def deposit(self, money):
        self._currentBalance += money
        return self._currentBalance
    def withdraw(self,money):
        self._currentBalance-=money
        return self._currentBalance
    
class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__('savings', accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._minimumBalance = minimumBalance
    def withdraw(self, withdrawnMoney):
        if self._currentBalance - withdrawnMoney < self._minimumBalance:
            return 'Transaction Rejected'
        else:
            self._currentBalance -=withdrawnMoney
            return withdrawnMoney

    

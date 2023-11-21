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

class CheckingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, Overdraft):
        super().__init__('checking', accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraft = Overdraft
    def withdraw(self, withdrawnMoney):
        if withdrawnMoney > self._currentBalance + self._overdraft:
            return 'Transaction Rejected'
        else:
            self._currentBalance -=withdrawnMoney
            return withdrawnMoney

class Bank:
    def __init__(self):
        print('Welcome To the Bank!')
        self._biglist = []
        self.new_account = None
    def makelist(self):
        for i in range(6):
            account_Type = input('Enter Account Type: ')
            accountNo = int(input('Account Number: '))
            accountHolderName = input('Enter Account Holder Name: ')
            Rate_of_interest = int(input('Enter Rate of Interest: '))
            Current_Balance = int(input('Enter Current Balance: '))
            if (account_Type.lower() == 'savings'):
                minimumBalance = int(input('Enter Minimum balance: '))
                self.new_account = SavingsAccount(account_Type, accountNo, accountHolderName, Rate_of_interest, Current_Balance, minimumBalance)
            elif (account_Type.lower() == 'checking'):
                overdraft = int(input('Enter Overdraft limit: '))
                self.new_account = CheckingAccount(account_Type, accountNo, accountHolderName, Rate_of_interest, Current_Balance, overdraft)
            else:
                pass
            self._biglist.append(self.new_account)
    def getlist(self):
        return self._biglist
    def searchAccount(self, accountNo):
        for account in self._biglist:
            if (account.getAccountNumber() == accountNo):
                return account
    def OpenAccount(self, account_Type, accountno, name, Rate_of_interest, currentBalance):
        if (account_Type.lower() == 'savings'):
            minimumBalance = int(input('Enter Minimum balance: '))
            self.new_account = SavingsAccount(account_Type, accountno, name, Rate_of_interest, currentBalance, minimumBalance)
        elif (account_Type.lower() == 'checking'):
            overdraft = int(input('Enter Overdraft limit: '))
            self.new_account = CheckingAccount(account_Type, accountno, name, Rate_of_interest, currentBalance, overdraft)
        else:
            pass
        self._biglist.append(self.new_account)
        return self._biglist
    def addDeposit(self, accountNumber, money):
        for account in self._biglist:
            if (account.getAccountNumber() == accountNumber):
                account.deposit(money)


        
            

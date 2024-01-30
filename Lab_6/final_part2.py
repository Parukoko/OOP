# Class Code

##################################################################################
import datetime
class Bank:
	def __init__(self):
		self.__users = []
		self.__atms = []
	def insert_user(self, citizen_id, name):
		user = User(citizen_id, name)
		self.__users.append(user)
		return user
	def create_account(self, user, account_number, balance, card_number):
		account = Account(account_number, balance, card_number)
		user.get_accounts.append(account)
		return account
	def create_atm(self, atm_number, atm_balance):
		atm = AtmMachine(atm_number, atm_balance)
		self.__atms.append(atm)
		return atm
	@property
	def get_users(self):
		return self.__users
	@property
	def get_atms(self):
		return self.__atms
class User:
	def __init__(self, citizen_id, name):
		self.__citizen_id = citizen_id
		self.__name = name
		self.__accounts = []
	@property
	def get_citizen_id(self):
		return self.__citizen_id
	@property
	def get_name(self):
		return self.__name
	@property
	def get_accounts(self):
		return self.__accounts

class Account:
	def __init__(self, account_number, balance, card_number):
		self.__account_number = account_number
		self.__balance = balance
		self.__card_number = card_number
		self.__transactions = []
	@property
	def get_account_number(self):
		return self.__account_number
	@property
	def get_card_number(self):
		return self.__card_number
	@property
	def get_balance(self):
		return self.__balance
	def set_balance(self, balance):
		self.__balance = balance
	@property
	def get_transactions(self):
		return self.__transactions
	def deposit(self, atm, account, amount):
		if amount > 0:
			self.__balance += amount
			self.__transactions.append(Transaction("D", amount,None, atm.get_atm_number, self.__balance))
			atm.set_atm_balance(atm.get_atm_balance + amount)
			return "Success"
		else:
			return "ERROR Invalid"
	def withdraw(self, atm, account, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			self.__transactions.append(Transaction("W", amount,None, atm.get_atm_number, self.__balance))
			atm.set_atm_balance(atm.get_atm_balance - amount)
			return "Success"
		else:
			return "ERROR Invalid"
	def transfer(self, atm, account, target_account, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			target_account.set_balance(target_account.get_balance + amount)
			self.__transactions.append(Transaction("T", amount, target_account.get_account_number, atm.get_atm_number, self.__balance))
			target_account.get_transactions.append(Transaction("T", amount, self.__account_number, atm.get_atm_number, target_account.get_balance))
			return "Success"
		else:
			return "ERROR Invalid"
	def __str__(self):
		return f"Account Number: {self.get_account_number}, Card Number: {self.get_card_number}, Balance: {self.get_balance}"

class DepositAccount(Account):
	def __init__(self, account_number, balance):
		super().__init__(account_number, balance)
		self.__interest_rate = 0.05
	@property
	def get_interest_rate(self):
		return self.__interest_rate

class Transaction:
	def __init__(self, _type, amount, target_account_number, atm_number, balance):
		self.__type = _type
		self.__amount = amount
		self.__date_time = datetime.datetime.now().strftime("%c")
		self.__target_account_number = target_account_number
		self.__atm_number = atm_number
		self.__balance = balance
	def __str__(self):
		if self.__type.lower() == "t":
			return f"{self.__type}+-{self.__amount}-ATM:{self.__atm_number}-{self.__date_time}-{self.__target_account_number}-{self.__balance}"
		else:
			return f"{self.__type}-{self.__amount}-ATM:{self.__atm_number}-{self.__date_time}-{self.__balance}"

class AtmMachine:
	def __init__(self, atm_number, atm_balance):
		self.__atm_number = atm_number
		self.__atm_balance = atm_balance
	@property
	def get_atm_number(self):
		return self.__atm_number
	@property
	def get_atm_balance(self):
		return self.__atm_balance
	def set_atm_balance(self, atm_balance):
		self.__atm_balance = atm_balance
	def authenticate(self, bank_instance, atm_card, input_pin):
		for user in bank_instance.get_users:
			for account in user.get_accounts:
				if account.get_card_number == atm_card.get_card_number:
					if self.validate_pin(atm_card.get_pin, input_pin):
						return account
		return None
	def validate_pin(self, atm_pin, entered_pin):
		if entered_pin.isdigit() and len(entered_pin) == 4:
			return int(atm_pin) == int(entered_pin)
		return False

class AtmCard:
	def __init__(self, card_number, pin):
		self.__card_number = card_number
		self.__pin = pin
	@property
	def get_card_number(self):
		return self.__card_number
	@property
	def get_pin(self):
		return self.__pin

class DebitCard(AtmCard):
	def __init__(self, card_number, pin):
		super().__init__(card_number, pin)
	def purchase(self, account, atm, amount):
		if 0 < amount <= account.get_balance:
			account.set_balance(account.get_balance - amount)
			account.get_transactions.append(Transaction("P", amount, atm.get_atm_number))
			return "Success"
		else:
			return "ERROR Invalid"

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
# *** Dictionary นี้ ใช้สำหรับสร้าง user และ atm instance เท่านั้น
user = {'1-1101-12345-12-0':['Harry Potter','1234567890',20000,'12345'],
		'1-1101-12345-13-0':['Hermione Jean Granger','0987654321',1000,'12346']}
atm = {'1001':1000000,'1002':200000}

def add_instance(user_data, atm_data):
	bank = Bank()
	for citizen_id, user_info in user_data.items():
		name, account_number, balance, atm_number = user_info
		new_user = bank.insert_user(citizen_id, name)
		new_account = bank.create_account(new_user, account_number, balance, atm_number)
	for atm_number, atm_balance in atm_data.items():
		bank.create_atm(atm_number, atm_balance)
	return bank

bank_instance = add_instance(user, atm)


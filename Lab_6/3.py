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

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
# *** Dictionary นี้ ใช้สำหรับสร้าง user และ atm instance เท่านั้น
user = {'1-1101-12345-12-0':['Harry Potter','1234567890',20000,'12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321',1000,'12346']}

atm = {'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance จากข้อมูล Dictionary
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

def add_instance(user_data, atm_data):
	bank = Bank()
	for citizen_id, user_info in user_data.items():
		name, account_number, balance, atm_number = user_info
		new_user = bank.insert_user(citizen_id, name)
		bank.create_account(new_user, account_number, balance, atm_number)
	for atm_number, atm_balance in atm_data.items():
		bank.create_atm(atm_number, atm_balance)
	return bank

bank_instance = add_instance(user, atm)

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 3 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card 3) entered Pin ที่ user input ให้เครื่อง ATM
# TODO     return ถ้าบัตร และ Pin ถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 2 ตัว คือ
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 2 ตัว คือ
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 3 ตัว คือ
# TODO     1) instance ของ account ตนเอง 2) instance ของ account ที่โอนไป 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1")
harry_atm_card = AtmCard('12345', '1234')
authenticated_account_harry = bank_instance.get_atms[0].authenticate(bank_instance, harry_atm_card, '1234')
if authenticated_account_harry:
	print(f'Authenticated Account for Harry: {authenticated_account_harry}')
else:
	print('Authentication failed')
print("--------------------------------")

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("test case #2")
hermione_account = bank_instance.get_users[1].get_accounts[0]
result = hermione_account.deposit(bank_instance.get_atms[1], hermione_account, 1000)
print(f'Hermione account after test: {hermione_account.get_balance}')
print(f'Deposit result: {result}')
print("Hermione transactions:")
for transaction in hermione_account.get_transactions:
	print(transaction)
print("--------------------------------")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #3")
result_negative_deposit = hermione_account.deposit(bank_instance.get_atms[1], hermione_account, -1)
print(f'Deposit result with negative amount: {result_negative_deposit}')
print("--------------------------------")
# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("test case #4")
print(f'Hermione account before test: {hermione_account.get_balance}')
result_withdrawal = hermione_account.withdraw(bank_instance.get_atms[1], hermione_account, 500)
print(f'Hermione account after test: {hermione_account.get_balance}')
print(f'Withdrawal result: {result_withdrawal}')
print("Hermione transactions:")
for transaction in hermione_account.get_transactions:
	print(transaction)
print("--------------------------------")

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("test case #5")
result_over_withdrawal = hermione_account.withdraw(bank_instance.get_atms[1], hermione_account, 2000)
print(f'Withdrawal result with overdraft: {result_over_withdrawal}')
print("--------------------------------")

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("test case #6")
harry_account = bank_instance.get_users[0].get_accounts[0]
print(f'Harry account before test: {harry_account.get_balance}')
print(f'Hermione account before test: {hermione_account.get_balance}')
result_transfer = harry_account.transfer(bank_instance.get_atms[1], harry_account, hermione_account, 10000)
print(f'Harry account after test: {harry_account.get_balance}')
print(f'Hermione account after test: {hermione_account.get_balance}')
print(f'Transfer result: {result_transfer}')
print("Harry transactions:")
for transaction in harry_account.get_transactions:
    print(transaction)
print("Hermione transactions:")
for transaction in hermione_account.get_transactions:
    print(transaction)
print("--------------------------------")

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด
# กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("Test case #7")
print("Hermione transactions:")
for transaction in hermione_account.get_transactions:
	print(transaction)
print("--------------------------------")

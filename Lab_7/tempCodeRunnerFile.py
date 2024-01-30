	def __init__(self, account_no, user, amount):
		Account.__init__(self, account_no, user, amount)
		self.__card = None

	def add_card(self, card):
		self.__card = card

	def get_card(self):
		return self.__card
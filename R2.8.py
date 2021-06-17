#R-2.8

"""

Ubah deklarasi for loop pertama dalam pengujian CreditCard,
dari Code Fragment 2.3, sehingga pada akhirnya akan menyebabkan
salah satu dari tiga kartu kredit melampaui batas kreditnya.
Kartu kredit yang mana?

"""

#JAWABAN

"""

jawabannya adalah " California Savings "
jika mengubah price menjadi melebihi syntax dibawah maka kartu kredit yang terlebih dahulu akan melebihi adalah California Savings

syntax = if price + self._balance > self._limit:
      
"""

#PEMBUKTIAN

#pembuatan class
class CreditCard:

	def __init__(self, customer, bank, acnt, limit, balance = 0):
		"""
		Create a new credit card instance. 
		The initial balance is zero.
		"""
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = balance
		self._charge_count = 0

	def get_customer(self):
		"""Return the name of the customer"""
		return self._customer

	def get_bank(self):
		"""Return the bank's name"""
		return self._bank

	def get_account(self):
		"""Return the card identifying number (typically a str)"""
		return self._account

	def get_limit(self):
		"""Return current credit limit"""
		return self._limit

	def get_balance(self):
		"""Return current balance"""
		return self._balance

	def charge(self, price):
		"""
		Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed, False if charge was denied
		
		if not isinstance(price, (float, int)):
			raise ValueError('price must be a number.')
		"""
		if price + self._balance > self._limit:
                        #
			#print(f"Credit card with account number {self._account} denied. Accrued balance over limit.")
			
			return False
		else:
			self._balance += price
			"""
                        self._charge_count += 1
			if self._charge_count > 10:
				self._balance += 1	#$1 surcharge for all calls after 10 charges
			"""
			return True

	def make_payment(self, amount):
		if not isinstance(amount, (int, float)):
			raise ValueError('payment must be a number')
		elif amount < 0:
			raise ValueError('payment must be positive')
		"""Process customer payment that reduces the balance"""
		self._balance -= amount

#code fragment 2.3
if __name__ == '__main__':
	wallet = [ ]
	wallet.append(CreditCard( 'John Bowman' , 'California Savings' ,'5391 0375 9387 5309' , 2500) )
	wallet.append(CreditCard( 'John Bowman' , 'California Federal' ,'3485 0399 3395 1954' , 3500) )
	wallet.append(CreditCard( 'John Bowman' , 'California Finance' ,'5391 0375 9387 5309' , 5000) )

for val in range(1, 17):
	wallet[0].charge(val)
	wallet[1].charge(2*val)
	wallet[2].charge(3*val)

for c in range(3):
	print( 'Customer = ', wallet[c].get_customer( ))
	print( 'Bank = ', wallet[c].get_bank( ))
	print( 'Account = ', wallet[c].get_account( ))
	print( 'Limit = ', wallet[c].get_limit( ))
	print( 'Balance = ', wallet[c].get_balance( ))
	while wallet[c].get_balance( ) > 100:
		wallet[c].make_payment(100)
		print( 'New balance = ', wallet[c].get_balance( ))
	print( )

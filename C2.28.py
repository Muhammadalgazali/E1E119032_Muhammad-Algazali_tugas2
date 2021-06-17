# C-2.28
"""
Kelas PredatoryCreditCard dari Bagian 2.4.1
menyediakan metode bulan proses yang memodelkan
penyelesaian siklus bulanan. Ubah kelas sehingga
setelah pelanggan melakukan sepuluh panggilan untuk
menagih pada bulan berjalan, setiap panggilan
tambahan ke fungsi tersebut menghasilkan biaya tambahan $1.
"""

#JAWABAN

class PredatoryCreditCard(CreditCard):
    def init (self, customer, bank, acnt, limit, apr):
        super( ). init (customer, bank, acnt, limit) # call super constructor
        self. apr = apr

    def charge(self, price):
        success = super( ).charge(price) # call inherited method
            if not success:
            self. balance += 5 # assess penalty
            return success # caller expects return value

     def process month(self):
         if self. balance > 0:
        # if positive balance, convert APR to monthly multiplicative factor
            monthly factor = pow(1 + self. apr, 1/12)
            self. balance = monthly factor



# R-2.4
"""
Tulis kelas Python, Bunga, yang memiliki tiga variabel instan tipe str, int, dan float,
yang masing-masing mewakili nama bunga,jumlah kelopak, dan harganya.
Kelas Anda harus menyertakan metode konstruktor yang menginisialisasi
setiap variabel ke nilai yang sesuai,
dan kelas Anda harus menyertakan metode untuk menyetel nilai setiap jenis,
dan mengambil nilai setiap jenis.
"""

#JAWABAN

#pembuatan kelas
class Flower:
	def __init__(self, name, petals, price):
		self._name = name
		self._petals = petals
		self._price = price

	def get_name(self):
		return self._name

	def get_petals(self):
		return self._petals

	def get_price(self):
		return self._price

	def set_name(self, name):
		self._name = name

	def set_petals(self, petals):
		self._petals = petals

	def set_price(self, price):
		self._price = price

#pegirim nama bunga, jumlah kelopak, harganya
#nama bunga     = name
#jumlah kelopak = petals
#harganya       = price		
bunga = Flower('sunflower', 24, 1.25)

#print(bunga.get_price())
print("\n sebelum di ganti")
print(bunga.get_name())
print(bunga.get_petals())
print(bunga.get_price())

#pengubah syntak
bunga.set_name('rose')
bunga.set_petals(32)
bunga.set_price(1.45)

#pemanggil setelah diubah
print("\n setelah di ganti")
print(bunga.get_name())
print(bunga.get_petals())
print(bunga.get_price())

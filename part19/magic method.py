# MAGIC METHOD
# adalah kumpulan methods yang sudah built-in dalam python dengan ciri-ciri "__nama__"
# contoh :
# [1] __init__
# [2] __repr__
# [3] __str__
# [4] __add__
# dll....

class Buah:
    def __init__(self, nama, jumlah): #magic mathod dimana method ini akan langsung dieksekusi
        self.nama = nama
        self.jumlah = jumlah

    def __str__(self):
        return "Buah {} dengan jumlah {}".format(self.nama, self.jumlah)

    # contoh magic method untuk operasi matematika
    def __add__(self, objek):
        return self.jumlah + objek.jumlah

mangga = Buah("mangga", 7)
semangka = Buah("semangka", 10)

print(mangga) #dengan adanya method __str__ maka hasil print akan sesuai dengan isian __str__
# __str__ dan __repr__ berfungsi sama
# namun __repr__ biasa dipakai ketika proses perangcangan program untuk debugging

#penggunaan magic method __add__
print(semangka + mangga)
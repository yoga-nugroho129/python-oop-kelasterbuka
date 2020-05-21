# MULTIPLE INHERITANCE
# CONTOH SEDERHANA

def garis():
    print (50*"=")

garis()

# CONTOH INHERITANCE SINGLE/BIASA
class A:
    def method_A(self):
        print("Ini adalah method A")

# CLASS YANG MENG-HERITANCE DARI CLASS PERTAMA DIATAS
class pertama(A):
    pass

object1 = pertama()

# PEMANGGILAN CLASS DENGAN INHERITANCE BIASA
object1.method_A()

garis()

# CONTOH PENERAPAN MULTIPLE INNHERITANCE
class B:
    def method_B(self):
        print("Ini method B")

class C:
    def method_C(self):
        print("ini method C")

# CLASS YANG MENG-HERITANCE DARI 2 CLASS DIATAS
class multipleInherit(B, C):
    pass

object2 = multipleInherit()

# PENGGUNAAN MULTIPLE INHERITANCE DARI CLASS B DAN C
object2.method_B()
object2.method_C()

garis()

########################
########################

# CONTOH PENERAPAN MULTIPLE INHERITANCE
# TERDAPAT KARAKTER PEMAIN BOLA YANG MENG-HERITANCE DARI 2 CLASS
# CLASS PERTAMA ADALAH CLASS CLUB
# CLASS KEDUA ADALAH CLASS POSISI

class Club:
    def clubPemain(self, namaClub):
        self.club = namaClub

    def showClub(self):
        print(self.club)

class Posisi:
    def posisiPemain(self, namaPosisi):
        self.posisiPemain = namaPosisi

    def showPosisi(self):
        print(self.posisiPemain)

# CLASS YANG MENG-HERITANCE DARI 2 CLASS DIATAS
class PemainBola(Club, Posisi):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        print(self.name, "\n\t",self.nationality)

ronaldo = PemainBola("C. Ronaldo", "Portugal")

# PENGGUNAAN MULTIPLE INHERITANCE
ronaldo.clubPemain("Juventus FC")
ronaldo.posisiPemain("Winger")

ronaldo.showPosisi()
ronaldo.showClub()
### staticmethod & classmethod
### encapsulasi dengan menggunakan staticmethod dan classmethod

### contoh implementasi

class Karakter:
    # private class variabel
    __jumlahKarakter = 0

    def __init__(self,name):
        self.name = name
        Karakter.__jumlahKarakter += 1

    # penggunaan getter untuk mengakses object/instance dalam class karakter
    def getJumlah1(self):
        return Karakter.__jumlahKarakter

    # penggunaan getter untuk mengakses class Karakter
    def getJumlah2():
        return Karakter.__jumlahKarakter

    # sehingga untuk membuat fungsi yang dapat mengakses class maupun object dapat digunakan @staticmethod
    @staticmethod
    def getJumlah3():
        return Karakter.__jumlahKarakter

    # penggunaan classmethod
    # penggunaan classmethod ini menimpa argumen self yang biasanya dipakai serta memudahkan ketika ada perubahan nama class tidak harus merubah fungsi pemanggil yang sudah dirancang
    @classmethod
    def getJumlah4(cls):
        return cls.__jumlahKarakter

naruto = Karakter("Uzumaki Naruto")

luffy = Karakter("Monkey D Luffy")

saitama = Karakter("Saitama-sensei")


# PEMANGGILAN GETTER 1

#print(Karakter.getJumlah1()) #>>># dari hasil diketahui bahwa error karena penggunaan getter hanya berlaku untuk instance saja karena didalam fungsi getJumlah terdapat adanya "self"

print(naruto.getJumlah1()) #>>># namun jika menggunakan instance/object maka fungsi dapat berjalan untuk menghitung jumlah karakter yang ada

# PEMANGGILAN GETTER 2
print(Karakter.getJumlah2()) #>>># maka dengan penggunaan fungsi tanpa self maka dapat digunakan utnuk mengakses object dalam class
#print(luffy.getJumlah2()) #>>># namun model getJumlah2 tanpa self tidak dapat untuk mengakses object


# PEMANGGILAN GETTER 3 (@staticmethod)
print(saitama.getJumlah3()) #>>># penggunaan untuk mengaskses object = Lancar
print(Karakter.getJumlah3())  #>>># penggunaan untuk mengaskses class = Lancar


# PEMANGGILAN GETTER 4 (@classmethod)
print(Karakter.getJumlah4())
print(naruto.getJumlah4())






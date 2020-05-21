### private variable
### contoh variabel non-private/public

class Karakter:
    def __init__(self, name, skill):
        self.name = name ### variabel public
        self.skill = skill # variabel public dapat diakses dan dirubah oleh user

naruto = Karakter("naruto", "jurus bayangan")

### memeriksa instance "naruto"
print(naruto.__dict__)

### memeriksa skill "naruto"
print(naruto.name)

### merubah variabel karena bukan variabel private
naruto.skill = "Chidori"

### memeriksa ulang hasil perubahan
print(naruto.__dict__)
### variabel skill instance naruto telah dirubah

print(50 * "=")

### contoh penggunaan variabel private
class Hero:
    def __init__(self, name, skill):
        self.__name = name ### dengan penambahan "__"  maka variabel menjadi private
        self.__skill = skill

flash = Hero("Flash", "Lighting Speed")

print(flash.__dict__)

### percobaan mengubah skill pada Hero
flash.__skill = "terbang"

### maka skill dari flash tidak akan berubah namun akan menjadi variabel baru
print(flash.__dict__)

### percobaan mengakses nama Hero maka akan terjadi error
print(flash.__name)

print(30 * "=")


### variabel protected menggunakan "_" dengan sistem penerapan seperti variabel private
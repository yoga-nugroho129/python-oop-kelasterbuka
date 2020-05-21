### PENGANTAR ENCAPSULASI
### Berguna ketika digunakan untuk mengakses variabel private
### sehingga variabel private bisa diakses dan dirubah seperti variabel public
### namun proses perubahan dilakukan dibelakang layar bukan oleh user
### menggunakan fungsi GETTER dan SETTER

# pembuatan class
class Hero:
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

# GETTER = membuat fungsi untuk mengakses/mengambil variabel private
# contoh untuk variabel nama
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

# SETTER = membuat untuk men-setting/merubah variabel private
# contoh untuk perubahan nilai Health
    def diserang(self, serangan):
        self.__health -= serangan


# awalan
gundala = Hero("Gundala", 100, 5)

# pemanggilan fungsi GETTER
# cara 1
print(Hero.getName(gundala))
print(Hero.getHealth(gundala))
# cara 2
print(gundala.getHealth())
print(gundala.getName())

print(10*"=")

# pemanggilan fungsi SETTER
print(gundala.getHealth())
gundala.diserang(5)
print(gundala.getHealth())
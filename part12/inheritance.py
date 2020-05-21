#inheritance = warisan
#digunakan agar object tidak perlu mengulang-ulang fungsi tertentu

#Class hero ini merupakan super class yang memiliki sub-class
class Hero:
    def __init__(self, name, power):
        self.__name = name
        self.__power = power

#sub-class dengan contoh tipe Hero yang ada dengan isian dalam (...) adalah class supper nya
class HeroTipeMesin(Hero):
    pass

class HeroTipeNinja(Hero):
    pass

#contoh penggunaan oleh object yang mengacu pada class Super
luffy = Hero("Monkey D Luffy", "Gomu Gomu no Mi")
print(luffy.__dict__)


#contoh penggunaan object dengan sub-class pertama
gundam = HeroTipeMesin("Gundam", "Saber Shot")
print(gundam.__dict__)

#contoh penggunaan object dengan sub-class pertama
naruto = HeroTipeNinja("Uzumaki Naruto", "Bijuu Mode")
print(naruto.__dict__)
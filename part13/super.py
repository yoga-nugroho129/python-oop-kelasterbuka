#INHERITANCE DENGNA MENGGUNAKAN SUPER
print(50*"=")
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


#contoh untuk penerapan karakter hero dengan spesifikasi health tertentu
#hero Ninja memiliki health 100 dan hero Pirate memiliki health 150

###########################
######## CARA KE-1 ########
###########################
class Hero_ninja(Hero): #menggunakan cara biasa (harus diulang-ulang)
    def __init__(self, name): #berulang karena sama dengan class Hero diatas
        self.name = name
        self.health = 100

class Hero_pirate(Hero):
    def __init__(self, name):
        self.name = name
        self.health = 150

naruto = Hero_ninja("Uzumaki Naruto")
luffy = Hero_pirate("Monkey D Luffy")

print(naruto.name, "memiliki health sebesar", naruto.health)
print(luffy.name, "memiliki health sebesar", luffy.health)

print(50*"=")

###########################
######## CARA KE-2 ########
###########################
class Hero_shinobi(Hero): #menggunakan cara PEMANGGILAN __init__
    def __init__(self, name):
        Hero.__init__(self, name, 100) #rawan ketika nama "Hero" dirubah maka harus mengganti semua yang berkaitan dengan nama baru

class Hero_pendekarPedang(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 200)

kakashi = Hero_shinobi("Hatake Kakashi")
zoro = Hero_pendekarPedang("Roronoa Zoro")

print(zoro.name, "memiliki health sebesar", zoro.health)
print(kakashi.name, "memiliki health sebesar", kakashi.health)

print((50 * "="))

###########################
######## CARA KE-3 ########
###########################
class Hero_NINJA(Hero): #menggunakan cara SUPER
    def __init__(self, name):
        super().__init__(name, 100) #dengan super maka ketika terjadi perubahan nama "Hero" maka semua langsung menyesuaikan

class Hero_PIRATE(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

gaara = Hero_NINJA("Sabaku Gaara")
sanji = Hero_PIRATE("Vinsmoke Sanji")

print(gaara.name, "memiliki health sebesar", gaara.health)
print(sanji.name, "memiliki health sebesar", sanji.health)

print((50 * "="))

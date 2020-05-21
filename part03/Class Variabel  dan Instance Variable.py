class Hero():
    #class variabel (variabel yang dimiliki secara umum
    # contoh untuk menghitung jumlah hero
    jumlahHero = 0

    def __init__(self, name, attack, healt, defense):
        # bisa disebut sebagai instanse variabel
        self.name = name
        self.attack = attack
        self.health = healt
        self.defense =defense
        Hero.jumlahHero += 1
        print("Membuat Hero dengan nama", name)

hero1 = Hero("Iron Man", 80, 100, 70)
print(Hero.jumlahHero)

hero2 = Hero("Batman", 85, 90, 85)
print(Hero.jumlahHero)

hero3 = Hero("Gundala", 95, 80, 75)
print(Hero.jumlahHero)

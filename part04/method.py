###

class Hero():
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealt, inputAttack, inputDefense):
        # instance variable
        self.name = inputName
        self.health = inputHealt
        self.attack = inputAttack
        self.defense = inputDefense
        Hero.jumlah += 1
        print("Hero no. urut", Hero.jumlah, "adalah", inputName)

    # membuat method tanpa argumen dan tanpa return
    def namaHero(self):
        print("Namaku adalah", self.name)

    # membuat method dengan argumen
    def defenseUp(self, up):
        self.defUp = up
        self.health += up

    # membuat method dengan return
    def showAttack(self):
        return self.attack

hero1 = Hero("Iron Man", 90, 70, 85)
hero2 = Hero("Batman", 80, 80, 80)
hero3 = Hero("Gathotkaca", 90, 75, 75)

# aksi untuk method tanpa argumen dan tanpa return
hero1.namaHero()

# aksi untuk method dengan argumen
hero2.defenseUp(100)
print(hero2.health)

# aksi untuk method dengan return
print(hero1.showAttack())
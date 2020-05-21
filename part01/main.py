### Pengenalan Object Dasar
### contoh membuat object berupa karakter hero
### menggunakan magic keyword __init__

### Class/Template
class Hero():
    def __init__(self, name, attack, healt, defense):
        self.name = name
        self.attack = attack
        self.health = healt
        self.defense =defense

hero1 = Hero("Iron Man", 80, 100, 70)
hero2 = Hero("Batman", 85, 90, 85)

print(hero1.__dict__)
print(hero2.__dict__)
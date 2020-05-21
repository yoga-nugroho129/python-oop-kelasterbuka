### game sederhana berbasis text
### 2 karakter saling menyerang

class Hero:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    ### fungsi untuk menyerang
    def serang(self, Hero): #nama variabel "musuh"=bebas asal sama dengan nama yang dibawah
        print(self.name, "menyerang", Hero.name)
        #ketika sudah diserang maka musuh harus tau bahwa musuh diserang dengan syntax
        Hero.diserang(self, self.attack)

    def diserang(self, Hero, attackLawan):
        print(self.name, "diserang", Hero.name)
        attackDiterima = attackLawan/self.defense
        print("Serangan bernilai", str(attackDiterima))
        self.health -= attackDiterima
        print("Health", self.name, "tersisa", self.health, "\n",10*"-")



### instance
batman = Hero("Batman", 100, 10, 10)
robin = Hero("Robin", 90, 5, 20)

### running game
print(3*"=", "GAME MULAI", 3 * "=")
batman.serang(robin)
batman.serang(robin)
robin.serang(batman)

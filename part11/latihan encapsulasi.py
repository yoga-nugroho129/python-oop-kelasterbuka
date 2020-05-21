### EXERCISE ENCAPSULASI DENGAN GETTER & SETTER PYTHON

class Hero:
    #privet class variabel
    __jumlah = 0

    def __init__(self, name, health, attack, defense):
        self.__name = name
        self.__healthStandard = health
        self.__attackStandard = attack
        self.__defenseStandard = defense
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandard * self.__level
        self.__attack = self.__attackStandard * self.__level
        self.__defense = self.__defenseStandard * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} : \n \t Level = {} \n \t Health = {}/{} \n \t Attack = {} \n \t Defense = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attack, self.__defense)


    @property
    def gainExp(self):
        pass

#perancangan sistem gain EXP untuk meningkatkan level Hero
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name, "level UP!!")
            self.__level += 1
            self.__exp -= 100
            self.__healthMax = self.__healthStandard * self.__level
            self.__attack = self.__attackStandard * self.__level
            self.__defense = self.__defenseStandard * self.__level

            self.__health = self.__healthMax

    def serang(self, musuh):
        self.gainExp = 50

print(20*"=")

naruto = Hero("Uzumaki Naruto", 100, 8, 7)
luffy = Hero("Monkey D Luffy", 100, 7, 9)

print(naruto.info)

print(20*"=")

#penggunaan gain exp pada karakter Hero
# naruto.gainExp = 80
# naruto.gainExp = 30

#penggunaan gain exp melalui menyerang karakter/Hero lain
naruto.serang(luffy)
naruto.serang(luffy)

print(naruto.info)















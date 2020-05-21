#INHERITANCE dengan override method
#OVERRIDE method berfung sebagai overwrite/menimpa fungsi dalam class

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} memiliki health poin sebesar {}".format(self.name, self.health))


class Hero_ninja(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

class Hero_pirate(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

    #################################
    ####### OVERRIDE showInfo #######
    #################################
    def showInfo(self):
        print("{} bertipe Pirate dengan Health Poin sebesar {}".format(self.name, self.health))


naruto = Hero_ninja("Uzumaki Naruto")
luffy = Hero_pirate("Monkey D Luffy")

naruto.showInfo() #sesuai dengan standard fungsi pada class super nya
luffy.showInfo() #khusus untuk sowInfo ter overrde oleh fungsi dalam sub-class nya
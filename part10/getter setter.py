### menggunakan Getter dan Setter dengan cara python

### getter da setter dengan cara biasa
class Tokoh:
    def __init__(self, nama, kekuatan, pertahanan):
        self.__nama = nama
        self.__kekuatan = kekuatan
        self.__pertahanan = pertahanan

#getter OOP biasa
    def getNama(self):
        return self.__nama

#setter OOP biasa
    def setNama(self, namaBaru):
        self.__nama = namaBaru


naruto = Tokoh("Uzumaki Naruto",25, 300)


#penggunaan getter OOP biasa
print(naruto.getNama())

#penggunaan setter OOP biasa
naruto.setNama("Monkey D Luffy")
print(naruto.getNama())


print("\n", 30*">")

###getter dengan cara ala python
class Karakter:
    def __init__(self, name, attack, defense):
        self.__name = name
        self.__attack = attack
        self.__defense = defense

#untuk menggunakan getter setter ala python maka harus dijadikan sebagai property terlebih dahulu dengan cara
    @property #dekorator untuk property
    def name(self):
        pass

# getter ala python
    @name.getter
    def name(self):
        return self.__name

#setter ala python
    @name.setter
    def name(self, newName):
        self.__name = newName

#BONUS FUNGSI DELETER
    @name.deleter
    def name(self):
        self.__name = None

#juga harus dijadikan sebagai property terlebih dahulu dengan cara


zoro = Karakter("Roronoa Zoro",30,90)

#penggunaan getter ala python
print(zoro.name)


#penggunaan setter ala python
print(zoro.__dict__)
zoro.name = "Konohamaru" #penggunaan setter menjadi lebih simple seperti perumusan variable
print(zoro.__dict__)


#penggunaan fungsi tambahan (DELETER)
del zoro.name
print(zoro.__dict__)
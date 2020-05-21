# METHOD RESOLUTION ORDER BERHUBUNGAN DENGAN MULTIPLE INHERITANCE
# CONTOH KASUS

class A:
    def show(self): #nama show sama dengan class B
        print("Ini adalah show A")

class B:
    def show(self): #nama show sama dengan class A
        print("Ini adalah show B")

class C(A,B):
    pass

objek = C()

objek.show() # dengan nama function yang sama (show) maka,
# urutan yang akan dieksekusi adalah C kemudian A kemudian B
# jika didalam C terdapat function show maka C akan diprioritaskan
# sesuai dengan urutan posisi dari kiri

# DIAMOND PROBLEM PADA PENGGUNAAN MULTIPLE INHERITANCE

class A:
    def show(self):
        print("Ini adalah fungsi A")

class B(A):
    def show(self):
        print("Ini adalah method B")

class C(A):
    def show(self):
        print("Ini adalah method B")

class D(B,C):
    pass

# BENTUK HUBUNGAN CLASS DIATAS ADALAH MEMBENTUK DIAMOND
# SEHINGGA URUTAN EKSEKUSI UNTUK OBJECT DALAM D ADALAH

objek = D()
objek.show()

# show diatas akan melakukan eksekusi dengan urutan
# 1) memeriksa dalam class nya sendiri (D)
# 2) urutan dari kiri yang pertama yaitu B
# 3) urutan dari kiri yang selanjutnya yaitu C
# 4) selanjutnya urutan teratas yaitu A
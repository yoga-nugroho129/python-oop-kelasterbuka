### OOP dengan GUI menggunakan built-in tkinter

import tkinter

## comand pada tombol sebagai aksi ketika tombol ditekan
def tombolDitekan():
    tombolTelahDitekan = tkinter.Label(jendela_utama, text = "tombol 1 telah ditekan")
    tombolTelahDitekan.pack()

## memberi variabel untuk memanggil tkinter
jendela_utama = tkinter.Tk()

## tulisan/label yang nanti akan diletakkan di dalam tkinter
label1 = tkinter.Label(jendela_utama, text = "ini label 1")

## tombol dengan perintah/command
tombol1 = tkinter.Button(jendela_utama, text = "ini tombol 1", command = tombolDitekan)

## peletakkan label & tombol kedalam GUI
label1.pack()
tombol1.pack()

## memanggil GUI

jendela_utama.mainloop()
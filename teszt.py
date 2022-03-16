from tkinter import *
import math

def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Összeg: '+str(c))

def kivonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a - b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Különbség: '+str(c))

def szorzas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a * b
    mezo3.delete(0, END)
    mezo3.insert(0, 'Szorzat: '+str(c))

def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    if b == 0:
        mezo3.delete(0, END)
        mezo3.insert(0, 'Nullával nem lehet osztani!')
    else:
        c = a / b
        mezo3.delete(0, END)
        mezo3.insert(0, 'Hányados: '+str(c))

def negyzetre_emeles():
    a = int(mezo1.get())
    c = a * a
    mezo3.delete(0, END)
    mezo3.insert(0, f'{a} négyzete: '+str(c))

def negyzet_gyok():
    a = int(mezo1.get())
    if a < 0:
        mezo3.delete(0, END)
        mezo3.insert(0, 'Nem negatívot adjon meg!')
    else:
        c = math.sqrt(a)
        mezo3.delete(0, END)
        mezo3.insert(0, f'{a} négyzetgyöke: '+str(c))

foablak = Tk ()

elsosor = Label (foablak, text='Első szám:')
elsosor.grid(row=0, column=2)

masodiksor = Label (foablak, text='Második szám:')
masodiksor.grid(row=1, column=2)

erdmenysor = Label (foablak, text='Eredmény:')
erdmenysor.grid(row=2, column=2)


gkilepes = Button (foablak, text='Kilépés', command=foablak.destroy)
gkilepes.grid(row=8, column=3)




gosszead = Button (foablak, text='Összeadás', command=osszeg)
gosszead.grid(row=3, column=2, )

gkiv = Button (foablak, text='Kivonas', command=kivonas)
gkiv.grid(row=4, column=2, )

gszorz = Button (foablak, text='Szorzás', command=szorzas)
gszorz.grid(row=5, column=2, )

goszt = Button (foablak, text='Osztás', command=osztas)
goszt.grid(row=6, column=2, )

gnegyzetre = Button (foablak, text='Négyzetre emelés', command=negyzetre_emeles)
gnegyzetre.grid(row=7, column=2, )

gnegyzetgyok = Button (foablak, text='Négyzetgyökvonás', command=negyzet_gyok)
gnegyzetgyok.grid(row=8, column=2, )


mezo1 = Entry (foablak)
mezo1.grid(row=0, column=3)
mezo2 = Entry (foablak)
mezo2.grid(row=1, column=3)
mezo3 = Entry (foablak)
mezo3.grid(row=2, column=3)



can1= Canvas(foablak, width=460, height=460, bg="white")
photo = PhotoImage(file="SB.gif")
item = can1.create_image(80,80, image= photo)
can1.grid(row=9, column=3)





foablak.mainloop ()
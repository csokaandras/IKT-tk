from tkinter import *

#Névjegy ablak
def nevjegy ():
    nevjegyA = Toplevel (foablak)
    uz = Message (nevjegyA, text='Készítette: Csóka András\nBaja\n2022.04.06', width=300).pack ()
    kilepB = Button (nevjegyA, text='Kilép', command=nevjegyA.destroy).pack ()
    nevjegyA.mainloop ()
#Névjegy vége

#Felszín ablak
def felszin ():
    def szamitas ():
        a = int(aE.get())
        b = int(bE.get())
        c = int(cE.get())
        A = 2 * (a*b + b*c + a*c)
        eredmenyE.delete (0, END)
        eredmenyE.insert (0, str(A))

    felszinA = Toplevel (foablak)

    aL = Label (felszinA, text='a:')
    aL.grid (column=1, row=1)
    aE = Entry (felszinA)
    aE.grid (column=2, row=1)

    bL = Label (felszinA, text='b:')
    bL.grid (column=1, row=2)
    bE = Entry (felszinA)
    bE.grid (column=2, row=2)

    cL = Label (felszinA, text='c:')
    cL.grid (column=1, row=3)
    cE = Entry (felszinA)
    cE.grid (column=2, row=3)

    eredmenyL = Label (felszinA, text='Eredmény')
    eredmenyL.grid (column=1, row=4)
    eredmenyE = Entry (felszinA)
    eredmenyE.grid (column=2, row=4)

    szamitasB = Button (felszinA, text='Számítás', command=szamitas)
    szamitasB.grid (column=2, row=4, sticky=W)

    felszinA.mainloop ()
#Felszín ablak vége

#Térfogat ablak
def terfogat ():
    def szamitas ():
        a = int(aE.get())
        b = int(bE.get())
        c = int(cE.get())
        V = a * b * c
        eredmenyE.delete (0, END)
        eredmenyE.insert (0, str(V))

    terfogatA = Toplevel (foablak)

    aL = Label (terfogatA, text='a:')
    aL.grid (column=1, row=1)
    aE = Entry (terfogatA)
    aE.grid (column=2, row=1)

    bL = Label (terfogatA, text='b:')
    bL.grid (column=1, row=2)
    bE = Entry (terfogatA)
    bE.grid (column=2, row=2)

    cL = Label (terfogatA, text='c:')
    cL.grid (column=1, row=3)
    cE = Entry (terfogatA)
    cE.grid (column=2, row=3)

    eredmenyL = Label (terfogatA, text='Eredmény')
    eredmenyL.grid (column=1, row=4)
    eredmenyE = Entry (terfogatA)
    eredmenyE.grid (column=2, row=4)

    szamitasB = Button (terfogatA, text='Számítás', command=szamitas)
    szamitasB.grid (column=2, row=4, sticky=W)

    terfogatA.mainloop ()
#Térfogat ablak vége

#Főablak
foablak = Tk ()
foablak.title ('A téglatest adatai')
foablak.minsize (width=300, height=100)

menusor = Frame (foablak)
menusor.pack (side=TOP, fill=X)

menuF = Menubutton (menusor, text='Fájl', underline=0)
menuF.pack (side=LEFT)

fajl = Menu (menuF)
fajl.add_command (label='Névjegy', command=nevjegy, underline=0)
fajl.add_command (label='Kilépés', command=foablak.destroy, underline=0)
menuF.config(menu=fajl)

menuT = Menubutton (menusor, text='Téglatest', underline=0)
menuT.pack (side=LEFT)

teglatest = Menu (menuT)
teglatest.add_command (label='Térfogat', command=terfogat, underline=0)
teglatest.add_command (label='Felszín', command=felszin, underline=0)
menuT.config(menu=teglatest)


foablak.mainloop ()
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
        a = float(aE.get())
        b = float(bE.get())
        c = float(cE.get())
        A = 2 * (a*b + b*c + a*c)
        eredmenyE.delete (0, END)
        eredmenyE.insert (0, str(A))

    def hülyee ():
        try:
            szamitas ()
        except:
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Nincs értelme a számításnak.' )

    def törles ():
        aE.delete (0, END)
        bE.delete (0, END)
        cE.delete (0, END)
        eredmenyE.delete (0, END)

    felszinA = Toplevel (foablak)

    aL = Label (felszinA, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (felszinA, width=27)
    aE.grid (column=2, row=1)

    bL = Label (felszinA, text='b:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (felszinA, width=27)
    bE.grid (column=2, row=2)

    cL = Label (felszinA, text='c:')
    cL.grid (column=1, row=3, sticky=E)
    cE = Entry (felszinA, width=27)
    cE.grid (column=2, row=3)

    eredmenyL = Label (felszinA, text='Eredmény:')
    eredmenyL.grid (column=1, row=4, sticky=E)
    eredmenyE = Entry (felszinA, width=27)
    eredmenyE.grid (column=2, row=4)

    szamitasB = Button (felszinA, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=5, sticky=W)

    kilepB = Button (felszinA, text='Kilépés', command=felszinA.destroy)
    kilepB.grid (column=2, row=5, sticky=E)

    törlesB = Button (felszinA, text='Törlés', command=törles)
    törlesB.grid (column=1, row=5)

    felszinA.mainloop ()
#Felszín ablak vége

#Térfogat ablak
def terfogat ():
    def szamitas ():
        a = float(aE.get())
        b = float(bE.get())
        c = float(cE.get())
        V = a * b * c
        eredmenyE.delete (0, END)
        eredmenyE.insert (0, str(V))

    def hülyee ():
        try:
            szamitas ()
        except:
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Nincs értelme a számításnak.' )

    def törles ():
        aE.delete (0, END)
        bE.delete (0, END)
        cE.delete (0, END)
        eredmenyE.delete (0, END)

    terfogatA = Toplevel (foablak)

    aL = Label (terfogatA, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (terfogatA, width=27)
    aE.grid (column=2, row=1)

    bL = Label (terfogatA, text='b:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (terfogatA, width=27)
    bE.grid (column=2, row=2)

    cL = Label (terfogatA, text='c:')
    cL.grid (column=1, row=3, sticky=E)
    cE = Entry (terfogatA, width=27)
    cE.grid (column=2, row=3)

    eredmenyL = Label (terfogatA, text='Eredmény:')
    eredmenyL.grid (column=1, row=4, sticky=E)
    eredmenyE = Entry (terfogatA, width=27)
    eredmenyE.grid (column=2, row=4)

    szamitasB = Button (terfogatA, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=5, sticky=W)

    kilepB = Button (terfogatA, text='Kilépés', command=terfogatA.destroy)
    kilepB.grid (column=2, row=5, sticky=E)

    törlesB = Button (terfogatA, text='Törlés', command=törles)
    törlesB.grid (column=1, row=5)

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
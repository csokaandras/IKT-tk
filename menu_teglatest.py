from tkinter import *
import math

#Névjegy ablak
def nevjegy ():
    nevjegyA = Toplevel (foablak)
    nevjegyA.title ('Névjegy')
    uz = Message (nevjegyA, text='Készítette: Csóka András\nBaja\n2022.04.06', width=300).pack ()
    kilepB = Button (nevjegyA, text='Kilép', command=nevjegyA.destroy).pack ()
    nevjegyA.mainloop ()
#Névjegy vége

#Felszín téglatest ablak
def felszinT ():
    def szamitas ():
        if aE.get() == '' or bE.get() == '' or cE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            a = float(aE.get())
            b = float(bE.get())
            c = float(cE.get())
            
            if a <= 0 or b <= 0 or c <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
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

    felszinA.title ('Téglatest felszíne')
    felszinA.minsize (width=300, height=100)

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
#Felszín téglatest ablak vége

#Térfogat téglatest ablak
def terfogatT ():
    def szamitas ():
        if aE.get() == '' or bE.get() == '' or cE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            a = float(aE.get())
            b = float(bE.get())
            c = float(cE.get())
            
            if a <= 0 or b <= 0 or c <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
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

    terfogatA.title ('Téglatest térfogata')
    terfogatA.minsize (width=300, height=100)

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
#Térfogat téglatest ablak vége

#Felszín henger ablak
def felszinH ():
    def szamitas ():
        if aE.get() == '' or bE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            r = float(aE.get())
            m = float(bE.get())
            #c = float(cE.get())
            
            if r <= 0 or m <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
                A = round (2 * math.pi * r * (r + m), 2)
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

    felszinA.title ('Henger felszíne')
    felszinA.minsize (width=300, height=100)

    aL = Label (felszinA, text='Sugár:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (felszinA, width=27)
    aE.grid (column=2, row=1)

    bL = Label (felszinA, text='Magasság:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (felszinA, width=27)
    bE.grid (column=2, row=2)

    '''
    cL = Label (felszinA, text='c:')
    cL.grid (column=1, row=3, sticky=E)
    cE = Entry (felszinA, width=27)
    cE.grid (column=2, row=3)
    '''

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
#Felszín henger ablak vége

#Térfogat henger ablak
def terfogatH ():
    def szamitas ():
        if aE.get() == '' or bE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            r = float(aE.get())
            m = float(bE.get())
            #c = float(cE.get())

            if r <= 0 or m <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
                V = round (math.pi * r * r * m, 2)
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
        eredmenyE.delete (0, END)

    terfogatA = Toplevel (foablak)

    terfogatA.title ('Henger térfogat')
    terfogatA.minsize (width=300, height=100)

    aL = Label (terfogatA, text='Sugár:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (terfogatA, width=27)
    aE.grid (column=2, row=1)

    bL = Label (terfogatA, text='Magasság:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (terfogatA, width=27)
    bE.grid (column=2, row=2)

    '''
    cL = Label (terfogatA, text='c:')
    cL.grid (column=1, row=3, sticky=E)
    cE = Entry (terfogatA, width=27)
    cE.grid (column=2, row=3)
    '''

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
#Térfogat henger ablak vége

#Főablak
foablak = Tk ()
foablak.title ('Térfogat és felszín')
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
teglatest.add_command (label='Térfogat', command=terfogatT, underline=0)
teglatest.add_command (label='Felszín', command=felszinT, underline=0)
menuT.config(menu=teglatest)

menuH = Menubutton (menusor, text='Henger', underline=0)
menuH.pack (side=LEFT)

henger = Menu (menuH)
henger.add_command (label='Térfogat', command=terfogatH, underline=0)
henger.add_command (label='Felszín', command=felszinH, underline=0)
menuH.config(menu=henger)


foablak.mainloop ()
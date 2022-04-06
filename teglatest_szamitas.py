from tkinter import *

main = Tk()
main.title ('A téglatest adatai')
main.minsize (width=300, height=100)

def ablak2 ():

    abl2 = Toplevel(main)
    abl2.title ('Eredmények')
    abl2.minsize (width=300, height=100)

    felszinL = Label  (abl2, text='Felsín:')
    felszinL.grid (column=1, row=1)
    terfogatL = Label (abl2, text='Térfogat')
    terfogatL.grid (column=1, row=2)

    felszinE = Entry (abl2)
    felszinE.grid (column=2, row=1)
    terfogatE = Entry (abl2)
    terfogatE.grid (column=2, row=2)

    a = int(aE.get())
    b = int(bE.get())
    c = int(cE.get())

    V = a * b * c
    A = 2 * (a*b + b*c + a*c)

    felszinE.insert (0, str(A))
    terfogatE.insert (0, str(V))

aL = Label (main, text='a:')
aL.grid (column=1, row=1)
aE = Entry (main)
aE.grid (column=2, row=1)

bL = Label (main, text='b:')
bL.grid (column=1, row=2)
bE = Entry (main)
bE.grid (column=2, row=2)

cL = Label (main, text='c:')
cL.grid (column=1, row=3)
cE = Entry (main)
cE.grid (column=2, row=3)

szamitasB = Button (main, text='Számítás', command=ablak2)
szamitasB.grid (column=2, row=4, sticky=W)
main.mainloop()

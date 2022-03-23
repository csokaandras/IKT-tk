from tkinter import *
import math

def szamitas ():
    r = int(sugarbe.get())
    m = int(magssagbe.get())

    terfogat = round (math.pi * r * r * m, 2)
    terfogatki.delete (0, END)
    terfogatki.insert (0, str(terfogat)+' cm3' )

    vassur = round (7.874 * terfogat, 2)
    vashengerki.delete (0, END)
    vashengerki.insert (0, str(vassur)+' g' )

    fasur = round (0.65 * terfogat, 2)
    fahengerki.delete (0, END)
    fahengerki.insert (0, str(fasur)+' g' )

foablak = Tk()
gyoker = 'D:\\IKT\\IKT-tk\\'

icon = PhotoImage(file='henger.png')
foablak.iconphoto(True, icon)

foablak.title('Henger')

sugarm = Label(foablak, text='Sugár (cm):')
sugarm.grid (column=1, row=1, sticky= 'e')
sugarbe = Entry(foablak)
sugarbe.grid (column=2, row=1, columnspan=2)


magassagm = Label(foablak, text='Magasság (cm):')
magassagm.grid (column=1, row=2, sticky= 'e')
magssagbe = Entry(foablak)
magssagbe.grid (column=2, row=2, columnspan=2)

terfogatm = Label(foablak, text='Térfogat:')
terfogatm.grid (column=1, row=4, sticky= 'e')
terfogatki = Entry(foablak)
terfogatki.grid (column=2, row=4, columnspan=2)

vashengerm = Label(foablak, text='Vashenger:')
vashengerm.grid (column=1, row=5, sticky= 'e')
vashengerki = Entry(foablak)
vashengerki.grid (column=2, row=5, columnspan=2)

fahengerm = Label(foablak, text='Tölgyfa henger:')
fahengerm.grid (column=1, row=6, sticky= 'e')
fahengerki = Entry(foablak)
fahengerki.grid (column=2, row=6, columnspan=2)



szamitasg = Button(foablak, text='Kiszámít', command=szamitas)
szamitasg.grid (column= 3, row=3, sticky= 'e')



foablak.mainloop()
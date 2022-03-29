from tkinter import *
import math

def szamitas ():
    r = int(sugarbe.get())
    m = int(magssagbe.get())
    borl = int(borbe.get())
    meg = 0
    telitet = 0

    if borl <= 0 or r <= 0 or m <= 0:
        megbeleki.delete (0, END)
        megbeleki.insert (0, 'Nincs értelme a számításnak.' )
        telitetsegki.delete (0,END)
        telitetsegki.insert (0, 'Nincs értelme a számításnak.' )
        terfogatki.delete (0,END)
        terfogatki.insert (0, 'Nincs értelme a számításnak.' )
    else:
    
        terfogat = round (math.pi * r * r * m * 0.001)
        terfogatki.delete (0, END)
        terfogatki.insert (0, str(terfogat)+' l' )

        meg = terfogat - borl
        telitet = round (borl * (100 / terfogat))

        if borl > terfogat:
            megbeleki.delete (0, END)
            megbeleki.insert (0, 'Túl kicsi a hordó.' )
            telitetsegki.delete (0,END)
            telitetsegki.insert (0, 'Túl kicsi a hordó.' )
        else:
            megbeleki.delete (0, END)
            megbeleki.insert (0, str(meg)+' l')
            telitetsegki.delete (0, END)
            telitetsegki.insert (0, str(telitet)+' %')

    
    



foablak = Tk()
gyoker = 'D:\\IKT\\IKT-tk\\'

icon = PhotoImage(file='henger.png')
foablak.iconphoto(True, icon)

foablak.title('Henger')

bor = Label(foablak, text='Bor (l):')
bor.grid (column=1, row=1, sticky= 'e')
borbe = Entry(foablak, width=27)
borbe.grid (column=2, row=1, columnspan=2)

sugarm = Label(foablak, text='Sugár (cm):')
sugarm.grid (column=1, row=2, sticky= 'e')
sugarbe = Entry(foablak, width=27)
sugarbe.grid (column=2, row=2, columnspan=2)

magassagm = Label(foablak, text='Magasság (cm):')
magassagm.grid (column=1, row=3, sticky= 'e')
magssagbe = Entry(foablak, width=27)
magssagbe.grid (column=2, row=3, columnspan=2)


terfogatm = Label(foablak, text='Ennyi literes a hordó:')
terfogatm.grid (column=1, row=5, sticky= 'e')
terfogatki = Entry(foablak, width=27)
terfogatki.grid (column=2, row=5, columnspan=2)

megbelem = Label(foablak, text='Ennyi liter fér még bele:')
megbelem.grid (column=1, row=6, sticky= 'e')
megbeleki = Entry(foablak, width=27)
megbeleki.grid (column=2, row=6, columnspan=2)

telitetsegm = Label(foablak, text='Ennyi százalékig van a hordó:')
telitetsegm.grid (column=1, row=7, sticky= 'e')
telitetsegki = Entry(foablak, width=27)
telitetsegki.grid (column=2, row=7, columnspan=2)



szamitasg = Button(foablak, text='Kiszámít', command=szamitas)
szamitasg.grid (column= 3, row=4, sticky= 'e')



foablak.mainloop()
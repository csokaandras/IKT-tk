from tkinter import *



foablak = Tk()
gyoker = 'D:\\IKT\\IKT-tk\\'

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

fahengerm = Label(foablak, text='Fahenger:')
fahengerm.grid (column=1, row=6, sticky= 'e')
fahengerki = Entry(foablak)
fahengerki.grid (column=2, row=6, columnspan=2)



szamitasg = Button(foablak, text='Kiszámít')
szamitasg.grid (column= 3, row=3, sticky= 'e')


foablak.mainloop()
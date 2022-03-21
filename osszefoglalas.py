from tkinter import *

foablak = Tk()

elsomezo = Label (foablak, text='Első mező:')
elsomezo.grid (column=1, row=1)

masodiksor = Label (foablak, text='Második:')
masodiksor.grid (column=1, row=2)

harmadiksor = Label (foablak, text='Harmadik:')
harmadiksor.grid (column=1, row=3)


elsobe = Entry (foablak)
elsobe.grid (column=2, row=1)

masodikbe = Entry (foablak)
masodikbe.grid (column=2, row=2)

harmadikbe = Entry (foablak)
harmadikbe.grid (column=2, row=3)

can1 = Canvas(foablak,
            width = 160,
            height = 160,
            bg = 'white')
can1.grid (column=3, row=1, rowspan=3)
photo = PhotoImage(file='kiskacsa.png')
photo.subsample(2,2)
item = can1.create_image(80,80,image= photo)

icon = PhotoImage(file='clipart448417.png')
foablak.iconphoto(True, icon)

foablak.mainloop()
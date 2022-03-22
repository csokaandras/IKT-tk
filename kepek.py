from tkinter import *

ablak1 = Tk()
gyoker = 'D:\\IKT\\IKT-tk\\'

def klikk():
    print("Klikkeltem")

ablak1.geometry('450x450')

ablak1.title('Csokl_programol')

icon = PhotoImage(file=gyoker+'clipart448417.png')
ablak1.iconphoto(True, icon)

ablak1.config(background='black')

elsokep = PhotoImage(file=gyoker+'pngfind.com-yoshi-png-998353.png',
                    width=(100),
                    height=(200))
cimke =Label(ablak1,
            text='Helo',
            fg='#152354',
            bg='#812456',
            font=('Arial', 45, 'bold'),
            bd=10,
            relief=RAISED,
            padx=25,
            pady=30,
            #image=elsokep,
            compound='center').pack()

gomb = Button(ablak1,
            text="Kacsints!",
            fg="green",
            bg='red',
            font=('Comis Sans', 35, 'bold'),
            relief=SUNKEN,
            bd=10,
            command=klikk,
            padx=12,
            pady=12,
            #image=gombkep,
            compound="bottom",
            activebackground='green',
            activeforeground='red',
            state=ACTIVE).pack()
ablak1.mainloop()
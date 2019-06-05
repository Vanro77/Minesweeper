from tkinter import *
from Demineur import Cases


def set_n():
    n = int(nombre.get())
    nb_widgets = grille.grid_slaves()
    if len(nb_widgets) != 0:
        for bouton in grille.grid_slaves():
            bouton.destroy()
    b = Cases(grille)
    b.configuration(n, grille)
    b.action(n)


root = Tk()

usage = Label(root, text="Entrer la dimension d'un côté de la grille à déminer", font='courrier', bg='#778899')
usage.pack()

nb = IntVar()
nombre = Entry(root, textvariable=nb)
nombre.pack()

play = Button(root, text='Jouer !', font='courrier', command=set_n)
play.pack()

grille = Frame(root)
grille.config(bg='#778899')

label_title = Label(root, text='A game produced by Vanro inc.', font=('Arial', 8), bg='#778899')
label_title.pack(side=BOTTOM)
root.title('Démineur')
root.geometry('600x600')
root.minsize(600, 600)
grille.pack(expand=1)
root.config(bg='#778899')
root.iconbitmap('Bomb.ico')
root.mainloop()

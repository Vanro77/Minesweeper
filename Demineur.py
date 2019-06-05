import random
from tkinter import messagebox
from tkinter import *


def spliter(a, n):
    chunks = [a[x:x+n] for x in range(0, len(a), n)]
    return chunks


class Grilledejeu:
    def __init__(self, n):
        self.n = n
        self.grille = []
        for indice in range(self.n):
            self.grille.append(list((0,) * self.n))
        for indice_b in range(self.n):
            ra = random.randrange(self.n)
            rb = random.randrange(self.n)
            self.grille[ra][rb] = 'b'
        self.incrementation(self.grille)

    def incrementation(self, grille):
        for a, line in enumerate(grille):
            for b in range(len(line)):
                if grille[a][b] == 'b':
                    if b < self.n - 1:
                        if type(grille[a][b + 1]) is int:
                            grille[a][b + 1] += 1
                    if b > 0:
                        if type(grille[a][b - 1]) is int:
                            grille[a][b - 1] += 1
                    if a > 0:
                        if type(grille[a - 1][b]) is int:
                            grille[a - 1][b] += 1
                        if b > 0:
                            if type(grille[a - 1][b - 1]) is int:
                                grille[a - 1][b - 1] += 1
                        if b < self.n - 1:
                            if type(grille[a - 1][b + 1]) is int:
                                grille[a - 1][b + 1] += 1
                    if a < self.n - 1:
                        if type(grille[a + 1][b]) is int:
                            grille[a + 1][b] += 1
                        if b > 0:
                            if type(grille[a + 1][b - 1]) is int:
                                grille[a + 1][b - 1] += 1
                        if b < self.n - 1:
                            if type(grille[a + 1][b + 1]) is int:
                                grille[a + 1][b + 1] += 1

    def configuration(self, jeu_interface):
        list_buttons = []
        for bouton in jeu_interface:
            list_buttons.append(bouton)
        matrix_buttons = spliter(list_buttons, len(self.grille[0]))
        tupledujeu = []
        for i, j in enumerate(matrix_buttons):
            tupledujeu.append(list(zip(j, self.grille[i])))
        return tupledujeu


class Cases(Button):

    def configuration(self, n, grille):
        self.listbuttons = []
        b_column = 0
        for indice in range(n):
            b_row = 0
            b_column += 1
            bouton = Cases(grille)
            bouton.config(height=1, width=2, bg='#ffcc66')
            bouton.grid(row=0, column=b_column)
            self.listbuttons.append(bouton)
            for indice_1 in range(n - 1):
                b_row += 1
                bouton2 = Cases(grille)
                bouton2.config(height=1, width=2, bg='#ffcc66')
                bouton2.grid(row=b_row, column=b_column)
                self.listbuttons.append(bouton2)

    def action(self, n):
        grille_jeu = Grilledejeu(n)
        tuple_jeu = grille_jeu.configuration(self.listbuttons)
        for a, line in enumerate(tuple_jeu):
            for b in range(len(line)):
                line[b][0].commande(line[b][1])


    def creuser(self, text):
        if self['bg'] == 'green':
            pass
        else:
            self['relief'] = SUNKEN
            self['state'] = DISABLED
            self['text'] = text
            if text != 'b':
                self['bg'] = 'white'
            else:
                self['bg'] = 'red'
                messagebox.showerror('Démineur', 'Vous avez perdu :(')


    def drapeau(self):
        if self['bg'] == 'green':
            self['bg'] = '#ffcc66'
        elif self['bg'] != 'white' or self['bg'] != 'red':
            self['bg'] = 'green'

    def commande(self, text):
        self['command'] = lambda: self.creuser(text)
        self.bind('<Button-3>', lambda event: self.drapeau())

    def victoire(self, n):
        a = Grilledejeu(n)
        tupledujeu = a.configuration(self.listbuttons)



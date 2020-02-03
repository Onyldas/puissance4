from utilitaires import CustomLogging
import os
clear = lambda: os.system('clear') #on Linux System

import numpy as np

logging = CustomLogging()


class Partie:
    grille = []
    is_ended=False

    def __init__(self, m, n, p):
        self.m = 7
        self.n = 7
        self.p = 4
        logging.set_log('Nouvelle partie : ' + str(self.m) + ' de longueur et ' + str(
            self.n) + ' de largeur.\nLes joueurs doivent aligner ' + str(self.p) + ' jetons.')
        self.creer_tableau()

    def creer_tableau(self):
        for i in range(self.n):
            self.grille.append([0] * self.m)  # Ajoute m colonnes

    def afficher_grille(self):
        for i in range(self.n):
            print(self.grille[i])

    def begin_game(self):
        #current_y = self.m - 1
        current_player=False
        current_align_count_player1=1
        current_align_count_player2=1
        while not self.is_ended:
            x=input("Selectionner la colonne:")
            if(not x == ""):
                current_y=self.m-1
                while(self.grille[current_y][int(x)-1]==1 or self.grille[current_y][int(x)-1]==2):
                    current_y-=1
                if (current_y < 1):
                    print("You can't place anymore here")
                else:
                    if(not current_player):
                        self.grille[current_y][int(x)-1]=1
                        print(current_y)
                        self.afficher_grille()
                        if (not (current_y-1) == self.m):
                            print("le x-1 n'est pas egal a 0")
                            current_align_count_player1 = 1

                            #vérification si le pion sur la ligne horizontale juste avant est un pion du joueur courant (player 1)
                            for i in range(0, self.m - 1):
                                # On verifie tous les anciens pions posés sur la ligne horizontale (de la droite vers la gauche)
                                if (i > 0):
                                    if (self.grille[current_y][i] == 1 and self.grille[current_y][i - 1] == 1):
                                        current_align_count_player1 += 1
                            print("current count for player 1 =" + str(current_align_count_player1))
                            if (current_align_count_player1 >= self.p):
                                print("player 1 won the game!")
                                self.is_ended = True
                        current_player=not current_player
                    else:
                        self.grille[current_y][int(x) - 1] = 2
                        print(current_y)
                        self.afficher_grille()
                        if(not current_y-1 ==self.m):
                            print("le x-1 n'est pas egal a 0")
                            current_align_count_player2 = 1
                            #vérification si le pion sur la ligne horizontale juste avant est un pion du joueur courant (player 2)
                            for i in range(0,self.m-1):
                                #On verifie tous les anciens pions posés sur la ligne horizontale (de la droite vers la gauche)
                                if(i>0):
                                    if(self.grille[current_y][i] == 2 and self.grille[current_y][i-1] == 2):
                                        current_align_count_player2+=1
                            print("current count for player 2 ="+str(current_align_count_player2))
                            if(current_align_count_player2 >= self.p):
                                print("player 2 won the game!")
                                self.is_ended = True
                        current_player=not current_player
        else:
            print("you have to enter a number")

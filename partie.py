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
                if(not int(x)>self.m):
                    current_y=self.m-1
                    #On fait tomber le pion au dessus du précédent si jamais un pion est déjà posé sur cette colonne
                    while(self.grille[current_y][int(x)-1]==1 or self.grille[current_y][int(x)-1]==2):
                        current_y-=1
                    if (current_y < 1):
                        print("You can't place anymore here")
                    else:
                        if(not current_player):
                            self.grille[current_y][int(x)-1]=1
                            self.afficher_grille()
                            if (not (current_y-1) == self.m):
                                current_align_count_player1 = 1
                                # vérification des pions successifs sur la ligne horizontale pour le player 2
                                for i in range(0, self.m - 1):
                                    if (i > 0):
                                        if (self.grille[current_y][i] == 1 and self.grille[current_y][i - 1] == 1):
                                            # Si deux pions se suivent, on incrémente le compteur
                                            current_align_count_player1 += 1
                                if (current_align_count_player1 >= self.p):
                                    print("player 1 won the game!")
                                    self.is_ended = True
                                current_align_count_player1 = 1
                                # vérification des pions successifs sur la ligne verticale pour le player 2
                                for i in range(0, self.n):
                                    if (i > 0):
                                        if (self.grille[i][int(x) - 1] == 1 and self.grille[i - 1][int(x) - 1] == 1):
                                            # Si deux pions se suivent, on incrémente le compteur
                                            current_align_count_player1 += 1
                                if (current_align_count_player1 >= self.p):
                                    print("player 1 won the game!")
                                    self.is_ended = True
                            current_player = not current_player
                        else:
                            self.grille[current_y][int(x) - 1] = 2
                            self.afficher_grille()
                            if(not current_y-1 ==self.m):
                                current_align_count_player2 = 1
                                # vérification des pions successifs sur la ligne horizontale pour le player 2
                                for i in range(0,self.m-1):
                                    if(i>0):
                                        if(self.grille[current_y][i] == 2 and self.grille[current_y][i-1] == 2):
                                            #Si deux pions se suivent, on incrémente le compteur
                                            current_align_count_player2+=1
                                if(current_align_count_player2 >= self.p):
                                    print("player 2 won the game!")
                                    self.is_ended = True
                                current_align_count_player2 = 1
                                # vérification des pions successifs sur la ligne verticale pour le player 2
                                for i in range(0,self.n):
                                    if (i > 0):
                                        if (self.grille[i][int(x)-1] == 2 and self.grille[i-1][int(x)-1] == 2):
                                            #Si deux pions se suivent, on incrémente le compteur
                                            current_align_count_player2 += 1
                                if (current_align_count_player2 >= self.p):
                                    print("player 2 won the game!")
                                    self.is_ended = True
                            current_player=not current_player
        else:
            print("you have to enter a number")

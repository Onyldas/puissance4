from utilitaires import CustomLogging
from ia.minimax import Minimax

import random

logging = CustomLogging()


class Partie:
    grille = []
    is_ended = False

    def __init__(self, m, n, p):
        self.m = 6  # colonnes x
        self.n = 7  # lignes y
        self.p = 4  # nombres de pions à aligner pour gagner avec p < (min(m,n) - 1)
        logging.set_log('Nouvelle partie : ' + str(self.m) + ' de longueur et ' + str(
            self.n) + ' de largeur.\nLes joueurs doivent aligner ' + str(self.p) + ' jetons.')
        self.creer_tableau()

    def creer_tableau(self):
        for i in range(self.n):
            self.grille.append([0] * self.m)  # Ajoute m colonnes

    def afficher_grille(self):
        for i in range(self.n):
            print(self.grille[i])

    def get_diagonal_gd(self, x, y):
        diag = []
        for j in range(self.n):
            for i in range(self.m):
                for k in range(-min(x, y), max(self.n, self.m) - max(x, y)):
                    if i == x + k and j == y + k:
                        diag.append(self.grille[j][i])
        return diag

    def get_diagonal_dg(self, x, y):
        diag2 = []
        for j2 in range(self.n):
            for i2 in range(self.m):
                for k2 in range(-min(x + self.m - 1, y), max(self.n, self.m) - max(x - self.m - 1, y)):
                    if self.m - 1 - i2 == self.m + 1 - x + k2 and j2 == y + k2:
                        diag2.append(self.grille[j2][i2])
        return diag2

    def find_y(self, choosen_column):
        current_y = self.n - 1
        # On fait tomber le pion au dessus du précédent si jamais un pion est déjà posé sur cette colonne
        while self.grille[current_y][int(choosen_column) - 1] == 1 or self.grille[current_y][
            int(choosen_column) - 1] == 2:
            current_y -= 1
            if current_y < 0:
                print("You can't place anymore here")
                break

    def combo_for_user(self, current_y, player, x):
        # Si on est player 1, on met un 1 dans le tableau ou le pion tombera
        if player == 1:
            self.grille[current_y][int(x) - 1] = 1
        # Si on est player 2, on met un 2 dans le tableau ou le pion tombera
        else:
            self.grille[current_y][int(x) - 1] = 2

    def check_victory(self, current_y, player, x):
        # Vérification des pions successifs sur la ligne horizontale
        current_align_count = 1
        for i in range(1, self.m):
            if self.grille[current_y][i] == player and self.grille[current_y][i - 1] == player:
                # Si deux pions se suivent, on incrémente le compteur
                current_align_count += 1
                if current_align_count >= self.p:
                    print("Player " + str(player) + " won the game! - horizontal")
                    return True
            else:
                current_align_count = 1

        # Vérification des pions successifs sur la ligne verticale
        current_align_count = 1
        for j in range(1, self.n):
            if self.grille[j][int(x) - 1] == player and self.grille[j - 1][int(x) - 1] == player:
                # Si deux pions se suivent, on incrémente le compteur
                current_align_count += 1
                if current_align_count >= self.p:
                    print("Player " + str(player) + " won the game! - vertical")
                    return True
            else:
                current_align_count = 1

        # Vérification des pions successifs sur la diagonale hautgauche vers basdroite
        current_align_count = 1
        diag = self.get_diagonal_gd(int(x), current_y + 1)  # on récupère la première diagonale
        for i in range(1, len(diag)):
            if diag[i] == player and diag[i - 1] == player:
                # Si deux pions se suivent sur la diagonale, on incrémente le compteur
                current_align_count += 1
                if current_align_count >= self.p:
                    print("Player " + str(player) + " won the game! - diagonal_gd")
                    return True
            else:  # si les pions ne se suivent pas, on remet le compteur à 1
                current_align_count = 1

        # Vérification des pions successifs sur la diagonale hautdroite vers basgauche
        current_align_count = 1
        diag2 = self.get_diagonal_dg(int(x) + 1, current_y)  # on récupère la deuxième diagonale
        for i in range(1, len(diag2)):
            if diag2[i] == player and diag2[i - 1] == player:
                # Si deux pions se suivent sur la diagonale, on incrémente le compteur
                current_align_count += 1
                if current_align_count >= self.p:
                    print("Player " + str(player) + " won the game! - diagonal_dg")
                    return True
            else:  # si les pions ne se suivent pas, on remet le compteur à 1
                current_align_count = 1

    def begin_game(self):
        selected_game = input("Select game : 1- Joueur vs Joueur || 2- Joeur vs Dumb IA || 3 - incoming...")
        if int(selected_game) == 1:
            current_player = 1
            while not self.is_ended:

                choosen_column = input("Selectionner la colonne:")
                if (not choosen_column == "") and (not int(choosen_column) > self.m):
                    current_y = self.n - 1
                    # On fait tomber le pion au dessus du précédent si jamais un pion est déjà posé sur cette colonne
                    while self.grille[current_y][int(choosen_column) - 1] == 1 or self.grille[current_y][
                        int(choosen_column) - 1] == 2:
                        current_y -= 1
                        if current_y < 0:
                            print("You can't place anymore here")
                            break

                    if current_y >= 0:
                        # On place le pion
                        self.combo_for_user(current_y, current_player, choosen_column)
                        # On affiche la grille
                        self.afficher_grille()
                        # On check si le joueur a gagné
                        self.is_ended = self.check_victory(current_y, current_player, choosen_column)
                        # On change de joueur
                        if current_player == 1:
                            current_player = 2
                        else:
                            current_player = 1
                else:
                    print("you have to enter a number")
        if int(selected_game) == 2:
            current_player = 1
            while not self.is_ended:
                if current_player == 1:
                    choosen_column = input("Selectionner la colonne:")
                    if (not choosen_column == "") and (not int(choosen_column) > self.m):
                        if not int(choosen_column) > self.m:
                            current_y = self.n - 1
                            # On fait tomber le pion au dessus du précédent si jamais un pion est déjà posé sur cette colonne
                            while self.grille[current_y][int(choosen_column) - 1] == 1 or self.grille[current_y][
                                int(choosen_column) - 1] == 2:
                                current_y -= 1
                            if current_y < 1:
                                print("You can't place anymore here")
                            else:
                                self.combo_for_user(current_y, 1, choosen_column)
                                current_player = 2
                            cls = lambda: print('\n' * 100)
                            cls()
                    else:
                        print("you have to enter a number")
                else:
                    choosen_column = random.randint(1, self.n)
                    if (not choosen_column == "") and (not int(choosen_column) > self.m):
                        current_y = self.n - 1
                        # On fait tomber le pion au dessus du précédent si jamais un πon est déjà posé sur cette colonne
                        while self.grille[current_y][int(choosen_column) - 1] == 1 or self.grille[current_y][
                            int(choosen_column) - 1] == 2:
                            current_y -= 1
                        if current_y < 1:
                            print("You can't place anymore here")
                        else:
                            print("Dumb ia is playing")
                            self.combo_for_user(current_y, 2, choosen_column)
                            current_player = 1
                    else:
                        print("you have to enter a number")
        if int(selected_game) == 3:
            ai = Minimax(self)
            ai.minmax()

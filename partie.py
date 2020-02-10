from utilitaires import CustomLogging

import random

logging = CustomLogging()


class Partie:
    grille = []
    is_ended = False

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

    def combo_for_user(self, current_y, player, x):
        # Si on est player 1, on met un 1 dans le tableau ou le pion tombera
        if player == 1:
            self.grille[current_y][int(x) - 1] = 1
        # Si on est player 2, on met un 2 dans le tableau ou le pion tombera
        else:
            self.grille[current_y][int(x) - 1] = 2

    def check_victory(self, current_y, player, x):
        current_align_count = 1
        # vérification des pions successifs sur la ligne horizontale
        for i in range(1, self.m - 1):
            if self.grille[current_y][i] == player and self.grille[current_y][i - 1] == player:
                # Si deux pions se suivent, on incrémente le compteur
                current_align_count += 1
        if current_align_count >= self.p:
            print("player " + str(player) + " won the game!")
            return True
        current_align_count = 1
        # vérification des pions successifs sur la ligne verticale
        for i in range(1, self.n):
            if self.grille[i][int(x) - 1] == player and self.grille[i - 1][int(x) - 1] == player:
                # Si deux pions se suivent, on incrémente le compteur
                current_align_count += 1
        if current_align_count >= self.p:
            print("player " + str(player) + " won the game!")
            return True

    def begin_game(self):
        selected_game = input("Select game : 1- Joueur vs Joueur || 2- Joeur vs Dumb IA || 3 - incoming...")
        if int(selected_game) == 1:
            current_player = 1
            while not self.is_ended:

                choosen_column = input("Selectionner la colonne:")
                if (not choosen_column == "") and (not int(choosen_column) > self.m):
                    current_y = self.m - 1
                    # On fait tomber le pion au dessus du précédent si jamais un pion est déjà posé sur cette colonne
                    while self.grille[current_y][int(choosen_column) - 1] == 1 or self.grille[current_y][
                        int(choosen_column) - 1] == 2:
                        current_y -= 1
                    if current_y < 1:
                        print("You can't place anymore here")
                    else:
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
                            current_y = self.m - 1
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
                    choosen_column = random.randint(1, self.n)
                    if (not choosen_column == "") and (not int(choosen_column) > self.m):
                        current_y = self.m - 1
                        # On fait tomber le pion au dessus du précédent si jamais un pion est déjà posé sur cette colonne
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

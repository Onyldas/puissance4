from utilitaires import CustomLogging

import random

logging = CustomLogging()


class Minimax:

    def __init__(self):
        self.coupsdavance = 3

    def play(self, player, partie):
        total = [0] * partie.m
        for i in range(self.coupsdavance):
            if player == 1:
                total -= self.minmax(partie, player)
            else:
                total += self.minmax(partie, player)

    def minmax(self, partie, player):
        points = [0] * partie.m  # on crée une liste de la même taille que la grille (colonnes)
        for x in range(partie.m):
            y = self.find_y(partie, partie.n - 1, x)
            partie.combo_for_user(y, player, x)
            if partie.check_victory:
                points[x] += 1
        return points

    def best_choice(self, liste):
        best = 0
        for i in range(1, len(liste)):
            if liste[i - 1] < liste[i]:
                best = i
        return best

    def find_y(self, partie, current_y, choosen_column):
        while (partie.grille[current_y][int(choosen_column) - 1] != 0) and (current_y >= 0):
            current_y -= 1
        return current_y

from utilitaires import CustomLogging
import numpy as np

logging = CustomLogging()


class Partie:
    grille = []
  #  is_ended=false
    def __init__(self, m, n, p):
        self.m = 7
        self.n = 6
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


  #  def begin_game(self):
 #       while is_ended
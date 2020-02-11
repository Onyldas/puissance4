from flask import Flask, render_template
from partie import Partie

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title='Puissance 4')


if __name__ == "__main__":
    # app.run()
    game = Partie(15, 14, 8)
    game.begin_game()

    # TESTS RECUPERATION DIAGONALES
    # test_grille = []
    # c = 10
    # for i in range(7):  # n
    #     test_grille.append([c + 1, c + 2, c + 3, c + 4, c + 5, c + 6])  # m
    #     c += 10
    #
    #
    # def afficher_grille(grille):
    #     for e in range(7):
    #         print(grille[e])
    #
    #
    # afficher_grille(test_grille)
    # diag = []
    # y = 6
    # x = 5
    # for j in range(7):
    #     for i in range(6):
    #         for k in range(-min(x, y), 7 - max(x, y)):
    #             if i == x + k and j == y + k:
    #                 diag.append(test_grille[j][i])
    #
    # print()
    # print(diag)
    #
    # diag2 = []
    # for j2 in range(7):
    #     for i2 in range(6):
    #         for k2 in range(-min(x+6, y), 7 - max(x-6, y)):
    #             if 6 - i2 == 8 - x + k2 and j2 == y + k2:
    #                 diag2.append(test_grille[j2][i2])
    #
    # print()
    # print(diag2)

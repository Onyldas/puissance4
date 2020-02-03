from flask import Flask, render_template
from partie import Partie

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html',title='Puissance 4')

if __name__ == "__main__":
    app.run()
    game = Partie(15, 14, 8)
    game.afficher_grille()

from flask import *
from src.creature import Creature


app = Flask(__name__)
app.secret_key = "andithoughtmyjokeswerebad"


@app.route("/submit", methods=["POST"])
def instantiate():
    card_id = session["cards"]
    session["cards"] += 1
    data = request.form.get("data")
    return render_template("creature.html", creature=Creature(data, 15, card_id))


@app.route("/getBestiary", methods=["GET"])
def getBestiary():

    result = {"data": list(Creature.get_bestiary().keys())}
    return jsonify(result)


@app.route("/")
def index():
    session["cards"] = 0
    return render_template("index.html")


if __name__ == "__main__":
    print("Launching on http://localhost:5000")
    app.run(debug=True)

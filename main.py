from flask import *
from random import randint

bestiairy = {
    "Goblin":{
      "STR":12,
      "STR_std":[-1, 3],
      "DEX":11,
      "DEX_std":[0, 4],
      "CON":10,
      "CON_std":[-2,2],
      "INT":9,
      "INT_std":[-3,1],
      "WIS":9,
      "WIS_std":[-2,2],
      "CHA":10,
      "CHA_std":[-4,0],
      "AC":11,
      "Base_Hp":10,
      "Hp_Dices":[1,4]
    }
}

class Creature:

    calculate_skill_base = lambda name,skill : bestiairy[name][skill] + randint(bestiairy[name][skill + "_std"][0],bestiairy[name][skill + "_std"][1])
    calculate_ac = lambda base_ac, dex : (base_ac + dex - 10)//10
    calculate_mhp = lambda base_hp, level, con, hp_dices : base_hp + (level//4) * ((con - 10) // 2) + randint(hp_dices[0], (level - 1) * hp_dices[1] * hp_dices[0])
    def skill_add_pts(self, skill, n=1):
        self.json_data[skill]["Value"] += n

    def get_value(self, key):
        return self.json_data[key]["Value"]
    
    def get_bestiary_data(self,key):
        return bestiairy[self.get_value("NAM")][key]

    def __init__(self, name, level):
        
        self.json_data = {
            "NAM" : {"Value":name, "Immuable":True},
            "STR" : {"Value": Creature.calculate_skill_base(name, "STR"), "Immuable":False},
            "DEX" : {"Value": Creature.calculate_skill_base(name, "DEX"), "Immuable":False},
            "CON" :{"Value": Creature.calculate_skill_base(name, "CON"), "Immuable":False},
            "INT" : {"Value": Creature.calculate_skill_base(name, "INT"), "Immuable":False},
            "WIS" : {"Value": Creature.calculate_skill_base(name, "WIS"), "Immuable":False},
            "CHA" : {"Value": Creature.calculate_skill_base(name, "CHA"), "Immuable":False}
        }

        points = (level // 4)*2

        while points > 0:
            d = randint(1,6)
            if d == 1:
                self.skill_add_pts("STR")
            elif d == 2:
                self.skill_add_pts("DEX")
            elif d == 3:
                self.skill_add_pts("CON")
            elif d == 4:
                self.skill_add_pts("INT")
            elif d == 5:
                self.skill_add_pts("WIS")
            else:
                self.skill_add_pts("CHA")
            points -= 1


        
        self.json_data["AC"] = {"Value": Creature.calculate_ac(self.get_bestiary_data("AC"), self.get_value("DEX")), "Immuable":False}
        self.json_data["MHP"] = {"Value": Creature.calculate_mhp(self.get_bestiary_data("Base_Hp"), level, \
                                                                  self.get_value("CON"), self.get_bestiary_data("Hp_Dices")), "Immuable":False}
        self.json_data["HP"] = {"Value": self.get_value("MHP"), "Immuable":False}

    def __str__(self):

        return self.json_data
    
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def monster():
    data = request.form.get('data')
    c = Creature(data, 15)
    return jsonify(c.__str__())


@app.route('/')
def index():
    return render_template('index.html')

# http://localhost:5000

if __name__ == '__main__':
    app.run(debug=True)

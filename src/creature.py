import os
import json
from random import randint


class Creature:
    bestiary = None


    @staticmethod
    def get_bestiary():
        if Creature.bestiary is None:
            with open(
                os.path.join(os.getcwd(), "static", "bestiary.json"), "r"
            ) as file:
                Creature.bestiary = json.load(file)

        return Creature.bestiary


    @staticmethod
    def calculate_skill_base(name, skill):
        bestiary = Creature.get_bestiary()
        return bestiary[name][skill] + randint(
            bestiary[name][skill + "_std"][0],
            bestiary[name][skill + "_std"][1],
        )


    @staticmethod
    def calculate_ac(base_ac, dex):
        return base_ac + (dex - 10) // 2


    @staticmethod
    def calculate_mhp(base_hp, level, con, hp_dices):
        return (
            base_hp
            + (level // 4) * ((con - 10) // 2)
            + randint(hp_dices[0], (level - 1) * hp_dices[1] * hp_dices[0])
        )


    def skill_add_pts(self, skill, n=1):
        self.json_data[skill]["Value"] += n


    def get_value(self, key):
        return self.json_data[key]["Value"]


    def get_bestiary_data(self, key):
        return self.bestiary[self.get_value("NAM")][key]


    def __init__(self, name, level, card_id):
        self.bestiary = Creature.get_bestiary()

        self.card_id = card_id

        self.json_data = {
            "NAM": {"Value": name, "Immuable": True},
            "STR": {
                "Value": Creature.calculate_skill_base(name, "STR"),
                "Immuable": False,
            },
            "DEX": {
                "Value": Creature.calculate_skill_base(name, "DEX"),
                "Immuable": False,
            },
            "CON": {
                "Value": Creature.calculate_skill_base(name, "CON"),
                "Immuable": False,
            },
            "INT": {
                "Value": Creature.calculate_skill_base(name, "INT"),
                "Immuable": False,
            },
            "WIS": {
                "Value": Creature.calculate_skill_base(name, "WIS"),
                "Immuable": False,
            },
            "CHA": {
                "Value": Creature.calculate_skill_base(name, "CHA"),
                "Immuable": False,
            },
        }

        points = (level // 4) * 2

        while points > 0:
            d = randint(1, 6)
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

        self.json_data["AC"] = {
            "Value": Creature.calculate_ac(
                self.get_bestiary_data("AC"), self.get_value("DEX")
            ),
            "Immuable": False,
        }

        self.json_data["MHP"] = {
            "Value": Creature.calculate_mhp(
                self.get_bestiary_data("Base_Hp"),
                level,
                self.get_value("CON"),
                self.get_bestiary_data("Hp_Dices"),
            ),
            "Immuable": False,
        }

        self.json_data["HP"] = {"Value": self.get_value("MHP"), "Immuable": False}

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
        return randint(
            bestiary[name][skill]['min'],
            bestiary[name][skill]['max'],
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

    def get_bestiary_data(self, key):
        return self.bestiary[self.name][key]

    def __init__(self, name, level, card_id):
        self.bestiary = Creature.get_bestiary()

        self.card_id = card_id
        self.name = name
        self.strength = Creature.calculate_skill_base(name, "strength")
        self.dexterity = Creature.calculate_skill_base(name, "dexterity")
        self.constitution = Creature.calculate_skill_base(name, "constitution")
        self.intelligence = Creature.calculate_skill_base(name, "intelligence")
        self.wisdom = Creature.calculate_skill_base(name, "wisdom")
        self.charisma = Creature.calculate_skill_base(name, "charisma")
        self.armor_class = Creature.calculate_ac(
            self.get_bestiary_data("armor_class"), self.dexterity
        )
        self.current_health_point = self.max_health_point = Creature.calculate_mhp(
            self.get_bestiary_data("max_health_point"),
            level,
            self.constitution,
            self.get_bestiary_data("hp_dices"),
        )

        points = (level // 4) * 2

        while points > 0:
            d = randint(1, 6)
            if d == 1:
                self.strength += 1
            elif d == 2:
                self.dexterity += 1
            elif d == 3:
                self.constitution += 1
            elif d == 4:
                self.intelligence += 1
            elif d == 5:
                self.wisdom += 1
            else:
                self.charisma += 1
            points -= 1

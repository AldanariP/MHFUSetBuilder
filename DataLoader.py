from json import load

from ArmorPiece import ArmorPiece
from Jewel import Jewel
from Skill import Skill


class DataLoader:

    def __init__(self):
        self.__armorData = {}
        with open("armorpiece.json", 'r') as file:
            data = load(file)
        for piece_name, piece_data in data.items():
            self.__armorData[piece_name] = ArmorPiece(piece_data)

        self.__jewelData = {}
        with open("jewel.json", 'r') as file:
            data = load(file)
        for jewel_name, jewel_data in data.items():
            self.__jewelData[jewel_name] = Jewel(jewel_data)

        self.__skillData = {}
        with open("skill.json", 'r') as file:
            data = load(file)
        for skill_name, skill_data in data.items():
            self.__jewelData[skill_name] = Skill(skill_data)

    def getArmorData(self, name) -> ArmorPiece:
        return self.__armorData[name]

    def getJewelData(self, name) -> Jewel:
        return self.__jewelData[name]

    def getSkillData(self, name) -> Skill:
        return self.__skillData[name]

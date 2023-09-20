from ArmorClass import ArmorClass
from Gender import Gender
from Parts import Part
from Rarity import Rarity
from Jewel import Jewel
from collections import defaultdict


class ArmorPiece:

    def __init__(self, name, data):
        try:
            piece = data[name]
            self.__name = piece['name']
            self.__rarity = Rarity(piece['rarity']).rarity()
            self.__part = Part(piece['part'])
            self.__armor_class = ArmorClass(piece['class'])
            self.__gender = Gender(piece['gender'])
            self.__defense = piece['defense']
            self.__fireRes = piece['fireRes']
            self.__waterRes = piece['waterRes']
            self.__thunderRes = piece['thunderRes']
            self.__iceRes = piece['iceRes']
            self.__dragonRes = piece['dragonRes']
            self.__nbSlots = piece['nbSlots']
            self.__freeSlots = self.__nbSlots
            self.__jewels = []
            self.__skills = defaultdict(int)
            self.__skills.update(piece['skills'])
            self.__cost = piece['cost']
            self.__materials = piece['materials']
        except KeyError as _:
            print(f"Error: '{name}' is not a valid armor piece name.")

    def name(self) -> str:
        return self.__name

    def rarity(self) -> int:
        return self.__rarity

    def part(self) -> Part:
        return self.__part

    def defense(self) -> int:
        return self.__defense

    def fireRes(self) -> int:
        return self.__fireRes

    def waterRes(self) -> int:
        return self.__waterRes

    def thunderRes(self) -> int:
        return self.__thunderRes

    def iceRes(self) -> int:
        return self.__iceRes

    def dragonRes(self) -> int:
        return self.__dragonRes

    def nbSolt(self) -> int:
        return self.__nbSlots

    def freeSlot(self) -> int:
        return self.__freeSlots

    def jewels(self) -> list[Jewel]:
        return self.__jewels

    def skills(self) -> dict[str, int]:
        return self.__skills

    def armor_class(self) -> ArmorClass:
        return self.__armor_class

    def gender(self) -> Gender:
        return self.__gender

    def cost(self) -> int:
        return self.__cost

    def materials(self) -> dict[str, int]:
        return self.__materials

    def isHead(self) -> bool:
        return self.__part == Part.HEAD

    def isTorso(self) -> bool:
        return self.__part == Part.TORSO

    def isArm(self) -> bool:
        return self.__part == Part.ARM

    def isWaist(self) -> bool:
        return self.__part == Part.WAIST

    def isLeg(self) -> bool:
        return self.__part == Part.LEG

    def rank(self) -> str:
        if self.__rarity <= 3:
            return "low"
        elif self.__rarity <= 8:
            return "high"
        else:
            return "G"

    def getSkillAmount(self, skill) -> int | None:
        return self.__skills.get(skill)

    def attachJewel(self, jewel: Jewel) -> bool:
        if jewel.slots() <= self.__freeSlots:
            for skill, amount in jewel.skills().items():
                self.__skills[skill] += amount
            self.__jewels.append(jewel)
            self.__freeSlots -= jewel.slots()
            return True
        else:
            return False

    def detachJewel(self, jewel: Jewel) -> bool:
        jSkill = jewel.skills()
        if jewel.name() in [j.name() for j in self.__jewels]:
            for skill, amount in jSkill.items():
                if self.__skills.get(skill, 0) > jSkill.get(skill, 0):
                    self.__skills[skill] -= jSkill.get(skill, 0)
                else:
                    self.__skills.pop(skill, None)
            self.__jewels.remove(jewel)
            self.__freeSlots += jewel.slots()
            return True
        else:
            return False

    def __str__(self) -> str:
        result = (
            f"Name               : {self.__name}\n"
            f"Rarity             : {self.__rarity}\n"
            f"Class              : {self.__armor_class.value}\n"
            f"Gender             : {self.__gender.value}\n"
            f"Defense            : {self.__defense}\n"
            f"Fire Resistance    : {self.__fireRes}\n"
            f"Water Resistance   : {self.__waterRes}\n"
            f"Thunder Resistance : {self.__thunderRes}\n"
            f"Ice Resistance     : {self.__iceRes}\n"
            f"Dragon Restistance : {self.__dragonRes}\n"
            f"Base Slots         : {self.__nbSlots}\n"
            f"Slots Available    : {self.__freeSlots}\n"
            f"Cost               : {self.__cost}z\n"
            f"Skills :\n"
        )
        max_key_width = max(len(i) for i in self.__skills.keys())

        for skill, value in self.__skills.items():
            if value >= 0:
                key = f"{skill}".ljust(max_key_width)
                result += f"    {key} :  {value}\n"
            else:
                key = f"{skill}".ljust(max_key_width)
                result += f"    {key} : {value}\n"

        max_key_width = max(len(i) for i in self.__materials.keys())

        result += f"Material :\n"
        for material, value in self.__materials.items():
            key = f"{material}".ljust(max_key_width)
            result += f"    {key} : {value}\n"

        if self.__jewels:
            result += f"Jewel :\n"
            for jewel in self.__jewels:
                result += f"   -{jewel.name()} : {jewel.skills()}"

        return result

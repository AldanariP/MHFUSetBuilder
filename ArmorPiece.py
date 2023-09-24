from ArmorClass import ArmorClass
from Gender import Gender
from Parts import Part
from Rarity import Rarity
from Jewel import Jewel
from collections import defaultdict


class ArmorPiece:

    def __init__(self, data):
        self.name = data['name']
        self.rarity = Rarity(data['rarity']).rarity
        self.part = Part(data['part'])
        self.armorClass = ArmorClass(data['class'])
        self.gender = Gender(data['gender'])
        self.defense = data['defense']
        self.fireRes = data['fireRes']
        self.waterRes = data['waterRes']
        self.thunderRes = data['thunderRes']
        self.iceRes = data['iceRes']
        self.dragonRes = data['dragonRes']
        self.nbSlots = data['nbSlots']
        self.freeSlots = self.nbSlots
        self.jewels = []
        self.skills = defaultdict(int)
        self.skills.update(data['skills'])
        self.cost = data['cost']
        self.materials = data['materials']

    def isHead(self) -> bool:
        return self.part == Part.HEAD

    def isTorso(self) -> bool:
        return self.part == Part.TORSO

    def isArm(self) -> bool:
        return self.part == Part.ARM

    def isWaist(self) -> bool:
        return self.part == Part.WAIST

    def isLeg(self) -> bool:
        return self.part == Part.LEG

    def rank(self) -> str:
        if self.rarity <= 3:
            return "low"
        elif self.rarity <= 8:
            return "high"
        else:
            return "G"

    def getSkillAmount(self, skill: str) -> int | None:
        return self.skills.get(skill)

    def attachJewel(self, jewel: Jewel) -> bool:
        if jewel.slots <= self.freeSlots:
            for skill, amount in jewel.skills.items():
                self.skills[skill] += amount
            self.jewels.append(jewel)
            self.freeSlots -= jewel.slots
            return True
        else:
            return False

    def detachJewel(self, jewel: Jewel) -> bool:
        jSkill = jewel.skills
        if jewel.name in [j.name for j in self.jewels]:
            for skill, amount in jSkill.items():
                if self.skills.get(skill, 0) > jSkill.get(skill, 0):
                    self.skills[skill] -= jSkill.get(skill, 0)
                else:
                    self.skills.pop(skill, None)
            self.jewels.remove(jewel)
            self.freeSlots += jewel.slots
            return True
        else:
            return False

    def __str__(self) -> str:
        result = (
            f"Name               : {self.name}\n"
            f"Rarity             : {self.rarity}\n"
            f"Class              : {self.armorClass.value}\n"
            f"Gender             : {self.gender.value}\n"
            f"Defense            : {self.defense}\n"
            f"Fire Resistance    : {self.fireRes}\n"
            f"Water Resistance   : {self.waterRes}\n"
            f"Thunder Resistance : {self.thunderRes}\n"
            f"Ice Resistance     : {self.iceRes}\n"
            f"Dragon Restistance : {self.dragonRes}\n"
            f"Base Slots         : {self.nbSlots}\n"
            f"Slots Available    : {self.freeSlots}\n"
            f"Cost               : {self.cost}z\n"
            f"Skills :\n"
        )
        max_key_width = max(len(i) for i in self.skills.keys())

        for skill, value in self.skills.items():
            key = f"{skill}".ljust(max_key_width)
            if value >= 0:
                result += f"    {key} :  {value}\n"
            else:
                result += f"    {key} : {value}\n"

        max_key_width = max(len(i) for i in self.materials.keys())

        result += f"Material :\n"
        for material, value in self.materials.items():
            key = f"{material}".ljust(max_key_width)
            result += f"    {key} : {value}\n"

        if self.jewels:
            result += f"Jewel :\n"
            for jewel in self.jewels:
                result += f"   -{jewel.name} : {jewel.skills}"

        return result

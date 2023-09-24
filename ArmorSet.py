from ArmorClass import ArmorClass
from ArmorPiece import ArmorPiece
from Jewel import Jewel
from Parts import *
from Gender import *
from typing import Optional
from collections import Counter, defaultdict

from Skill import Skill


def genderWaring(armorPiece, armorSet):
    return (f"ArmorPiece '{armorPiece.name}' of gender '{armorPiece.gender.value}' "
            f"is not compatible with the set gender '{armorSet.setGender}'")


def classWaring(armorPiece, armorSet):
    return (f"ArmorPiece '{armorPiece.name}' class '{armorPiece.part.value}' "
            f"is not compatible with the set class : '{armorSet.setClass}'")


class ArmorSet:
    def __init__(self):
        self.armorSet: dict[str, ArmorPiece] = {"Head": Optional[ArmorPiece],
                                                "Torso": Optional[ArmorPiece],
                                                "Arm": Optional[ArmorPiece],
                                                "Waist": Optional[ArmorPiece],
                                                "Leg": Optional[ArmorPiece]}
        self.setClass: ArmorClass = Optional[ArmorClass]
        self.setGender: Gender = Optional[Gender]
        self.weaponSlot: int = 0
        self.freeWeaponSlot: int = 0
        self.weaponSkill: dict[str, int] = {}
        self.weaponJewels: list[Jewel] = []

    def pieces(self):
        return self.armorSet

    def setHead(self, headPiece: ArmorPiece):
        if headPiece.part != Part.HEAD:
            raise ValueError(f"ArmorPiece '{headPiece.name}' is not a Head Piece")

        elif self.setGender is not Optional[Gender] and (
                headPiece.gender != self.setGender or headPiece.gender != Gender.BOTH):
            raise ValueError(genderWaring(headPiece, self))

        else:
            self.setGender = headPiece.gender
            self.armorSet["Head"] = headPiece

    def setTorso(self, torsoPiece: ArmorPiece):
        if torsoPiece.part != Part.TORSO:
            raise ValueError(f"ArmorPiece '{torsoPiece.name}' is not a Torso Piece")

        elif self.setClass is not Optional[ArmorClass] and torsoPiece.armorClass != self.setClass:
            raise ValueError(classWaring(torsoPiece, self))

        elif self.setGender is not Optional[Gender] and (
                torsoPiece.gender != self.setGender or torsoPiece.gender != Gender.BOTH):
            raise ValueError(genderWaring(torsoPiece, self))

        else:
            self.setClass = torsoPiece.armorClass
            self.setGender = torsoPiece.gender
            self.armorSet["Torso"] = torsoPiece

    def setArm(self, armPiece: ArmorPiece):
        if armPiece.part != Part.ARM:
            raise ValueError(f"ArmorPiece '{armPiece.name}' is not an Arm Piece")

        elif self.setClass is not Optional[ArmorClass] and armPiece.armorClass != self.setClass:
            raise ValueError(classWaring(armPiece, self))

        elif self.setGender is not Optional[Gender] and (
                armPiece.gender != self.setGender or armPiece.gender != Gender.BOTH):
            raise ValueError(genderWaring(armPiece, self))

        else:
            self.setClass = armPiece.armorClass
            self.setGender = armPiece.gender
            self.armorSet["Arm"] = armPiece

    def setWaist(self, waistPiece: ArmorPiece):
        if waistPiece.part != Part.WAIST:
            raise ValueError(f"ArmorPiece '{waistPiece.name}' is not a Waist Piece")

        elif self.setClass is not Optional[ArmorClass] and waistPiece.armorClass != self.setClass:
            raise ValueError(classWaring(waistPiece, self))

        elif self.setGender is not Optional[Gender] and (
                waistPiece.gender != self.setGender or waistPiece.gender != Gender.BOTH):
            raise ValueError(genderWaring(waistPiece, self))

        else:
            self.setClass = waistPiece.armorClass
            self.setGender = waistPiece.gender
            self.armorSet["Waist"] = waistPiece

    def setLeg(self, legPiece: ArmorPiece):
        if legPiece.part != Part.LEG:
            raise ValueError(f"ArmorPiece '{legPiece.name}' is not a Leg Piece")

        elif self.setClass is not Optional[ArmorClass] and legPiece.armorClass != self.setClass:
            raise ValueError(classWaring(legPiece, self))

        elif self.setGender is not Optional[Gender] and (
                legPiece.gender != self.setGender or legPiece.gender != Gender.BOTH):
            raise ValueError(genderWaring(legPiece, self))

        else:
            self.setClass = legPiece.armorClass
            self.setGender = legPiece.gender
            self.armorSet["Leg"] = legPiece

    def setAllPieces(self, ArmorPieceList: list[ArmorPiece]):
        if Counter(i.armorClass for i in ArmorPieceList) != \
                {Part.HEAD: 1, Part.TORSO: 1, Part.ARM: 1, Part.WAIST: 1, Part.LEG: 1}:
            raise ValueError("Armor Piece list provided is not valid")

        for i in ArmorPieceList:
            if i.armorClass == Part.HEAD:
                self.setHead(i)
            if i.armorClass == Part.TORSO:
                self.setTorso(i)
            if i.armorClass == Part.ARM:
                self.setArm(i)
            if i.armorClass == Part.WAIST:
                self.setWaist(i)
            if i.armorClass == Part.LEG:
                self.setLeg(i)

    def setWeaponSlot(self, amount: int):
        self.weaponSlot, self.freeWeaponSlot = amount, amount

    def attachJeweltoWeapon(self, jewel: Jewel) -> bool:
        if jewel.slots <= self.freeWeaponSlot:
            for skill, amount in jewel.skills.items():
                if skill in self.weaponSkill.keys():
                    self.weaponSkill[skill] += amount
                else:
                    self.weaponSkill[skill] = amount
            self.weaponJewels.append(jewel)
            self.freeWeaponSlot -= jewel.slots
            return True
        else:
            return False

    def detachJeweltoWeapon(self, jewel: Jewel) -> bool:
        if jewel.name in self.weaponJewels:
            for skill, amount in jewel.skills.items():
                if self.weaponSkill[skill] > jewel.skills[skill]:
                    self.weaponSkill[skill] -= jewel.skills[skill]
                else:
                    self.weaponSkill.pop(skill)
            self.weaponJewels.remove(jewel)
            self.weaponSlot += jewel.slots
            return True
        else:
            return False

    def resetHead(self):
        self.armorSet["Head"] = Optional[ArmorPiece]

    def resetTorso(self):
        self.armorSet["Torso"] = Optional[ArmorPiece]

    def resetArm(self):
        self.armorSet["Arm"] = Optional[ArmorPiece]

    def resetWaist(self):
        self.armorSet["Waist"] = Optional[ArmorPiece]

    def resetleg(self):
        self.armorSet["leg"] = Optional[ArmorPiece]

    def skills(self) -> list[str]:
        return list(self.skillTableTotal().keys())

    def skillTableTotal(self) -> dict[str, int]:
        skillList = defaultdict(int)
        for armorPiece in self.armorSet.values():
            for skill, amount in armorPiece.skills.items():
                if skill == "Torso Inc.":
                    for torsoskill, torsoamount in self.armorSet["Torso"].skills.items():
                        skillList[torsoskill] += torsoamount
                skillList[skill] += amount
        return dict(sorted(skillList.items(), key=lambda x: x[1], reverse=True))

    def skilltable(self, skillData: list[Skill]) -> list[tuple]:
        skillTable = [("Skill", "Active", "Head", "Torso", "Arm", "Waist", "Leg", "Total")]
        skillTotal = self.skillTableTotal()
        activeSkill = {skill.name: skill.getActiveNameFromLevel(skillTotal[skill.name]) for skill in skillData if skill.isActive(skillTotal[skill.name])}
        for skill in skillTotal.keys():
            row = (skill, activeSkill.get(skill, ""),)
            for armorPiece in self.armorSet.values():
                if armorPiece is None or armorPiece.getSkillAmount(skill) is None:
                    row += ('',)
                else:
                    if skillTotal.get("Torso Inc.") is not None and armorPiece.isTorso():
                        row += (armorPiece.getSkillAmount(skill),) * skillTotal.get("Torso Inc.")
                    else:
                        row += (armorPiece.getSkillAmount(skill),)
            row += (skillTotal[skill],)
            skillTable.append(row)
        return skillTable

    def resTableTotal(self) -> dict[str, int]:
        resList = {"def": 0,
                   "fire": 0,
                   "water": 0,
                   "thunder": 0,
                   "ice": 0,
                   "dragon": 0}
        for armorPiece in self.armorSet.values():
            resList["def"] += armorPiece.defense
            resList["fire"] += armorPiece.fireRes
            resList["water"] += armorPiece.waterRes
            resList["thunder"] += armorPiece.thunderRes
            resList["ice"] += armorPiece.iceRes
            resList["dragon"] += armorPiece.dragonRes
        return resList

    def totalCost(self) -> int:
        cost = 0
        for armorPiece in self.armorSet.values():
            cost += armorPiece.cost
        return cost

    def materialList(self) -> dict[str, int]:
        materials = {}
        for armorPiece in self.armorSet.values():
            for material, amount in armorPiece.materials.items():
                if material in materials.keys():
                    materials[material] += amount
                else:
                    materials[material] = amount
        return materials

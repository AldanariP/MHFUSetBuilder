from ArmorPiece import *
from Parts import *
from Gender import *
from typing import Optional
from collections import Counter


def genderWaring(armorPiece, armorSet):
    return (f"ArmorPiece '{armorPiece.name()}' of gender '{armorPiece.gender().value}' "
            f"is not compatible with the set gender '{armorSet.setGender()}'")


def classWaring(armorPiece, armorSet):
    return (f"ArmorPiece '{armorPiece.name()}' class '{armorPiece.part().value}' "
            f"is not compatible with the set class : '{armorSet.setClass()}'")


class ArmorSet:
    def __init__(self):
        self.__armorSet = {"Head": Optional[ArmorPiece],
                           "Torso": Optional[ArmorPiece],
                           "Arm": Optional[ArmorPiece],
                           "Waist": Optional[ArmorPiece],
                           "Leg": Optional[ArmorPiece]}
        self.__setClass = None
        self.__setGender = None

    def pieces(self):
        return self.__armorSet

    def setHead(self, headPiece: ArmorPiece):
        if headPiece.part() != Part.HEAD:
            raise ValueError(f"ArmorPiece '{headPiece.name()}' is not a Head Piece")

        elif self.__setGender is not None and (
                headPiece.gender() != self.__setGender or headPiece.gender() != Gender.BOTH):
            raise ValueError(genderWaring(headPiece, self))

        else:
            self.__setGender = headPiece.gender()
            self.__armorSet["Head"] = headPiece

    def setTorso(self, torsoPiece: ArmorPiece):
        if torsoPiece.part() != Part.TORSO:
            raise ValueError(f"ArmorPiece '{torsoPiece.name()}' is not a Torso Piece")

        elif self.__setClass is not None and torsoPiece.armor_class() != self.__setClass:
            raise ValueError(classWaring(torsoPiece, self))

        elif self.__setGender is not None and (
                torsoPiece.gender() != self.__setGender or torsoPiece.gender() != Gender.BOTH):
            raise ValueError(genderWaring(torsoPiece, self))

        else:
            self.__setClass = torsoPiece.armor_class()
            self.__setGender = torsoPiece.gender()
            self.__armorSet["Torso"] = torsoPiece

    def setArm(self, armPiece: ArmorPiece):
        if armPiece.part() != Part.ARM:
            raise ValueError(f"ArmorPiece '{armPiece.name()}' is not an Arm Piece")

        elif self.__setClass is not None and armPiece.armor_class() != self.__setClass:
            raise ValueError(classWaring(armPiece, self))

        elif self.__setGender is not None and (
                armPiece.gender() != self.__setGender or armPiece.gender() != Gender.BOTH):
            raise ValueError(genderWaring(armPiece, self))

        else:
            self.__setClass = armPiece.armor_class()
            self.__setGender = armPiece.gender()
            self.__armorSet["Arm"] = armPiece

    def setWaist(self, waistPiece: ArmorPiece):
        if waistPiece.part() != Part.WAIST:
            raise ValueError(f"ArmorPiece '{waistPiece.name()}' is not a Waist Piece")

        elif self.__setClass is not None and waistPiece.armor_class() != self.__setClass:
            raise ValueError(classWaring(waistPiece, self))

        elif self.__setGender is not None and (
                waistPiece.gender() != self.__setGender or waistPiece.gender() != Gender.BOTH):
            raise ValueError(genderWaring(waistPiece, self))

        else:
            self.__setClass = waistPiece.armor_class()
            self.__setGender = waistPiece.gender()
            self.__armorSet["Waist"] = waistPiece

    def setLeg(self, legPiece: ArmorPiece):
        if legPiece.part() != Part.LEG:
            raise ValueError(f"ArmorPiece '{legPiece.name()}' is not a Leg Piece")

        elif self.__setClass is not None and legPiece.armor_class() != self.__setClass:
            raise ValueError(classWaring(legPiece, self))

        elif self.__setGender is not None and (
                legPiece.gender() != self.__setGender or legPiece.gender() != Gender.BOTH):
            raise ValueError(genderWaring(legPiece, self))

        else:
            self.__setClass = legPiece.armor_class()
            self.__setGender = legPiece.gender()
            self.__armorSet["Leg"] = legPiece

    def setAllPieces(self, ArmorPieceList: list[ArmorPiece]):
        if Counter(i.armor_class() for i in ArmorPieceList) != \
                {Part.HEAD: 1, Part.TORSO: 1, Part.ARM: 1, Part.WAIST: 1, Part.LEG: 1}:
            raise ValueError("Armor Piece list provided is not valid")

        for i in ArmorPieceList:
            if i.armor_class() == Part.HEAD:
                self.setHead(i)
            if i.armor_class() == Part.TORSO:
                self.setTorso(i)
            if i.armor_class() == Part.ARM:
                self.setArm(i)
            if i.armor_class() == Part.WAIST:
                self.setWaist(i)
            if i.armor_class() == Part.LEG:
                self.setLeg(i)

    def resetHead(self):
        self.__armorSet["Head"] = Optional[ArmorPiece]

    def resetTorso(self):
        self.__armorSet["Torso"] = Optional[ArmorPiece]

    def resetArm(self):
        self.__armorSet["Arm"] = Optional[ArmorPiece]

    def resetWaist(self):
        self.__armorSet["Waist"] = Optional[ArmorPiece]

    def resetleg(self):
        self.__armorSet["leg"] = Optional[ArmorPiece]

    def setClass(self):
        return self.__setClass

    def setGender(self):
        return self.__setGender

    def skillTable(self):
        skillList = {}
        for armorPiece in self.__armorSet.values():
            for skill, amount in armorPiece.skills().items():
                if skill == "Torso Inc.":
                    for torsoskill, torsoamount in self.__armorSet["Torso"].skills().items():
                        if torsoskill in skillList.keys():
                            skillList[torsoskill] += torsoamount
                        else:
                            skillList[torsoskill] = torsoamount
                else:
                    if skill in skillList.keys():
                        skillList[skill] += amount
                    else:
                        skillList[skill] = amount
        return skillList

    def resTable(self):
        resList = {"def": 0,
                   "fire": 0,
                   "water": 0,
                   "thunder": 0,
                   "ice": 0,
                   "dragon": 0}
        for armorPiece in self.__armorSet.values():
            resList["def"] += armorPiece.defense()
            resList["fire"] += armorPiece.fireRes()
            resList["water"] += armorPiece.waterRes()
            resList["thunder"] += armorPiece.thunderRes()
            resList["ice"] += armorPiece.iceRes()
            resList["dragon"] += armorPiece.dragonRes()
        return resList

    def totalCost(self):
        cost = 0
        for armorPiece in self.__armorSet.values():
            cost += armorPiece.cost()
        return cost

    def materialList(self):
        materials = {}
        for armorPiece in self.__armorSet.values():
            for material, amount in armorPiece.materials().items():
                if material in materials.keys():
                    materials[material] += amount
                else:
                    materials[material] = amount
        return materials

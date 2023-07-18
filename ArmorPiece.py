import ArmorClass
import Gender
import Parts
import Rarity


class ArmorPiece:

    def __init__(self, name, data):
        try:
            piece = data[name]
            self.__name = piece['name']
            self.__rarity = Rarity.Rarity(piece['rarity']).rarity()
            self.__part = Parts.Part(piece['part'])
            self.__armor_class = ArmorClass.ArmorClass(piece['class'])
            self.__gender = Gender.Gender(piece['gender'])
            self.__defense = piece['defense']
            self.__fireRes = piece['fireRes']
            self.__waterRes = piece['waterRes']
            self.__thunderRes = piece['thunderRes']
            self.__iceRes = piece['iceRes']
            self.__dragonRes = piece['dragonRes']
            self.__nbSlots = piece['nbSlots']
            self.__freeSlots = self.__nbSlots
            self.__jewels = []
            self.__skills = piece['skills']
            self.__cost = piece['cost']
            self.__materials = piece['materials']
        except KeyError as e:
            print(f"Error: '{name}' is not a valid armor piece name.")

    def name(self):
        return self.__name

    def rarity(self):
        return self.__rarity

    def part(self):
        return self.__part

    def defense(self):
        return self.__defense

    def fireRes(self):
        return self.__fireRes

    def waterRes(self):
        return self.__waterRes

    def thunderRes(self):
        return self.__thunderRes

    def iceRes(self):
        return self.__iceRes

    def dragonRes(self):
        return self.__dragonRes

    def nbSolt(self):
        return self.__nbSlots

    def freeSlot(self):
        return self.__freeSlots

    def jewels(self):
        return self.__jewels

    def skills(self):
        return self.__skills

    def armor_class(self):
        return self.__armor_class

    def gender(self):
        return self.__gender

    def cost(self):
        return self.__cost

    def materials(self):
        return self.__materials

    def rank(self):
        if self.__rarity <= 3:
            return "low"
        elif self.__rarity <= 8:
            return "high"
        else:
            return "G"

    def attachJewel(self, jewel):
        if jewel.slots() <= self.__freeSlots:
            for skill, amount in jewel.skills().items():
                if skill in self.__skills.keys():
                    self.__skills[skill] += amount
                else:
                    self.__skills[skill] = amount
            self.__jewels.append(jewel)
            self.__freeSlots -= jewel.slots()
            return True
        else:
            return False

    def detachJewel(self, jewel):
        if jewel.name() in self.__jewels:
            for skill, amount in jewel.skills().items():
                if self.__skills[skill] > jewel.skills()[skill]:
                    self.__skills[skill] -= jewel.skills()[skill]
                else:
                    self.__skills.pop(skill)
            self.__jewels.pop(jewel)
            self.__freeSlots += jewel.slots()
            return True
        else:
            return False

    def __str__(self):
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

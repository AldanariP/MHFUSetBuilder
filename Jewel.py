class Jewel:

    def __init__(self, data):
        self.name = data["name"]
        self.skills = data["skill"]
        self.material = data["material"]
        self.slots = data["slot"]
        self.cost = data["cost"]

    def __str__(self):
        result = (
            f"Name     : {self.name}\n"
            f"nbSlots  : {self.slots}\n"
            f"Cost     : {self.cost}z\n"
            f"Skills   : \n"
        )
        max_key_width = max(len(i) for i in self.skills.keys())

        for skill, value in self.skills.items():
            key = f"{skill}".ljust(max_key_width)
            if value >= 0:
                result += f"    {key} :  {value}\n"
            else:
                result += f"    {key} : {value}\n"

        max_key_width = max(len(i) for i in self.material.keys())

        result += f"Material :\n"
        for material, value in self.material.items():
            key = f"{material}".ljust(max_key_width)
            result += f"    {key} : {value}\n"

        return result

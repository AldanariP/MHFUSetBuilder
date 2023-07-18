class Jewel:

    def __init__(self, name, data):
        try:
            dataJewel = data[name]
            self.__name = dataJewel["name"]
            self.__skills = dataJewel["skill"]
            self.__material = dataJewel["material"]
            self.__slots = dataJewel["slot"]
            self.__cost = dataJewel["cost"]
        except KeyError as e:
            print(f"Error: '{name}' is not a valid Jewel name.")

    def name(self):
        return self.__name

    def skills(self):
        return self.__skills

    def materials(self):
        return self.__material

    def slots(self):
        return self.__slots

    def cost(self):
        return self.__cost

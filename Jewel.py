class Jewel:

    def __init__(self, data):
        self.__name = data["name"]
        self.__skills = data["skill"]
        self.__material = data["material"]
        self.__slots = data["slot"]
        self.__cost = data["cost"]

    def name(self) -> str:
        return self.__name

    def skills(self) -> dict[str, int]:
        return self.__skills

    def materials(self) -> dict[str, int]:
        return self.__material

    def slots(self) -> int:
        return self.__slots

    def cost(self) -> int:
        return self.__cost

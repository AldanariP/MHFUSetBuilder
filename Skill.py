class Skill:
    def __init__(self, data):
        self.__name = data["Name"]
        self.__description = data["Description"]
        self.__levels = data["Levels"]
        self.__activeNames = data["ActiveNames"]
        self.__subDescription = data["SubDescriptions"]

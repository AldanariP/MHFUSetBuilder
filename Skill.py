class Skill:
    def __init__(self, data):
        self.name = data["Name"]
        self.description = data["Description"]
        self.levels = data["Levels"]
        self.activeNames = data["ActiveNames"]
        self.subDescription = data["SubDescriptions"]

    def isActive(self, value: int) -> bool:
        if self.name != "Tosro Inc.":
            if any(i < 0 for i in self.levels):
                return value >= 10 or value <= -10
            else:
                return value >= 10
        else:
            return True

    def getActiveNameFromLevel(self, level: int) -> str:
        if level > max(self.levels):
            return self.activeNames[str(max(self.levels))]
        else:
            return self.activeNames[str((level // 5) * 5)]

    def getsubDescriptionFromLevel(self, level: int) -> str:
        if level in self.levels.contain():
            return self.subDescription[str(level)]
        else:
            raise IndexError("Skill does not have that level")

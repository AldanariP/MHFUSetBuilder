class Rarity:
    def __init__(self, rarity: int):
        if rarity <= 0:
            raise ValueError(f"The Rarity must be at least 1, got : '{rarity}'")
        elif rarity > 10:
            raise ValueError(f"The Rarity must be at most 9, got : '{rarity}'")
        else:
            self.__rarity = rarity

    def rarity(self):
        return self.__rarity

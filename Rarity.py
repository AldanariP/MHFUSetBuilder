class Rarity:
    def __init__(self, rarity: int):
        if rarity < 1:
            raise ValueError(f"The Rarity must be at least 1, got : '{rarity}'")
        elif rarity > 9:
            raise ValueError(f"The Rarity must be at most 9, got : '{rarity}'")
        else:
            self.rarity = rarity


import json


class PieceList:
    data = json.load(open('armorpiece.json', 'r'))

    def __init__(self):
        self.pieceList = []

    # def ofType(self, armorClass: ArmorClass) -> list[ArmorPiece]:

import json
import ArmorPiece


class PieceList:
    data = json.load(open('armorpiece.json', 'r'))

    def __init__(self):
        self.pieceList = []

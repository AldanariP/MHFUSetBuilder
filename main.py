import json
from ArmorPiece import ArmorPiece
from ArmorSet import ArmorSet

try:
    with open('armorpiece.json', 'r') as file:
        data = json.load(file)
        mySet = ArmorSet()
        mySet.setHead(ArmorPiece("Mafumofu Hood", data))
        mySet.setTorso(ArmorPiece("Mafumofu Jacket", data))
        mySet.setArm(ArmorPiece("Mafumofu Mittens", data))
        mySet.setWaist(ArmorPiece("Mafumofu Coat", data))
        mySet.setLeg(ArmorPiece("Mafumofu Boots", data))
        print(mySet.materialList())
        # root = tk.Tk()
        # root.minsize(480, 480)
        # label = tk.Label(root, text=str(head), justify="left", font="UbuntuMono")
        # label.pack()
        # root.mainloop()
except FileNotFoundError as e:
    print("Error: File 'armorpiece.json' not found.")

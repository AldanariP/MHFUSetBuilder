import json
from ArmorPiece import ArmorPiece
from ArmorSet import ArmorSet
from Jewel import Jewel

try:
    with open('armorpiece.json', 'r') as file:
        data = json.load(file)
        jeweldata = json.load(open("jewel.json", "r"))
        mySet = ArmorSet()
        helm = ArmorPiece("Mafumofu Mittens", data)
        print(helm)
        if helm.attachJewel(Jewel("WarmBreeze Jewel", jeweldata)):
            print("SUCCES\n", helm)
        else:
            print("FAIL")
        # mySet.setHead(ArmorPiece("Mafumofu Hood", data))
        # mySet.setTorso(ArmorPiece("Mafumofu Jacket", data))
        # mySet.setArm(ArmorPiece("Mafumofu Mittens", data))
        # mySet.setWaist(ArmorPiece("Mafumofu Coat", data))
        # mySet.setLeg(ArmorPiece("Mafumofu Boots", data))
        # root = tk.Tk()
        # root.minsize(480, 480)
        # label = tk.Label(root, text=str(head), justify="left", font="UbuntuMono")
        # label.pack()
        # root.mainloop()
except FileNotFoundError as e:
    print("Error: File 'armorpiece.json' not found.")

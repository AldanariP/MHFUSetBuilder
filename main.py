from ArmorSet import ArmorSet
from DataLoader import DataLoader

data = DataLoader()
jewel = data.getJewelData("PickyEater Jewel")
armor = data.getArmorData("Mafumofu Coat")
skill = data.getSkillData("Attack")

mySet = ArmorSet()
mySet.setHead(data.getArmorData("Mafumofu Hood"))
mySet.setTorso(data.getArmorData("Mafumofu Jacket"))
mySet.setArm(data.getArmorData("Mafumofu Mittens"))
mySet.setWaist(data.getArmorData("Mafumofu Coat"))
mySet.setLeg(data.getArmorData("Mafumofu Boots"))
skillTable = mySet.skilltable([data.getSkillData(i) for i in mySet.skills()])
print(skillTable)

with open("HunterSet.html") as file:
    data = file.readlines()

startLine = [index + 1 for index, line in enumerate(data) if "ffaq" in line][1]
stopline = [index + startLine + 1 for index, line in enumerate(data[startLine::]) if "/table" in line][1]

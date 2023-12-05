def getAdjacent(arr, i, j):
    v = []

    def addIfValidPos(x, y):
        if (
            0 <= x < len(arr)
            and 0 <= y < len(arr[0])
            and arr[x][y] != "."
            and arr[x][y].isdigit()
        ):
            v.append([x, y])

    addIfValidPos(i - 1, j - 1)
    addIfValidPos(i - 1, j)
    addIfValidPos(i - 1, j + 1)
    addIfValidPos(i, j - 1)
    addIfValidPos(i, j + 1)
    addIfValidPos(i + 1, j - 1)
    addIfValidPos(i + 1, j)
    addIfValidPos(i + 1, j + 1)

    return v


def getWholeNum(arr, x, y):
    v = []
    combinedInt = 0
    v.append(int(arr[x][y]))
    while y + 1 < len(arr[x]) and arr[x][y + 1].isdigit():
        v.append(int(arr[x][y + 1]))
        y += 1
    y = y - len(v) + 1
    while y - 1 >= 0 and arr[x][y - 1].isdigit():
        v.insert(0, int(arr[x][y - 1]))
        y -= 1
    combinedInt = int("".join(map(str, v)))
    # print(combinedInt)
    return combinedInt


engine = []
resultArray = []
result = 0
specialChars = "!@#$%^&*()-+?_=,<>/"
with open("example.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        engine.append(row)
    for row in range(len(engine)):
        for col in range(len(engine[row])):
            if engine[row][col] in specialChars:
                coordList = getAdjacent(engine, row, col)
                print(coordList)
                tempArray = []
                for coordinates in coordList:
                    x, y = coordinates
                    wholeNum = getWholeNum(engine, x, y)
                    tempArray.append(wholeNum)
                    tempArray = list(set(tempArray))
                    print("Temp:", tempArray)
                resultArray += tempArray
                print("Result:", resultArray)

# print(resultArray)
resultArray = list(resultArray)
for i in range(len(resultArray)):
    result += resultArray[i]
print(result)

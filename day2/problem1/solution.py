import re

def parseLine(input_string):
    parsedString = re.findall("(\d+)\s*(red|green|blue)", input_string)
    return parsedString

gameNumber = 0
finalCount = 0
with open('input.txt', 'r') as file:
    for line in file:
        gameNumber += 1
        parsedString = parseLine(line)
        redCount = any(int(number) > 12 for number, color in parsedString if color == 'red')
        greenCount = any(int(number) > 13 for number, color in parsedString if color == 'green')
        blueCount = any(int(number) > 14 for number, color in parsedString if color == 'blue')
        if redCount == False and greenCount == False and blueCount == False:
            finalCount += gameNumber
print(finalCount)
import re

def parseLine(input_string):
    parsedString = re.findall("(\d+)\s*(red|green|blue)", input_string)
    return parsedString

solution = 0
with open('input.txt', 'r') as file:
    for line in file:
        parsedString = parseLine(line)
        redMax = max(int(number) for number, color in parsedString if color == 'red')
        greenMax = max(int(number) for number, color in parsedString if color == 'green')
        blueMax = max(int(number) for number, color in parsedString if color == 'blue')
        solution += redMax * greenMax * blueMax
print(solution)
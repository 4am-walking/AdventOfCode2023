import re


def matchesToList(pattern, line):
    matches = pattern.findall(line)
    for match in matches:
        num = match.split()
        print(num)
    return num


winningNumPattern = re.compile(r":\s*(\d+\s+\d+\s+\d+\s+\d+\s+\d+)\s*\|")
scratcherPattern = re.compile(r"(\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+)")
matches = 0
with open("example.txt", "r") as file:
    for line in file:
        winningNumbers = matchesToList(winningNumPattern, line)
        scratcherNumbers = matchesToList(scratcherPattern, line)

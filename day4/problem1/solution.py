import re

def matchesToList(pattern, line):
    matches = pattern.findall(line)
    for match in matches:
        num = match.split()
    return num

matches = 0
result = 0
winningNumPattern = re.compile(r":\s*(\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+)\s*\|")
scratcherPattern = re.compile(r"(\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+)")
with open("input.txt", "r") as file:
    for line in file:
        winningNumbers = matchesToList(winningNumPattern, line)
        scratcherNumbers = matchesToList(scratcherPattern, line)
        counter = 0
        temp = 1
        for num in winningNumbers:
            if num in scratcherNumbers:
                counter += 1
        if counter >= 1:
            for _ in range(counter - 1):
                if counter == 1:
                    break
                else:
                    temp *= 2
        else:
            temp = 0
        result += temp
print(result)

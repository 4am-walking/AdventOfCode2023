with open("input.txt", "r") as file:
    solution = 0
    for line in file:
        first = None
        for x in range(len(line)):
            if line[x].isdigit():
                first = line[x]
                break
        line_reversed = line[::-1]
        last = None
        for x in range(len(line_reversed)):
            if line_reversed[x].isdigit():
                last = line_reversed[x]
                break

        if first is not None and last is not None:
            solution += int(first + last)
print(solution)

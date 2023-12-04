word_to_digit = {
    'zero': 'z0e',
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

def convert_string_to_number(input_string):
    for word, number in word_to_digit.items():
        input_string = input_string.replace(word, number)
    return input_string
    

with open("input.txt", "r") as file:
    solution = 0
    for line in file:
        converted_line = convert_string_to_number(line)
        first = None
        for x in range(len(converted_line)):
            if converted_line[x].isdigit():
                first = converted_line[x]
                break
        line_reversed = converted_line[::-1]
        last = None
        for x in range(len(line_reversed)):
            if line_reversed[x].isdigit():
                last = line_reversed[x]
                break

        if first is not None and last is not None:
            solution += int(first + last)

print(solution)

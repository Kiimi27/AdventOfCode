import re


def main(input_text):
    result = 0

    for multiplication in re.findall('mul\((\d+),(\d+)\)', input_text):
        result += int(multiplication[0]) * int(multiplication[1])

    return result

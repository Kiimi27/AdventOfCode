import re


def main(input_text):
    result = 0

    next_match = re.search('mul\((\d+),(\d+)\)', input_text)
    multiplication_enabled = True

    while next_match:
        while input_text.find('do()') < next_match.span()[0] and not input_text.find('do()') == -1 or input_text.find('don\'t()') < next_match.span()[0] and not input_text.find('don\'t()') == -1:
            if input_text.find('do()') < next_match.span()[0] and not input_text.find('do()') == -1:
                multiplication_enabled = True
                input_text = input_text[input_text.find('do()') + 1:]
            next_match = re.search('mul\((\d+),(\d+)\)', input_text)
            if input_text.find('don\'t()') < next_match.span()[0] and not input_text.find('don\'t()') == -1:
                multiplication_enabled = False
                input_text = input_text[input_text.find('don\'t()') + 1:]
            next_match = re.search('mul\((\d+),(\d+)\)', input_text)
        if multiplication_enabled:
            result += int(next_match[1]) * int(next_match[2])
        input_text = input_text[next_match.span()[1]:]
        next_match = re.search('mul\((\d+),(\d+)\)', input_text)

    return result

from math import floor


def main(input_text):
    result = 0

    input_parts = input_text.split('\n\n')
    ordering_rules = [[int(number) for number in line.split('|')] for line in input_parts[0].split('\n')]
    updates = [[int(number) for number in line.split(',')] for line in input_parts[1].split('\n')[:-1]]

    for update in updates:
        correct_order = True
        for rule in ordering_rules:
            if rule[0] not in update or rule[1] not in update:
                continue
            if update.index(rule[0]) > update.index(rule[1]):
                correct_order = False
                break
        if correct_order:
            result += update[floor(len(update) / 2)]

    return result
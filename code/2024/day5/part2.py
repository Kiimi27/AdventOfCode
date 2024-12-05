from math import floor


def main(input_text):
    result = 0

    input_parts = input_text.split('\n\n')
    ordering_rules = [[int(number) for number in line.split('|')] for line in input_parts[0].split('\n')]
    updates = [[int(number) for number in line.split(',')] for line in input_parts[1].split('\n')[:-1]]

    for update in updates:
        rules_to_follow = []
        for rule in ordering_rules:
            if rule[0] in update and rule[1] in update:
                rules_to_follow.append(rule)
        if not all([check_rule(rule, update) for rule in rules_to_follow]):
            while not all([check_rule(rule, update) for rule in rules_to_follow]):
                for rule in rules_to_follow:
                    if check_rule(rule, update):
                        continue
                    update.remove(rule[0])
                    update.insert(update.index(rule[1]), rule[0])
            result += update[floor(len(update) / 2)]

    return result


def check_rule(rule, update):
    return update.index(rule[0]) < update.index(rule[1])

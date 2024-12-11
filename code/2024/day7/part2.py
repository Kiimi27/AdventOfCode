from copy import copy

operator_combinations = []

def main(input_text):
    global operator_combinations
    result = 0

    for line in input_text.split('\n')[:-1]:
        line_parts = line.split(': ')
        expected = int(line_parts[0])
        numbers = [int(num) for num in line_parts[1].split(' ')]

        operator_combinations = []
        operators = [None] * (len(numbers) - 1)
        generate_operators(len(numbers) - 1, operators, 0)

        for operator_combination in operator_combinations:
            cur_result = numbers[0]
            for o_index in range(len(operator_combination)):
                if operator_combination[o_index] == '+':
                    cur_result += numbers[o_index + 1]
                elif operator_combination[o_index] == '*':
                    cur_result *= numbers[o_index + 1]
                elif operator_combination[o_index] == '|':
                    cur_result = int(str(cur_result) + str(numbers[o_index + 1]))
            if cur_result == expected:
                result += cur_result
                break
    return result


def generate_operators(length, operators, i):
    global operator_combinations

    if i == length:
        operator_combinations.append(copy(operators))
        return

    operators[i] = '+'
    generate_operators(length, operators, i + 1)

    operators[i] = '*'
    generate_operators(length, operators, i + 1)

    operators[i] = '|'
    generate_operators(length, operators, i + 1)

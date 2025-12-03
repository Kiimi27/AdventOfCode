
def main(input_text):
    result = 0

    for bank in input_text.splitlines():
        first_joltage_digit = '0'
        for battery in bank[:-1]:
            if int(battery) > int(first_joltage_digit):
                first_joltage_digit = battery
                if first_joltage_digit == '9':
                    break
        first_digit_index = bank.index(first_joltage_digit)
        second_joltage_digit = '0'
        for battery in bank[first_digit_index + 1:]:
            if int(battery) > int(second_joltage_digit):
                second_joltage_digit = battery
                if second_joltage_digit == '9':
                    break

        result += int(first_joltage_digit + second_joltage_digit)

    return result
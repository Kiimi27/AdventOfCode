
def main(input_text):
    result = 0

    for bank in input_text.splitlines():
        battery_joltage = '0'
        for battery in bank[:-11]:
            if int(battery) > int(battery_joltage):
                battery_joltage = battery
                if battery_joltage == '9':
                    break
        next_joltage_digit = battery_joltage
        for i in range(11):
            last_digit_index = bank.index(next_joltage_digit)
            bank = bank[last_digit_index + 1:]
            next_joltage_digit = '0'
            searchable_bank = bank[:-10+i]
            if searchable_bank == "":
                searchable_bank = bank
            for battery in searchable_bank:
                if int(battery) > int(next_joltage_digit):
                    next_joltage_digit = battery
                    if next_joltage_digit == '9':
                        break
            battery_joltage += next_joltage_digit

        result += int(battery_joltage)

    return result
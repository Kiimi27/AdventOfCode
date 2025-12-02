
def main(input_text):
    result = 0
    dial_pos = 50

    for line in input_text.splitlines():
        dial_pos += int(line.replace('L', '-').replace('R', '')) % 100

        if dial_pos < 0:
            dial_pos = 100 + dial_pos % 100
        elif dial_pos > 99:
            dial_pos = -1 + (dial_pos - 99)
        if dial_pos == 0:
            result += 1

    return result
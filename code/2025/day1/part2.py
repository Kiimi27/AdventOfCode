import math

def main(input_text):
    result = 0
    dial_pos = 50

    for line in input_text.splitlines():
        # get the amount the dial needs to be turned
        dial_shift = int(line.replace('L', '-').replace('R', ''))
        # add the number of full turns to the counter
        result += math.floor(abs(dial_shift) / 100)

        # remove full turns
        if dial_shift < 0:
            reduced_dial_shift = dial_shift % -100
        else:
            reduced_dial_shift = dial_shift % 100

        # turn dial
        dial_pos += reduced_dial_shift

        if dial_pos < 0:
            # wrap around back up to 99, only add if the dial wasn't at 0 before turning
            if dial_pos - reduced_dial_shift != 0:
                result += 1
            dial_pos = dial_pos % 100
        elif dial_pos > 99:
            # wrap around back down to 0, add to counter
            dial_pos = -1 + (dial_pos - 99)
            result += 1
        elif dial_pos == 0:
            # dial points to 0, add to counter
            result += 1

    return result
import re

def main(input_text):
    result = 0

    for pid_range in input_text.split(','):
        start, end = pid_range.split('-')
        for pid in range(int(start), int(end) + 1):
            if re.match(r'^([1-9][0-9]*)\1$', str(pid)):
                result += pid

    return result
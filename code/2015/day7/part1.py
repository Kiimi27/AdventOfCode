import numpy

def main(input_text):
    result = ''

    starting_parts = []
    parts = []
    for line in input_text.split('\n')[:-1]:
        split = line.split(' -> ')

        if 'NOT' in split[0]:
            parts.append([split[0].split(' ')[0], split[0].split(' ')[1], split[1]])
        elif 'AND' in split[0] or 'OR' in split[0] or 'LSHIFT' in split[0] or 'RSHIFT' in split[0]:
            parts.append([split[0].split(' ')[1], [split[0].split(' ')[0], split[0].split(' ')[2]] , split[1]])
        else:
            starting_parts.append([split[0], split[1]])

    # TODO trace a wire backwards


    return result
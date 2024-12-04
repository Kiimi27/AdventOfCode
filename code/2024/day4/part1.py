WORD_TO_FIND = 'XMAS'

def main(input_text):
    result = 0

    word_grid = []

    for line in input_text.split('\n')[:-1]:
        word_grid.append([])
        for char in line:
            word_grid[-1].append(char)

    for y in range(len(word_grid)):
        for x in range(len(word_grid[y])):
            if word_grid[y][x] == WORD_TO_FIND[0]:
                for y_dir in range(-1, 2):
                    for x_dir in range(-1, 2):
                        if find_word(x, y, x_dir, y_dir, word_grid):
                            result += 1

    return result


def find_word(x, y, x_dir, y_dir, word_grid):
    if x + x_dir * (len(WORD_TO_FIND) - 1) >= len(word_grid[0]) or x + x_dir * (len(WORD_TO_FIND) - 1) < 0 or y + y_dir * (len(WORD_TO_FIND) - 1) >= len(word_grid) or y + y_dir * (len(WORD_TO_FIND) - 1) < 0:
        return False

    for i in range(1, len(WORD_TO_FIND)):
        if WORD_TO_FIND[i] != word_grid[y + y_dir * i][x + x_dir * i]:
            return False

    return True

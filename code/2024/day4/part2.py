WORD_TO_FIND = 'MAS'

def main(input_text):
    result = 0

    word_grid = []

    for line in input_text.split('\n')[:-1]:
        word_grid.append([])
        for char in line:
            word_grid[-1].append(char)

    for y in range(1, len(word_grid) - 1):
        for x in range(1, len(word_grid[y]) - 1):
            if word_grid[y][x] == WORD_TO_FIND[1]:
                if (word_grid[y - 1][x - 1] == WORD_TO_FIND[0] and word_grid[y + 1][x + 1] == WORD_TO_FIND[2] or word_grid[y + 1][x + 1] == WORD_TO_FIND[0] and word_grid[y - 1][x - 1] == WORD_TO_FIND[2]) and (word_grid[y + 1][x - 1] == WORD_TO_FIND[0] and word_grid[y - 1][x + 1] == WORD_TO_FIND[2] or word_grid[y - 1][x + 1] == WORD_TO_FIND[0] and word_grid[y + 1][x - 1] == WORD_TO_FIND[2]):
                    result += 1

    return result

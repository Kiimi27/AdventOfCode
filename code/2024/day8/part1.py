
def main(input_text):

    grid = []
    for line in input_text.split('\n')[:-1]:
        grid.append([])
        for char in line:
            grid[-1].append(char)

    antenna_frequencies = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                if not grid[y][x] in antenna_frequencies:
                    antenna_frequencies[grid[y][x]] = []
                antenna_frequencies[grid[y][x]].append([x, y])

    antinodes = set()
    for frequency in antenna_frequencies.values():
        for antenna in frequency:
            for other_antenna in frequency:
                if other_antenna == antenna:
                    continue
                x_order = antenna[0] < other_antenna[0]
                y_order = antenna[1] < other_antenna[1]
                if x_order:
                    antinode_x = antenna[0] - (other_antenna[0] - antenna[0])
                else:
                    antinode_x = antenna[0] + (antenna[0] - other_antenna[0])
                if y_order:
                    antinode_y = antenna[1] - (other_antenna[1] - antenna[1])
                else:
                    antinode_y = antenna[1] + (antenna[1] - other_antenna[1])

                if 0 <= antinode_y < len(grid) and 0 <= antinode_x < len(grid[0]):
                    antinodes.add((antinode_x, antinode_y))

    return len(antinodes)

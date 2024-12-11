
def main(input_text):
    result = 0

    grid = []
    for line in input_text.split('\n')[:-1]:
        grid.append([])
        for char in line:
            try:
                grid[-1].append(int(char))
            except:
                grid[-1].append(char)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                trails = climb_trail(9, x, y, grid)
                print(x, y, trails)
                result += trails

    return result

def climb_trail(end_height, x, y, grid):
    if grid[y][x] == end_height:
        return 1
    result = 0

    if 0 <= x - 1 and grid[y][x - 1] == grid[y][x] + 1:
        result += climb_trail(end_height, x - 1, y, grid)
    if x + 1 < len(grid[0]) and grid[y][x + 1] == grid[y][x] + 1:
        result += climb_trail(end_height, x + 1, y, grid)
    if 0 <= y - 1 and grid[y - 1][x] == grid[y][x] + 1:
        result += climb_trail(end_height, x, y - 1, grid)
    if y + 1 < len(grid) and grid[y + 1][x] == grid[y][x] + 1:
        result += climb_trail(end_height, x, y + 1, grid)

    return result

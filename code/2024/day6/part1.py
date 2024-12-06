
def main(input_text):

    map_grid = input_text.split('\n')[:-1]
    guard_pos = [0, 0]
    guard_dir = [0, -1]

    for y in range(len(map_grid)):
        for x in range(len(map_grid[y])):
            if map_grid[y][x] == '^':
                guard_pos = [x, y]

    visited_positions = set()
    visited_positions.add((guard_pos[0], guard_pos[1]))

    try:
        while True:
            if map_grid[guard_pos[1] + guard_dir[1]][guard_pos[0] + guard_dir[0]] == '#':
                if guard_dir == [0, 1]:
                    guard_dir = [-1, 0]
                elif guard_dir == [0, -1]:
                    guard_dir = [1, 0]
                elif guard_dir == [1, 0]:
                    guard_dir = [0, 1]
                elif guard_dir == [-1, 0]:
                    guard_dir = [0, -1]
            else:
                guard_pos = [guard_pos[0]+ guard_dir[0], guard_pos[1] + guard_dir[1]]
                visited_positions.add((guard_pos[0], guard_pos[1]))
    except:
        pass

    return len(visited_positions)

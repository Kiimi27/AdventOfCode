import copy
import queue
import threading

pos_queue = queue.Queue()
map_grid = ['']
start_x = 0
start_y = 0
possible_locations = queue.Queue()

def main(input_text):
    global map_grid, start_x, start_y

    map_grid = input_text.split('\n')[:-1]

    for y in range(len(map_grid)):
        for x in range(len(map_grid[y])):
            if map_grid[y][x] == '^':
                start_x = x
                start_y = y

    current_pos = [start_x, start_y]
    visited_positions = set()
    visited_positions.add((current_pos[0], current_pos[1]))
    current_dir = [0, -1]

    try:
        while True:
            if map_grid[current_pos[1] + current_dir[1]][current_pos[0] + current_dir[0]] == '#':
                if current_dir == [0, 1]:
                    current_dir = [-1, 0]
                elif current_dir == [0, -1]:
                    current_dir = [1, 0]
                elif current_dir == [1, 0]:
                    current_dir = [0, 1]
                elif current_dir == [-1, 0]:
                    current_dir = [0, -1]
            else:
                current_pos = [current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]]
                visited_positions.add((current_pos[0], current_pos[1]))
    except:
        pass

    for pos in visited_positions:
        pos_queue.put(pos)

    threads = [threading.Thread(check_position()) for _ in range(16)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return possible_locations.qsize()

def check_position():
    global map_grid, possible_locations
    while pos_queue.qsize() > 0:
        x, y = pos_queue.get()

        guard_pos = [[start_x, start_y], [0, -1]]
        guard_dir = [0, -1]
        visited_positions = []

        new_grid = copy.copy(map_grid)
        new_grid[y] = map_grid[y][:x] + '#' + map_grid[y][x + 1:]
        break_loop = False
        try:
            while not guard_pos in visited_positions:
                step = 0
                while not new_grid[guard_pos[0][1] + guard_dir[1] * (step + 1)][guard_pos[0][0] + guard_dir[0] * (step + 1)] == '#':
                    if guard_pos[0][1] + guard_dir[1] * (step + 1) < 0 or guard_pos[0][0] + guard_dir[0] * (step + 1) < 0:
                        break_loop = True
                        break
                    step += 1
                if break_loop:
                    break
                visited_positions.append(guard_pos)
                guard_pos = [[guard_pos[0][0] + guard_dir[0] * step, guard_pos[0][1] + guard_dir[1] * step],
                             [guard_dir[0], guard_dir[1]]]
                if guard_dir == [0, 1]:
                    guard_dir = [-1, 0]
                elif guard_dir == [0, -1]:
                    guard_dir = [1, 0]
                elif guard_dir == [1, 0]:
                    guard_dir = [0, 1]
                elif guard_dir == [-1, 0]:
                    guard_dir = [0, -1]
                guard_pos[1] = [guard_dir[0], guard_dir[1]]
        except:
            pass

        if guard_pos in visited_positions and not break_loop:
            possible_locations.put((x, y))
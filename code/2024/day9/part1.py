
def main(input_text):
    result = 0

    last_block = 0
    free_space = []
    files = []
    for index in range(len(input_text)):
        if index % 2 == 0:
            files.append([block for block in range(last_block, last_block + int(input_text[index]))])
        else:
            [free_space.append(block) for block in range(last_block, last_block + int(input_text[index]))]
        last_block += int(input_text[index])

    index = 0
    files.reverse()
    while len(free_space) > 0:
        for block_index in range(len(files[index])):
            free_space.sort()
            if files[index][block_index] > free_space[0]:
                free_space.append(files[index][block_index])
                files[index][block_index] = free_space[0]
                free_space.remove(files[index][block_index])
            else:
                free_space = []
                break
        index += 1

    files.reverse()
    for file_id in range(len(files)):
        for block in files[file_id]:
            result += block * file_id

    return result

def main(input_text):
    result = 0

    last_block = 0
    free_space = []
    files = []
    for index in range(len(input_text)):
        if index % 2 == 0:
            files.append([block for block in range(last_block, last_block + int(input_text[index]))])
        else:
            free_space.append([block for block in range(last_block, last_block + int(input_text[index]))])
        last_block += int(input_text[index])

    files.reverse()
    for reverse_file_index in range(len(files)):
        for space_index in range(len(free_space)):
            if len(free_space[space_index]) >= len(files[reverse_file_index]) and free_space[space_index][0] < files[reverse_file_index][0]:
                for i in range(len(files[reverse_file_index])):
                    files[reverse_file_index][i] = free_space[space_index][i]
                free_space[space_index] = free_space[space_index][len(files[reverse_file_index]):]
                break
        if [] in free_space:
            free_space.remove([])

    files.reverse()
    for file_id in range(len(files)):
        for block in files[file_id]:
            result += block * file_id

    return result
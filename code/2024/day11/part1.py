
def main(input_text):

    stones = [int(num) for num in input_text.split(' ')]

    for _ in range(25):
        for stone_index in range(len(stones)):
            if stones[stone_index] == 0:
                stones[stone_index] = 1
            elif len(str(stones[stone_index])) % 2 == 0:
                stones.append(int(str(stones[stone_index])[len(str(stones[stone_index])) // 2:]))
                stones[stone_index] = int(str(stones[stone_index])[:len(str(stones[stone_index])) // 2])
            else:
                stones[stone_index] *= 2024

    return len(stones)
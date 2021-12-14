import itertools

input_file = open(
    "H:\Personal\PRM\SkipsScramble_Repo\Advent_of_Code_2021\input_09_sample.txt"
)
input = input_file.read().splitlines()

# Note: basins can have flat part to them (every point is part of a basin that's not a 9)

ref_input = []

for item in input:
    new_item = str()
    for i in range(1, len(item)):
        if item[i] != "9":
            new_item = new_item + "0"
        else:
            new_item = new_item + "1"
    ref_input.append(new_item)

conf_indices = set()


def check_surroundings(row, col):
    for i in {-1, 1}:
        if row + i >= 0 and row + i <= len(ref_input) - 1:
            if ref_input[row + i][col] != 1:
                conf_indices.add((row + i, col))

    for i in {-1, 1}:
        if col + i >= 0 and col + i <= len(ref_input[0]) - 1:
            if ref_input[row][col + i] != 1:
                conf_indices.add((row, col + i))

    return conf_indices


check_surroundings(1, 2)


heights = 0
for i, j in itertools.product(range(len(input)), range(len(input[0]))):
    if input[i][j] < min(check_col(i, j) + check_row(i, j)):
        print(i, j)
        heights = heights + int(input[i][j]) + 1

print(heights)


import itertools

input_file = open(
    "H:\Personal\PRM\SkipsScramble_Repo\Advent_of_Code_2021\input_09_sample.txt"
)
input = input_file.read().splitlines()

# Note: basins can have flat part to them (every point is part of a basin that's not a 9)

test = []

for item in input[:2]:
    for i in range(1, len(item)):
        if i == 9:
            item[i].replace(str(i), "1")
        else:
            item.replace(str(i), "0")
    test.append(item)


def check_col(row, col):
    adj_vert = []
    for i in {-1, 1}:
        if row + i >= 0 and row + i <= len(input) - 1:
            adj_vert.append(input[row + i][col])

    return adj_vert


def check_row(row, col):
    adj_horiz = []
    for i in {-1, 1}:
        if col + i >= 0 and col + i <= len(input[0]) - 1:
            adj_horiz.append(input[row][col + i])

    return adj_horiz


check_col(4, 9)

check_row(4, 9)

heights = 0
for i, j in itertools.product(range(len(input)), range(len(input[0]))):
    if input[i][j] < min(check_col(i, j) + check_row(i, j)):
        print(i, j)
        heights = heights + int(input[i][j]) + 1

print(heights)


import itertools

input_file = open(
    "H:\Personal\PRM\SkipsScramble_Repo\Advent_of_Code_2021\input_09_sample.txt"
)
input = input_file.read().splitlines()

# Note: basins can have flat part to them (every point is part of a basin that's not a 9)

ref_input = []

for item in input:
    new_item = str()
    for i in range(0, len(item)):
        if item[i] != "9":
            new_item = new_item + "0"
        else:
            new_item = new_item + "1"
    ref_input.append(new_item)

# conf_indices = set()


def check_surroundings(row, col):
    for i in {-1, 1}:
        if row + i >= 0 and row + i <= len(ref_input) - 1:
            if ref_input[row + i][col] != "1":
                conf_indices.add((row + i, col))

    for i in {-1, 1}:
        if col + i >= 0 and col + i <= len(ref_input[0]) - 1:
            if ref_input[row][col + i] != "1":
                conf_indices.add((row, col + i))

    return conf_indices


conf_indices = {(4, 9)}

frozen_set = set()

while frozen_set != conf_indices:
    frozen_set = conf_indices.copy()

    for point in frozen_set:
        check_surroundings(point[0], point[1])

print(len(conf_indices))


# I think what I want is the following
# frozen_list = current_list
# loop over frozen_list and add new points to some list
# Add those new points to the current list (if not already done in the above step)
# repeat

basin_sizes = set()

for i, j in itertools.product(range(5), range(10)):
    conf_indices = {(i, j)}
    frozen_set = set()
    while frozen_set != conf_indices and ref_input[i][j] != "1":
        frozen_set = conf_indices.copy()

        for point in frozen_set:
            check_surroundings(point[0], point[1])
    # print("for ({}, {}), the size is {}".format(i,j, len(conf_indices)))
    basin_sizes.add(len(conf_indices))

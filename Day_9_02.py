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

conf_indices = set()


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


check_surroundings(2, 3)

add_points = True

while add_points == True:
    conf_indices = {(0, 9)}
    for point in conf_indices:
        old_len = len(conf_indices)
        conf_indices.union(check_surroundings(point[0], point[1]))
        new_len = len(conf_indices)
        if new_len > old_len:
            add_points = False

# I think what I want is the following
# frozen_list = current_list
# loop over frozen_list and add new points to some list
# Add those new points to the current list (if not already done in the above step)
# repeat

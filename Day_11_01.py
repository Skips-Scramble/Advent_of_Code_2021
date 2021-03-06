import itertools

input_file = open(
    "H:\Personal\PRM\SkipsScramble_Repo\Advent_of_Code_2021\input_11_sample.txt"
)
input = input_file.read().splitlines()

number_list = []

for i in range(len(input)):
    split_list = list(input[i])
    num_list = [int(x) for x in split_list]
    number_list.append(num_list)

# Scan numbers for a 10 (or more). If you see it, then add 1 to all of the
# surrounding numbers. And then set that 10 to a 0 to indicate it has been accounted for.
# Also need to get a dummy list of 1's and 0's to keep track of whether or not an entry has flashed. If it has, it just stays where it is and cannot increase its numbers

has_flashed = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


def add_one(list):
    list_plus_1 = [x + 1 for x in list]

    return list_plus_1


def add_one_matrix(matrix):
    output = []
    for row in matrix:
        list_plus_1 = [x + 1 for x in row]
        output.append(list_plus_1)

    return list_plus_1


add_one([1, 2, 3, 4, 5, 6, 7, 8, 9])


def light_nearby(matrix):
    for i, j in itertools.product(range(10), range(10)):
        if matrix[i][j] == 10:
            for k, l in itertools.product([-1, 1], [-1, 1]):
                matrix[i][j] = matrix[i][j] + 1

    return 0


light_nearby()


add_one(number_list)


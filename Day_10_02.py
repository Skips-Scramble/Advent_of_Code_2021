from collections import Counter
import statistics

input_file = open("H:\Personal\PRM\SkipsScramble_Repo\Advent_of_Code_2021\input_10.txt")
input = input_file.read().splitlines()

right_dict = {")": "(", "]": "[", "}": "{", ">": "<"}
right_dict_vals = {")": 1, "]": 2, "}": 3, ">": 4}

left_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}

# Let's just stip pairs successively

line_init = input[2]

line_frozen = ""
line = line_init

more_pairs = True
incomplete_lines = []

for line in input:
    more_pairs = True
    while more_pairs:
        print(line)
        line = line.replace("()", "")
        print(line)
        line = line.replace("[]", "")
        print(line)
        line = line.replace("{}", "")
        print(line)
        line = line.replace("<>", "")
        print(line)
        if "()" in line or "[]" in line or "{}" in line or "<>" in line:
            continue
        else:
            more_pairs = False
            right_chars = [x for x in line if x in right_dict.keys()]
            print(right_chars)
            # print("Your first incorrect item is {}".format(right_chars[0]))
            if right_chars == []:
                incomplete_lines.append(line)
            break


count_dict = dict(Counter(incomplete_lines[0]).items())

list_of_points = []

line = incomplete_lines[0]


def get_line_points(line):
    line_points = 0
    for elem in reversed(line):
        opp_elem = left_dict[elem]
        line_points = line_points * 5 + right_dict_vals[opp_elem]

    return line_points


for line in incomplete_lines:
    list_of_points.append(get_line_points(line))

print(statistics.median(list_of_points))

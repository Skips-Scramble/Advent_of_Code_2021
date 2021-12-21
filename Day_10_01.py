import re
from collections import Counter

input_file = open(
    "H:\Personal\PRM\SkipsScramble_Repo\Advent_of_Code_2021\input_10_sample.txt"
)
input = input_file.read().splitlines()

right_dict = {")": "(", "]": "[", "}": "{", ">": "<"}

left_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}

# Let's just stip pairs successively

line_init = input[2]

line_frozen = ""
line = line_init

more_pairs = True
illegal_items = []

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
            # print("Your first incorrect item is {}".format(right_chars[0]))
            if right_chars != []:
                illegal_items.append(right_chars[0])
            break

count_dict = dict(Counter(illegal_items).items())

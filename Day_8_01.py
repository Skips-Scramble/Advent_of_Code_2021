input_file = open("input_08.txt")
input = input_file.read().splitlines()

signals_last = [x.split("| ")[1] for x in input]

unique_lengths_dict = {2: 1, 3: 7, 4: 4, 7: 8}

numbers = []

for item in signals_last:
    sep_list = item.split(" ")
    for part in sep_list:
        if len(part) in {2, 3, 4, 7}:
            numbers.append(unique_lengths_dict[len(part)])


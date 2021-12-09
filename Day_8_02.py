input_file = open("input_08.txt")
input = input_file.read().splitlines()

signals_last = [x.split("| ")[1] for x in input]
signals_first = [x.split(" |")[0] for x in input]

unique_lengths_dict = {2: 1, 3: 7, 4: 4, 7: 8}

numbers = []

for item in signals_last:
    sep_list = item.split(" ")
    for part in sep_list:
        if len(part) in {2, 3, 4, 7}:
            numbers.append(unique_lengths_dict[len(part)])


scrambled = signals_first[0].split(" ")
scrambled_set = [{char for char in word} for word in scrambled]
leftover_numb_list = scrambled_set.copy()

numb_dict = {}
piece_dict = {}

# Find the 1, the 4 , the 7 and the 8
for item in scrambled_set:
    # print(item)
    if len(item) == 2:
        numb_dict[1] = item
        leftover_numb_list.remove(item)
    elif len(item) == 4:
        numb_dict[4] = item
        leftover_numb_list.remove(item)
    elif len(item) == 3:
        numb_dict[7] = item
        leftover_numb_list.remove(item)
    elif len(item) == 7:
        numb_dict[8] = item
        leftover_numb_list.remove(item)

# Find the number 9
for item in leftover_numb_list:
    if len(item) == 6 and len(item.strip(numb_dict[4])) == 2:
        print(item)

piece_dict[1] = numb_dict[7].strip(numb_dict[1])


input_file = open("input_08.txt")
input = input_file.read().splitlines()

signals_last = [x.split("| ")[1] for x in input]
signals_first = [x.split(" |")[0] for x in input]

scrambled = signals_first[0].split(" ")
scrambled_set = [{char for char in word} for word in scrambled]
leftover_numb_list = scrambled_set.copy()

numb_dict = {}
piece_dict = {}

# Find the 1, 4, 7 and 8
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
    if len(item) == 6:
        test_set = {x for x in item if x not in numb_dict[4]}
        if len(test_set) == 2:
            numb_dict[9] = item

# Find first piece and 7th piece
piece_dict[1] = {x for x in numb_dict[7] if x not in numb_dict[1]}
piece_dict[7] = {
    x for x in numb_dict[9] if x not in numb_dict[4] and x not in numb_dict[7]
}

piece_dict[1] = numb_dict[7].strip(numb_dict[1])


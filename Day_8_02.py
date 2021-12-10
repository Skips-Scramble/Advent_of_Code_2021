input_file = open("input_08.txt")
input = input_file.read().splitlines()

signals_first = [x.split(" |")[0] for x in input]
signals_second = [x.split("| ")[1] for x in input]

def doittoit(first, second):
    scrambled = first.split(" ")
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
                leftover_numb_list.remove(item)

    # Find 1st piece, 7th piece, 5th piece
    piece_dict[1] = [x for x in numb_dict[7] if x not in numb_dict[1]][0]
    piece_dict[7] = [
        x for x in numb_dict[9] if x not in numb_dict[4] and x not in numb_dict[7]
    ][0]
    piece_dict[5] = [x for x in numb_dict[8] if x not in numb_dict[9]][0]

    # Find number 2
    for item in leftover_numb_list:
        if len(item) == 5 and piece_dict[5] in item:
            numb_dict[2] = item
            leftover_numb_list.remove(item)

    # Find piece 3
    piece_dict[3] = [x for x in numb_dict[1] if x in numb_dict[2]][0]

    # Find piece 6
    piece_dict[6] = [x for x in numb_dict[1] if x != piece_dict[3]][0]

    # Find number 6
    for item in leftover_numb_list:
        if len(item) == 6:
            if piece_dict[3] not in item:
                numb_dict[6] = item
                leftover_numb_list.remove(item)

    # Find number 0
    for item in leftover_numb_list:
        if len(item) == 6:
            numb_dict[0] = item
            leftover_numb_list.remove(item)

    # Find piece 4
    piece_dict[4] = [x for x in numb_dict[6] if x not in numb_dict[0]][0]

    # Find number 3
    for item in leftover_numb_list:
        if piece_dict[3] in item:
            numb_dict[3] = item
            leftover_numb_list.remove(item)

    # Find number 5
    numb_dict[5] = leftover_numb_list[0]
    leftover_numb_list.remove(leftover_numb_list[0])

    # Find piece 2
    piece_dict[2] = [x for x in numb_dict[5] if x not in numb_dict[3]][0]

    scrambled_second = second.split(" ")
    scrambled_set_second = [{char for char in word} for word in scrambled_second]
    print("scrambled_second is {}".format(scrambled_second))
    print("scrambled_set_second is {}".format(scrambled_set_second))
 
    key_list = list(numb_dict.keys())
    print("key_list is {}".format(key_list))
    val_list = list(numb_dict.values())
    print("val_list is {}".format(val_list))

    number = ""
    for item in scrambled_set_second:
        pos = val_list.index(item)
        number_val = key_list[pos]
        number = number + str(number_val)
    
    return(int(number))

full_sum = 0
for i in range(len(input)):
    full_sum = full_sum + doittoit(signals_first[i], signals_second[i])

print(full_sum)



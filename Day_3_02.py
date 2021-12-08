with open("input_03_01.txt") as file:
    input = [x for x in file.readlines()]

column_dict = {}
gamma_str = ""
epsilon_str = ""
input_w_deletions = input

for i in range(len(input_w_deletions[0])-1):
    col_count = 0
    for item in input_w_deletions:
        the_numb = item[i]
        if the_numb == "1":
            col_count = col_count + 1
        else:
            col_count = col_count - 1
        if col_count < 0:
            column_dict[str(i)] = "0"
        else:
            column_dict[str(i)] = "1"



        

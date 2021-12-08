with open("input_03_01.txt") as file:
    input = [x for x in file.readlines()]

column_dict = {}
gamma_str = ""
epsilon_str = ""

for i in range(len(input[0])-1):
    col_count = 0
    for item in input:
        the_numb = item[i]
        if the_numb == "1":
            col_count = col_count + 1
        else:
            col_count = col_count - 1
        if col_count < 0:
            column_dict[str(i)] = ["0","1"]
        else:
            column_dict[str(i)] = ["1","0"]
    gamma_str = gamma_str + column_dict[str(i)][0]
    epsilon_str = epsilon_str + column_dict[str(i)][1]

gamma = int(gamma_str,2)
epsilon = int(epsilon_str,2)

print(gamma * epsilon)

        

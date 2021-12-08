
input_file = open("input_07.txt")
input = input_file.read().splitlines()

init_depths = [int(x) for x in input[0].split(",")]

max_y = max(test)
min_y = min(test)

def fuel_count(target):
    fuel = 0
    for item in init_depths:
        fuel = fuel + abs(item - target)
    return fuel

# Do something where you will go higher or lower as your guesses change

min_fuel = (max_y - min_y) * len(init_depths)

for i in range(min_y, max_y):
    fuel_count_i = fuel_count(i)
    if fuel_count_i < min_fuel:
        min_fuel = fuel_count_i
    

    


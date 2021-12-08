from collections import Counter

with open("input_06.txt") as file:
    input = [x for x in file.readlines()]

my_list = list(map(int, input[0].split(",")))

def count_from_start(fish_list):
    for i in range(1,81):
        for j in range(len(fish_list)):
            fish_list[j] = fish_list[j] - 1
            if fish_list[j] < 0:
                fish_list[j] = 6
                fish_list.append(8)
        #print(fish_list)
        #print("After day {}, there are {} fish".format(i, len(fish_list)))
    return len(fish_list)

from_1 = count_from_start([1])
from_2 = count_from_start([2])
from_3 = count_from_start([3])
from_4 = count_from_start([4])
from_5 = count_from_start([5])

first_fish = Counter(my_list)

total_fish = (from_1 * first_fish[1] + 
              from_2 * first_fish[2] + 
              from_3 * first_fish[3] + 
              from_4 * first_fish[4] + 
              from_5 * first_fish[5]
)

print(total_fish)

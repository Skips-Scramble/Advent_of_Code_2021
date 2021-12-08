from collections import Counter

with open("input_06.txt") as file:
    input = [x for x in file.readlines()]

my_list = list(map(int, input[0].split(",")))

def count_from_start(fish_list):
    for i in range(1,129):
        for j in range(len(fish_list)):
            fish_list[j] = fish_list[j] - 1
            if fish_list[j] < 0:
                fish_list[j] = 6
                fish_list.append(8)
        #print(fish_list)
        #print("After day {}, there are {} fish".format(i, len(fish_list)))
    return len(fish_list), fish_list

list_after_128_1 = count_from_start([1])[1]
list_after_128_2 = count_from_start([2])[1]
list_after_128_3 = count_from_start([3])[1]
list_after_128_4 = count_from_start([4])[1]
list_after_128_5 = count_from_start([5])[1]

initial_fish = Counter(my_list)

list_after_128 = (
    list_after_128_1 * initial_fish[1] + 
    list_after_128_2 * initial_fish[2] + 
    list_after_128_3 * initial_fish[3] + 
    list_after_128_4 * initial_fish[4] + 
    list_after_128_5 * initial_fish[5]
)

from_0 = count_from_start([0])[0]
from_1 = count_from_start([1])[0]
from_2 = count_from_start([2])[0]
from_3 = count_from_start([3])[0]
from_4 = count_from_start([4])[0]
from_5 = count_from_start([5])[0]
from_6 = count_from_start([6])[0]
from_7 = count_from_start([7])[0]
from_8 = count_from_start([8])[0]

first_fish = Counter(list_after_128)

total_fish = (from_0 * first_fish[0] +
              from_1 * first_fish[1] + 
              from_2 * first_fish[2] + 
              from_3 * first_fish[3] + 
              from_4 * first_fish[4] + 
              from_5 * first_fish[5] +
              from_6 * first_fish[6] +
              from_7 * first_fish[7] +
              from_8 * first_fish[8]
)

print(total_fish)

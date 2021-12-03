
with open("input_01_01.txt") as file:
    depth_list = [int(x) for x in file.read().split()]

increase_count = 0
for index, depth in enumerate(depth_list):
    if index == len(depth_list)-1:
        continue
    elif depth_list[index + 1] > depth_list[index]:
        increase_count += 1

print(increase_count)

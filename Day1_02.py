
with open("input_01_01.txt") as file:
    depth_list = [int(x) for x in file.read().split()]

increase_count = 0
for index, depth in enumerate(depth_list):
    if index > len(depth_list)-4:
        continue
    else:
        print(index)
        sum_a = depth_list[index] + depth_list[index + 1] + depth_list[index + 2]
        sum_b = depth_list[index + 1] + depth_list[index + 2] + depth_list[index + 3]
        if sum_b > sum_a:
            increase_count += 1

print(increase_count)

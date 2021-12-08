
input_file = open("input_02_01.txt")
directions = input_file.read().splitlines()

forward = 0
aim = 0
depth = 0

for item in directions:
    if "forward" in item:
        forward = forward + int(item.strip("forward "))
        depth = depth + aim * int(item.strip("forward "))
    elif "up" in item:
        aim = aim - int(item.strip("up "))
    else:
        aim = aim + int(item.strip("down "))


print(forward)
print(depth)
print(forward * depth)
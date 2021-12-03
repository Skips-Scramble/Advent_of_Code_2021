
input_file = open("input_02_01.txt")
directions = input_file.read().splitlines()

directions.sort()

forward = []
updown = []

for item in directions:
    if "forward" in item:
        forward.append(int(item.strip("forward ")))
    elif "up" in item:
         updown.append(-int(item.strip("up ")))
    else:
        updown.append(int(item.strip("down")))

print(sum(forward))
print(sum(updown))
print(sum(forward)*sum(updown))
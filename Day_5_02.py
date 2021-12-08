import re
from collections import Counter

with open("input_05.txt") as file:
    input = [x[:-1] for x in file.readlines()]

test_regex = re.compile(r'(\d+,\d+) -> (\d+,\d+)')
mo = test_regex.search(input[0])

line_segs = []

vert_points = []
horiz_points = []
diag_points = []

for item in input: #This works, so don't want to mess with it
    line_seg_comp = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    line_seg_search = line_seg_comp.search(item)

    if (
        line_seg_search.group(1) == line_seg_search.group(3)
    ):
        sm_y = min(int(line_seg_search.group(2)), int(line_seg_search.group(4)))
        lg_y = max(int(line_seg_search.group(2)), int(line_seg_search.group(4)))
        
        for i in range(lg_y - sm_y + 1):
            vert_points.append((
                int(line_seg_search.group(1)),
                sm_y + i,
            ))
    
    if (
        line_seg_search.group(2) == line_seg_search.group(4)
    ):
        sm_x = min(int(line_seg_search.group(1)), int(line_seg_search.group(3)))
        lg_x = max(int(line_seg_search.group(1)), int(line_seg_search.group(3)))
        
        for i in range(lg_x - sm_x + 1):
            horiz_points.append((
                sm_x + i,
                int(line_seg_search.group(2))
            ))

        
    try: 
        if (    
            (int(line_seg_search.group(4)) - int(line_seg_search.group(2))) / (int(line_seg_search.group(3)) - int(line_seg_search.group(1))) == 1
            or
            (int(line_seg_search.group(4)) - int(line_seg_search.group(2))) / (int(line_seg_search.group(3)) - int(line_seg_search.group(1))) == -1

        ):
            slope = (int(line_seg_search.group(4)) - int(line_seg_search.group(2))) / (int(line_seg_search.group(3)) - int(line_seg_search.group(1)))
            sm_x = min(int(line_seg_search.group(1)), int(line_seg_search.group(3)))
            lg_x = max(int(line_seg_search.group(1)), int(line_seg_search.group(3)))
            sm_y = min(int(line_seg_search.group(2)), int(line_seg_search.group(4)))
            if sm_y == int(line_seg_search.group(2)):
                start_x = int(line_seg_search.group(1))
            else:
                start_x = int(line_seg_search.group(3))
            
            for i in range(lg_x - sm_x + 1):
                diag_points.append((
                    start_x + int(i*slope),
                    sm_y + i
                ))

    except ZeroDivisionError:
        pass

my_points = vert_points + horiz_points + diag_points

multi_pt = set()

for index, item in enumerate(my_points):
    if my_points[index:].count(item) > 1:
        multi_pt.add(item)

print(len(multi_pt))









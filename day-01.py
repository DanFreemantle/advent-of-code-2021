# Advent of Code 2021
# Day 01
# Part 01

result = 0

#Load sonar sweeps into an array
with open('inputs/day-01.txt', 'r') as sonar_sweeps:
    depths = [int(depth) for depth in sonar_sweeps]

# Compare depths
for depth1, depth2 in zip(depths, depths[1:]):
    result += int(depth2 > depth1)

print(result)
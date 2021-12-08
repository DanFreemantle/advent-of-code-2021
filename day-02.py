# Advent of Code 2021
# Day 02
# Part 01

position = 0
depth = 0

#Load submarine sweeps into an array
with open('inputs/day-02.txt', 'r') as submarine_commands:
    commands = [command.strip().split(" ") for command in submarine_commands]

# Parse commands
for command in commands:
    if command[0] == 'forward':
        position += int(command[1])
    if command[0] == 'up':
        depth -= int(command[1])
    if command[0] == 'down':
        depth += int(command[1])

print(position * depth)
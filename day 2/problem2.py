horizontal_sum = 0
depth_sum = 0
aim_sum = 0
lines = []

# Read the input
print('enter the values')
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

# Calculate the sum of the horizontal and depth
for line in lines:
    line = line.split()
    if line[0] == 'forward':
        horizontal_sum += int(line[1])
        depth_sum += int(line[1]) * aim_sum
    elif line[0] == 'up':
        aim_sum -= int(line[1])
    elif line[0] == 'down':
        aim_sum += int(line[1])

print("horizontal_sum:", horizontal_sum)
print("depth_sum:", depth_sum)
print("multiplied_sum:", horizontal_sum * depth_sum)
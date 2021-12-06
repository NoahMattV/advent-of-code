print('enter the values')
lines = []
times_increased = 0
previous_sum = 0

# Read the input
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

# Calculate the sum
for i in range(len(lines)):
    j = i + 3
    if j > len(lines):
        break
    else:
        sum = 0
        for k in range(i, j):
            sum += int(lines[k])
        print (int(lines[i]), "+", int(lines[i+1]), "+", int(lines[i+2]), "=", sum)
        if sum > previous_sum:
            times_increased += 1
        previous_sum = sum
    

print('times increased:', times_increased - 1)

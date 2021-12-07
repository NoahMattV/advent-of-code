lines = []
values = []
# binary values
gamma = 0b00000
epsilon = 0b00000

# Read the input
print('enter the values')
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break


# Convert the input to individual bits 
values = [int(x) for x in lines]
for i in range(len(lines)):
    values[i] = [int(x) for x in str(lines[i])]

g = []
e = []
for i in range(len(values[0])):
    ones = 0
    zeros = 0

    for j in range(len(values)):
        if values[j][i] == 1:
            ones += 1
        else:
            zeros += 1
    if ones >= zeros:
        g.append(1)
        e.append(0)
    else:
        g.append(0)
        e.append(1)

gamma = [str(gs) for gs in g]
gamma = ''.join(gamma)
gamma = int(gamma,2)
print('gamma = ',gamma)

epsilon = [str(es) for es in e]
epsilon = ''.join(epsilon)
epsilon = int(epsilon,2)
print('epsilon = ',epsilon)

# Multiply and print result as decimal
print ("result = ",gamma * epsilon)


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

def saveValuesWithBitInPosition(values, position, bit):
    result = []
    for j in range(len(values)):
        if values[j][position] == bit:
            result.append(values[j])
    return result

oxygen = [] # value with most common bits in each position
c02 = []   # value with least common bits in each position
def findMostCommonAndLeastCommon(values, mostCommon):
    for i in range(len(values[0])):
        ones = 0
        zeros = 0

        for j in range(len(values)):
            if len(values) == 1:
                return values
            # print('current values: ', values)
            if values[j][i] == 1:
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            # place the values with this bit into the final list
            if mostCommon == True:
                values = saveValuesWithBitInPosition(values, i, 1)
            else:
                values = saveValuesWithBitInPosition(values, i, 0)
            #c02 = saveValuesWithBitInPosition(values, i, 0)
        else:
            if mostCommon == True:
                values = saveValuesWithBitInPosition(values, i, 0)
            else:
                values = saveValuesWithBitInPosition(values, i, 1)
            #c02 = saveValuesWithBitInPosition(values, i, 1)
    return values

print('finding oxygen')
oxygen = findMostCommonAndLeastCommon(values, True)
print('finding c02')
c02 = findMostCommonAndLeastCommon(values, False)

print('oxygen = ',oxygen)
print('c02 = ',c02)

o = int(''.join(str(x) for x in oxygen[0]), 2)
c = int(''.join(str(x) for x in c02[0]), 2)
# Multiply and print result as decimal
print ("result = ",o * c)


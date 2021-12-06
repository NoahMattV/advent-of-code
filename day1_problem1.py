print('enter the values')
lines = []
times_increased = 0
previous_value = 0

while True:
    line = input()
    if line:
        lines.append(line)
        if int(line) > previous_value:
            times_increased += 1
        previous_value = int(line)
    else:
        break
print('times increased:', times_increased - 1)

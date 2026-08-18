#2:23:04

# The continue statement ens the current iteration and jumps to the 
# top of the loop and starts the next iteration.

while True:
    line = input('>')
    if line[0] == '#' :
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

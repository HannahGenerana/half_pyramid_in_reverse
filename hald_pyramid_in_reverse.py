# Print a downward Half-Pyramid Pattern of Star (asterisk)

# pseudocode

# create while loop with a condition of a variable is greater than or equal to another variable
tree = 1
line_asterisk = 10

while line_asterisk >= tree:

# create a line of asterisk
    for i in range (line_asterisk):
        print ('*',end='')

# subtract the value of the variable that create a line of asterisk from 1 to reduce the value it will print
    line_asterisk = line_asterisk - 1

# make an empty print to start the next print at a new line
    print ("")
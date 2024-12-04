
# Get dimensions

# Read file in
fileContent = ""
with open('day_4_part_1_input.txt') as file:
    fileContent = file.read()
fileContent = fileContent.strip()

# Find the number of lines
data = fileContent.split("\n")
numberOfLines = len(data)

# Find the length of a line
lineLength = len(list(data[0]))

# Get the data into a 2D list
for i in range(numberOfLines):
    data[i] = data[i].strip()
    data[i] = list(data[i])
    
#for i in range(numberOfLines):
#    for j in range(lineLength):
#        print (data[i][j], end='')
#    print ("")

# Find all the XMAS
counter = 0
for i in range(numberOfLines):
    for j in range(lineLength):
        # Right
        if (j < (lineLength-3)):
            if data[i][j] == 'X':
                if data[i][j+1] == 'M':
                    if data[i][j+2] == 'A':
                        if data[i][j+3] == 'S':
                            counter += 1
        # Left
        if (j > 2):
            if data[i][j] == 'X':
                if data[i][j-1] == 'M':
                    if data[i][j-2] == 'A':
                        if data[i][j-3] == 'S':
                            counter += 1
        # Up
        if (i > 2):
            if data[i][j] == 'X':
                if data[i-1][j] == 'M':
                    if data[i-2][j] == 'A':
                        if data[i-3][j] == 'S':
                            counter += 1
        # Down
        if (i < (numberOfLines-3)):
            if data[i][j] == 'X':
                if data[i+1][j] == 'M':
                    if data[i+2][j] == 'A':
                        if data[i+3][j] == 'S':
                            counter += 1
        # Diagonal down and right
        if (j < (lineLength-3)):
            if (i < (numberOfLines-3)):
                if data[i][j] == 'X':
                    if data[i+1][j+1] == 'M':
                        if data[i+2][j+2] == 'A':
                            if data[i+3][j+3] == 'S':
                                counter += 1
        # Diagonal down and left
        if (j > 2):
            if (i < (numberOfLines-3)):
                if data[i][j] == 'X':
                    if data[i+1][j-1] == 'M':
                        if data[i+2][j-2] == 'A':
                            if data[i+3][j-3] == 'S':
                                counter += 1
        # Diagonal up and left
        if (j > 2):
            if (i > 2):
                if data[i][j] == 'X':
                    if data[i-1][j-1] == 'M':
                        if data[i-2][j-2] == 'A':
                            if data[i-3][j-3] == 'S':
                                counter += 1
        # Diagonal up and right
        if (j < (lineLength-3)):
            if (i > 2):
                if data[i][j] == 'X':
                    if data[i-1][j+1] == 'M':
                        if data[i-2][j+2] == 'A':
                            if data[i-3][j+3] == 'S':
                                counter += 1

print ("Total: "+str(counter))
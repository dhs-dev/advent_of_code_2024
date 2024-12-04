
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

# Find all the MAS X's
counter = 0
for i in range(numberOfLines):
    for j in range(lineLength):
        
        # Find A's not on the edge
        if data[i][j] == 'A':
            if 0 < i < (numberOfLines-1):
                if 0 < j < (lineLength-1):
                    
                    # M..
                    # .A. 
                    # ..S
                    if (data[i-1][j-1] == 'M'):
                        if (data[i+1][j+1] == 'S'):
                            # M.S
                            # .A. 
                            # M.S
                            if (data[i+1][j-1] == 'M'):
                                if (data[i-1][j+1] == 'S'):
                                    counter +=1
                            # M.M
                            # .A. 
                            # S.S
                            if (data[i+1][j-1] == 'S'):
                                if (data[i-1][j+1] == 'M'):
                                    counter +=1
                    
                    # S..
                    # .A. 
                    # ..M
                    if (data[i-1][j-1] == 'S'):
                        if (data[i+1][j+1] == 'M'):
                            # S.S
                            # .A. 
                            # M.M
                            if (data[i+1][j-1] == 'M'):
                                if (data[i-1][j+1] == 'S'):
                                    counter +=1
                            # S.M
                            # .A. 
                            # S.M
                            if (data[i+1][j-1] == 'S'):
                                if (data[i-1][j+1] == 'M'):
                                    counter +=1

print ("Total: "+str(counter))
import re

# Read file in
fileContent = ""
with open('day_3_part_1_input.txt') as file:
    fileContent = file.read()

# Find the mul(x,x) operations
operations = re.findall( r'mul\(\d{1,3},\d{1,3}\)', fileContent)

# Sum all the multiplication results
runningTotal = 0
for multiplication in operations:
    numbers = re.findall(r'\d+', multiplication)
    runningTotal += int(numbers[0]) * int(numbers[1])

print("Final sum: "+str(runningTotal))
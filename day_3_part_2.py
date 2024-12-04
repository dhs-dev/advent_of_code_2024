import re

# Get sections from string that are contained within strings
def extractSections(content, startString, endString):
    sections = []
    startPosition = 0
    while True:
        startPosition = content.find(startString, startPosition)
        if startPosition == -1:
            break
        endPosition = content.find(endString, startPosition + len(startString))
        if endPosition == -1:
            break
        sections.append(content[startPosition:endPosition + len(endString)])
        startPosition = endPosition + len(endString)
    
    return sections

# Read file in
fileContent = ""
with open('day_3_part_1_input.txt') as file:
    fileContent = file.read()

# Start with mul's enabled
fileContent = "do()"+fileContent+"don't()"

fileContentAbridged = extractSections(fileContent, "do()", "don't()")

fileContentAbridged = ''.join(fileContentAbridged)

# Find the mul(x,x) operations
operations = re.findall( r'mul\(\d{1,3},\d{1,3}\)', fileContentAbridged)

# Sum all the multiplication results
runningTotal = 0
for multiplication in operations:
    numbers = re.findall(r'\d+', multiplication)
    runningTotal += int(numbers[0]) * int(numbers[1])

print("Final sum: "+str(runningTotal))
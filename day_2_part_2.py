
# Apply checks to the input list, return True/False
def perform_checks(inputList):
    safe = True
    positiveDifference = False
    negativeDifference = False
    for i in range(len(inputList)-1):
        # Check for differing by 1-3
        difference = inputList[i+1] - inputList[i]
        if (difference == 0) or (abs(difference) > 3):
            safe = False
        # Check that difference is always positive, or always negative
        if difference > 0:
            positiveDifference = True
        if difference < 0:
            negativeDifference = True   
    if positiveDifference and negativeDifference:
        safe = False
    return safe;

# Main
with open('day_2_part_1_input.txt') as file:
    
    # Counter for the number of safe reports
    numberofSafeReports = 0
    
    # Iterate over each line in the file
    for line in file:
        
        if line.strip() != "":
        
            # Get the list of numbers from the line
            line = line.strip()
            lineParts = line.split(' ')
            for i in range(len(lineParts)):
                lineParts[i] = int(lineParts[i])
        
            # Apply checks to the line
            safe = perform_checks(lineParts)

            # Count the line if it's safe, or re-check with removing numbers if it's not
            if safe:
                numberofSafeReports += 1
            else:
                # Try removing one number at a time and re-checking
                canBeMadeSafe = False
                for i in range(len(lineParts)):
                    newList = lineParts.copy()
                    del newList[i]
                    newSafe = perform_checks(newList)
                    if newSafe:
                        canBeMadeSafe = True
                if canBeMadeSafe:
                    numberofSafeReports += 1
        
    print ("Number of safe reports: "+str(numberofSafeReports))
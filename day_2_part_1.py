
with open('day_2_part_1_input.txt') as file:
    
    # Counter for the number of safe reports
    numberofSafeReports = 0
    
    # Iterate over each line in the file
    for line in file:
        
        # Get the list of numbers from the line
        line = line.strip()
        lineParts = line.split(' ')
        for i in range(len(lineParts)):
            lineParts[i] = int(lineParts[i])
    
        # Apply checks to the line
        safe = True
        positiveDifference = False
        negativeDifference = False
        for i in range(len(lineParts)-1):
            # Check for differing by 1-3
            difference = lineParts[i+1] - lineParts[i]
            if (difference == 0) or (abs(difference) > 3):
                safe = False
            # Check that difference is always positive, or always negative
            if difference > 0:
                positiveDifference = True
            if difference < 0:
                negativeDifference = True   
        if positiveDifference and negativeDifference:
            safe = False

        if safe:
            numberofSafeReports += 1
        
    print ("Number of safe reports: "+str(numberofSafeReports))
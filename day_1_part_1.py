
list1 = []
list2 = []

with open('day_1_part_1_input.txt') as file:
    
    # Get the two lists of numbers
    for line in file:
        line = line.strip()
        lineParts = line.split('   ')
        list1.append(int(lineParts[0]))
        list2.append(int(lineParts[1]))
    
    # Sort the two lists of numbers
    list1.sort() 
    list2.sort() 
    
    # Calculate the total difference between each pair of numbers
    totalDifference = 0
    for i in range(len(list1)):
        totalDifference += abs(list2[i] - list1[i])
        
    print (totalDifference)
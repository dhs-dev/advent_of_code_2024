
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
    
    # Calculate the similarity
    totalSimilarity = 0
    for i in range(len(list1)):
        counter = 0
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                counter += 1
        totalSimilarity += list1[i] * counter
        
    print (totalSimilarity)
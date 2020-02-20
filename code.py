def solve(Max, Input):

    IndexLIst = []         # To store the best solution indexes through out the solution generating
    ValueList = []         # To store the best solution values through out the solution generating
    CurrentList = []       # To store the current solution indexes through out the solution generating
    CurrentValue = []      # To store the current solution values through out the solution generating

    fullSize = len(Input)
    MaxScore = 0 
    startIndex = fullSize
    sum = 0
    while((len(CurrentList) > 0 and CurrentList[0] != 0) or len(CurrentList) == 0):
        startIndex = startIndex - 1 
        for i in range(startIndex, -1, -1): # Used to traverse from end to start of the inputList
            currentValue = Input[i]
            TempSum = sum + currentValue 
            if (TempSum == Max):  # If the temporary sum is equal to target that means the perfect solution is found
                sum = TempSum
                CurrentList.append(i) # Add current Pizza index to the solution
                CurrentValue.append(currentValue) # Add current Pizza value to the solution
                break  # Go to return solution
            elif (TempSum > Max):  # If the temporary sum is greter than target
                continue  # Try next value
            elif (TempSum < Max):  # If the temporary sum is lesser than target
                sum = TempSum
                CurrentList.append(i) # Add current Pizza index to the solution
                CurrentValue.append(currentValue) # Add current Pizza value to the solution
                continue  # Try next value
        if (MaxScore < sum):  # If currently generated solution has the best score
            MaxScore = sum  # Save its value

            IndexLIst = []
            ValueList = []
            for y in CurrentList:
                IndexLIst.append(y)  # Save the currently best solution indexes
            for y in CurrentValue:
                ValueList.append(y)  # Save the currently best solution values
        if (MaxScore == Max):  # If current solution is the perfect solution
            break # Stop solution generating
        if(len(CurrentValue) != 0):
            lastVal = CurrentValue.pop() # Remove the last element from current values
            sum = sum - lastVal # Subtract it from sum
        if(len(CurrentList) != 0):
            lastIndex = CurrentList.pop() # Remove the last element from current indexes
            startIndex = lastIndex # Make it as the starting index for the next iteration
        if(len(CurrentList) == 0 and (startIndex == 0)): # If solution generating is almost finished
            break # Stop solution generating
    print("SCORE = " + str(MaxScore))     # Print the score of the best solution
    return IndexLIst  # Return indexes list of the best solution
def process(fileName):
     # Print data to console
    print("")
    print("-----------------------")
    print(fileName)
    print("-----------------------")
    #  Read the open file by name
    inputFile = open(fileName + ".in", "rt")
    #  Read file
    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()
    #  Print input data
    print("INPUT")
    print(firstLine)
    print(secondLine)
    #  Assign parameters
    Max, Num = list(map(int, firstLine.split()))
    # Create the pizza list by reading the file
    inputList = list(map(int, secondLine.split()))
    outputList = solve(Max, inputList)  # Solve the problem and get output
     #  Print output data and create output file
    print("")
    print("OUTPUT")
    print(len(outputList))
    outputString = ""
    for l in outputList:
        outputString = outputString + str(l) + " "
    print(outputString)
    outputFile = open(fileName + ".out", "w")
    outputFile.write(str(len(outputList)) + "\n")
    outputFile.write(outputString)
    outputFile.close()
fileNames = ["a_example", "b_small", "c_medium",
             "d_quite_big", "e_also_big"]  # File names

for fileName in fileNames:  # Take each and every file and solve
    process(fileName)
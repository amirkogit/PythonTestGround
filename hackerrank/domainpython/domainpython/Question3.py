def ReadInput ():
    stopCriteria = ""
    data = []
    while True:
        line = raw_input()
        if line.strip() == stopCriteria:
            break
        data.append(line)
    return data

def ProcessInputs(data):
    dataSize = len(data)

    textCaseNum = int(data[0])

    inputTextList = []
    phraseList = []
    for i in range(1,dataSize,2):
        inputTextList.append(data[i])
        phraseList.append(data[i+1].split())

    return textCaseNum, inputTextList, phraseList

def CalculateCost(startIndices,stopIndices,textLength):
    ranges = []
    totalCost = 0
    # Create ranges
    for i in range(len(startIndices)):
        ranges.append(range(startIndices[i], stopIndices[i]+1))
   
    # Calculate costs for deletions
    for i in range(textLength):
        check = False
        for j in range(len(ranges)):
            if i in ranges[j]:
                check = True
                break
        if not (check):
            totalCost += 1
    
    # Calculate cost of insertion
    for i in range(len(startIndices)-1):
        if startIndices[i+1] <= stopIndices[i]:
            totalCost += stopIndices[i] - startIndices[i+1] + 1
        
    # Insert spaces is just one less than number of words
    totalCost += len(startIndices)- 1
    print totalCost
    print ""
    return totalCost 

def FindPhrase(textCaseNum, inputTextList, phraseList):
    for i in range(textCaseNum):
        startIndices=[]
        stopIndices=[]
        print i, phraseList[i]
        phrase = phraseList[i]
        for word in phrase:
            index = inputTextList[i].find(word)
            if (index == -1):
                print "NO"
                print ""
                break
            else:
                startIndices.append(index)
                stopIndices.append(index+len(word)-1)
        print "YES"
        for j in (range(len(startIndices))):
            print phrase[j],startIndices[j],stopIndices[j],
        
        textLength = len(inputTextList[i])
        print ""
        CalculateCost(startIndices,stopIndices,textLength)
# Main
data = ReadInput()
textCaseNum, inputTextList, phraseList = ProcessInputs(data)
FindPhrase(textCaseNum, inputTextList, phraseList)


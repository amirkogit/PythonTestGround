import sys

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
         
    firstLine = data[0].split()
    # First row is number of entries and bucket Size
    numEntries = int(firstLine[0])
    bucketSize = int(firstLine[1])
     
    pointList = []
    lastIndex = 1
    for i in range(numEntries):
        point = [float(x) for x in data[i+lastIndex].split()]
        pointList.append(point)

    lastIndex += numEntries
    commandList = []
    for i in range(dataSize-lastIndex):
        commandList.append(data[i+lastIndex].split())
    
    return numEntries, bucketSize, pointList, commandList

def getKey(item):
    return item[3]

def InitializeBucket(numEntries,bucketSize,pointList):
    # Sort in decreasing order
    sortedPointList = sorted(pointList, key = getKey, reverse = True)
    bucket = []
    mainList = []
    for i in range(numEntries):
        point = ['%.1f'%x for x in sortedPointList[i]]
        point[0] = int(float(point[0]))
        if (i < bucketSize):
            bucket.append(point)
        else: 
            mainList.append(point)
    return bucket, mainList  

def FindWithinBucket(bucketContents,pointId):
    for i in range(len(bucketContents)):
        if (str(pointId) == str(bucketContents[i][0])):
            print pointId, "= (", bucketContents[i][1], ",", bucketContents[i][2], "," \
            ,bucketContents[i][3], ")"
            return 1
    
    print "Point doesn't exist in the bucket"
    return 0

def RemoveFromBucket(bucketContents,pointId,mainList):
    if len(mainList) == 0:
            print "No more points can be deleted"
            return bucketContents, mainList
    
    for i in range(len(bucketContents)):
        if (str(pointId) == str(bucketContents[i][0])):
            bucketContents.remove(bucketContents[i])
            if (len(mainList) > 0):
                bucketContents.append(mainList[0])
                mainList.remove(mainList[0])
            print "Point",pointId,"removed"
            return bucketContents, mainList
            
    print "Point doesn't exist in the bucket"
    return bucketContents, mainList

def ProcessQueries(commandList,bucketContents,mainList):
    numOfCommands = len(commandList)
    for i in range(numOfCommands):
        com = commandList[i][0]
        pointId = int(commandList[i][1])
        if (com == 'F' or com == 'f'):
            FindWithinBucket(bucketContents,pointId)
        elif (com == 'R' or com == 'r'):
            bucketContents, mainList = RemoveFromBucket(bucketContents,pointId,mainList)
        else: 
            print "Invalid query"

def ReadFile(fileName):
    fi = open(fileName, "r")
    data = fi.read().splitlines()
    return data

# Main
#data = ReadInput()
fileName = sys.argv
data = ReadFile(fileName[1])
numEntries, bucketSize, pointList, commandList = ProcessInputs(data)
bucketContents,mainList = InitializeBucket(numEntries, bucketSize, pointList)
ProcessQueries(commandList,bucketContents,mainList)

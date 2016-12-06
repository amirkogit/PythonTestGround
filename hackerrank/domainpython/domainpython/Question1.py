# Question 1
stopCriteria = ""
data = []
while True:
    line = raw_input()
    if line.strip() == stopCriteria:
        break
    else: 
        line = [int(x) for x in line.split()]
        data.append(line)

lengthArray = data[0][0]
A1 = data[1]
A2 = data[2]

differences = []
# Take differences between indices of unique numbers which appear in both arrays
for i in range(lengthArray):
    for j in range(lengthArray):
        if A1[i] == A2[j]:
            differences.append(abs(i - j))

# Take minimum index difference
minimumDifference = min(differences)

#Extract integers in which indices differences are minimum.
candidateSolutions = []
for i in range(lengthArray):
    if (minimumDifference == differences[i]):
        candidateSolutions.append(A1[i])

# Take smallest integer
solution = min(candidateSolutions)
print solution

#Things to remember/impression after completing this
#①Think of a nicer way to group in 3s (modulo?). A lot of lists right now

testList = []
testListTwo = []
sharedSum = 0

f = open("input.txt", "r")

#Part 1
for i in f:
    firstHalf = i[:len(i)//2]
    secondHalf = i[len(i)//2:]

    for j in firstHalf:
        if j in secondHalf:
            sameChar= j
                

    if sameChar.islower():
        sharedSum = sharedSum + (ord(sameChar)-96)
    else:
        sharedSum = sharedSum + (ord(sameChar)-38)

print("The shared sum is",sharedSum)

"""
#Part 2
#i[:-1] to get rid the of the new line, useful when looking for same character later
for i in f:
    testList.append(i[:-1])
    
for i in testList:
    try:
        for j in i:
            if j in testList[0] and j in testList[1] and j in testList[2]:
                if j == "\n":
                    sharedSum+=0
                elif j.islower():
                    sharedSum = sharedSum + (ord(j)-96)
    
                else:
                    sharedSum = sharedSum + (ord(j)-38)
                testList = testList[3:]
    except:
        pass
                    
print("The shared sum is",sharedSum)
"""

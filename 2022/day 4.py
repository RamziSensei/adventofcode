#Things of note
#① I'm happy with splitting the ranges. Not very readable, but looks cool and lots done on one line. Usually I'd throw a few more variables in for readable
#② Part 2 when quite smoothly!
#③ Should really code in a "nicer" way than just "Try" > "Except" out of range errors, but hey!
       
def PartOne():    
    try:
        while True:
            contained = True
            #Grabbing the lower and upper range values, and putting them and the numbers inbetween into a list
            rangeOne = list( range(int(testList[0].split(",")[0].split("-")[0]),int(testList[0].split(",")[0].split("-")[1])+1))
            rangeTwo = list(range(int(testList[0].split(",")[1].split("-")[0]),int(testList[0].split(",")[1].split("-")[1])+1))

            if len(rangeOne) <= len(rangeTwo):
                smallerRange = rangeOne
                biggerRange = rangeTwo
            else:
                smallerRange = rangeTwo
                biggerRange = rangeOne

            for i in smallerRange:
                if i in biggerRange:
                    continue
                else:
                    contained = False
                    
            if contained == True:
                counter += 1

            testList = testList[1:]
    except:
        print("Final count is",counter)


def PartTwo():
    testList = []
    smallerRange = []
    biggerRange = []
    checkingLoop = False
    counter = 0

    f = open("input.txt", "r")

    for i in f:
        if "\n" in i:
            testList.append(i[:-1])
        else:
            testList.append(i)

    print(testList)

    try:
        while True:
            contained = True
            #Grabbing the lower and upper range values, and putting them and the numbers inbetween into a list
            rangeOne = list( range(int(testList[0].split(",")[0].split("-")[0]),int(testList[0].split(",")[0].split("-")[1])+1))
            rangeTwo = list(range(int(testList[0].split(",")[1].split("-")[0]),int(testList[0].split(",")[1].split("-")[1])+1))

            if len(rangeOne) <= len(rangeTwo):
                smallerRange = rangeOne
                biggerRange = rangeTwo
            else:
                smallerRange = rangeTwo
                biggerRange = rangeOne

                
            for i in smallerRange:
                if i in biggerRange:
                    checkingLoop = True
            else:
                pass

            if checkingLoop == True:
                #print("overlap found")
                counter += 1
                checkingLoop = False

            testList = testList[1:]
            
            
    except:
        print("Final count is",counter)

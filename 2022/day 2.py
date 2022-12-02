#Things to remember/impression after completing this
#① str[-1] might look like the final character in a str, but can be a blank space /n...be careful! 
#② I like the win status string in I made in part 1...sadly it wasn't needed for 2!
#③ I would like a cleaner solution if I did this again, one that didn't use two separate blocks of code if possible
#④ I like how elements can be skipped at intervals with list[1::3]

f = open("input.txt", "r")
tempList= []

totalList = []
total= 0

#Part 1, Can also calculate who won and leave a string denoting who did
def Calculator(pointCalcStr):
    CPUScore = 0
    playerScore = 0
    result = ""
    
    #CPU picks Rock, and player picks...
    if pointCalcStr[0] == "A":
        CPUScore += 1
        if pointCalcStr[2] == "X":
            result = "DRAW"
            playerScore += 4
            CPUScore += 3
            
        elif pointCalcStr[2] == "Y":
            result = "PLAYW"
            playerScore+= 8

        else:
            result = "CPUW"
            playerScore+= 3
            CPUScore += 6


    #CPU picks Paper, and player picks...        
    elif pointCalcStr[0] == "B":
        CPUScore += 2
        if pointCalcStr[2] == "X":
            result = "CPUW"
            playerScore += 1
            CPUScore += 6
            
        elif pointCalcStr[2] == "Y":
            result = "DRAW"
            playerScore += 5
            CPUScore += 3

        else:
            result = "PLAYW"
            playerScore += 9


    #CPU picks Scissors, and player picks...    
    elif pointCalcStr[0] == "C":
        CPUScore += 3
        if pointCalcStr[2] == "X":
            result = "PLAYW"
            playerScore += 7
            
        elif pointCalcStr[2] == "Y":
            result = "CPUW"
            playerScore += 2
            CPUScore += 6

        else:
            result = "DRAW"
            playerScore += 6
            CPUScore += 3


    tempList.append(CPUScore)
    tempList.append(playerScore)
    
    if CPUScore > playerScore:
        tempList.append("CPUW")
    elif playerScore > CPUScore:
        tempList.append("PLAYW")
    else:
        tempList.append("DRAW")
    
    CPUScore = 0
    playerScore = 0

for i in f:
    Calculator(i)

print(sum(tempList[1::3]))

#########################

#Part 2

# X = Lose
# Y = Draw
# Z = Win

playerScore = 0

for pointCalcStr in f:

    #CPU picks Rock, and player...
    if pointCalcStr[0] == "A":
        if pointCalcStr[2] == "X":
            playerScore+= 3

        elif pointCalcStr[2] == "Y":
            playerScore+= 4

        else:
            playerScore+= 8


    #CPU picks Paper, and player...        
    elif pointCalcStr[0] == "B":
        if pointCalcStr[2] == "X":
            playerScore += 1
            
        elif pointCalcStr[2] == "Y":
            playerScore += 5

        else:
            playerScore += 9


    #CPU picks Scissors, and player...    
    elif pointCalcStr[0] == "C":
        if pointCalcStr[2] == "X":
            playerScore += 2
            
        elif pointCalcStr[2] == "Y":
            playerScore += 6

        else:
            playerScore += 7


print(playerScore)





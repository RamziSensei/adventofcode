#Things of note
#① Always be extremely careful manually copying down/converting things like the starting box state in this question
#② If I was to come back to this, I would make it much more readable and understandable by defining variables when referencing commandList and startList

f = open("input.txt", "r")
commandList = []

"""
    [M]             [Z]     [V]    
    [Z]     [P]     [L]     [Z] [J]
[S] [D]     [W]     [W]     [H] [Q]
[P] [V] [N] [D]     [P]     [C] [V]
[H] [B] [J] [V] [B] [M]     [N] [P]
[V] [F] [L] [Z] [C] [S] [P] [S] [G]
[F] [J] [M] [G] [R] [R] [H] [R] [L]
[G] [G] [G] [N] [V] [V] [T] [Q] [F]
 1   2   3   4   5   6   7   8   9
"""

startList = [ 
              ["G","F","V","H","P","S",],
              ["G","J","F","B","V","D","Z","M"],
              ["G","M","L","J","N"],
              ["N","G","Z","V","D","W","P"],
              ["V","R","C","B"],
              ["V","R","S","M","P","W","L","Z"],
              ["T","H","P"],
              ["Q","R","S","N","C","H","Z","V"],
              ["F","L","G","P","V","Q","J"]
              ]

def PartOne():
    #Checks first 3 numbers of list for relevant commands, carries them out on startList, deletes those 3 commands and moves on to the next until the list contains less than 3 values, in this case empty
    while len(commandList) >= 3:
        
        for i in range(int(commandList[0])):
            startList[int(commandList[2])-1].append(startList[int(commandList[1])-1].pop())

        commandList = commandList[3:]

def PartTwo():
    #CommandList[moveAmount, to, from]
    for i in f:
        commandList.append(i.split()[1])
        commandList.append(i.split()[3])
        commandList.append(i.split()[5])
    #print(commandList)
        
    while len(commandList) >= 3:
        counter = -int(commandList[0])
        
        while counter < 0:
            #print("moving",-counter,"from",commandList[1],"to",commandList[2])
            #print("appending",startList[int(commandList[1])-1][counter],"to",startList[int(commandList[2])-1])
            startList[int(commandList[2])-1].append(startList[int(commandList[1])-1].pop(counter))
            #print(startList)
            #print("counter was",counter)
            counter = counter + 1
            #print("counter is",counter)
        commandList = commandList[3:]

    #Print the top crate on each stack
    for i in startList:
        print(i[-1])

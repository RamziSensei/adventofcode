f = open("input.txt", "r")
listtemp=[]
totalList = []
total= 0

for x in f:
    try:
        listtemp.append(int(x))
    except:
        listtemp.append(x)

for i in listtemp:
    if i =="\n":
        totalList.append(total)
        total = 0
    else:
        total = total + i

totalList.sort(reverse=True)

print(totalList[0]+totalList[1]+totalList[2])
        

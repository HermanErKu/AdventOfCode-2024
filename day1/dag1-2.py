leftList = []
rightList = []

with open('dag1input.txt','r') as file:
    for line in file.readlines():
        leftList.append(int(line.split("   ")[0]))
        rightList.append(int(line.split("   ")[1]))


result = 0
for i in range(len(leftList)):
    leftNum = leftList[i]
    
    result += (rightList.count(leftNum)) * leftNum

print(result)
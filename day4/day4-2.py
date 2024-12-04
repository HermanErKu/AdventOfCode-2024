string = []

for i in range(5):
    stringToAppend = ""
    for i in range(145):
        stringToAppend += "."
    string.append([stringToAppend])

with open('input.txt','r') as file:
    for line in file.readlines():
        stringToAppend = ""
        stringToAppend += "..."
        for char in line:
            if char == "\n":
                stringToAppend += "..."
            stringToAppend += char
        string.append([stringToAppend])

for i in range(5):
    stringToAppend = ""
    for i in range(145):
        stringToAppend += "."
    string.append([stringToAppend])


sum = 0

for x in range(len(string)):
    for y in range(len(string[x][0])):
        if (string[x][0][y] == "A"):
            if ((string[x-1][0][y-1] == "M" and string[x-1][0][y+1] == "M") and (string[x+1][0][y-1] == "S" and string[x+1][0][y+1] == "S")):
                sum += 1
        
        if (string[x][0][y] == "A"):
            if ((string[x-1][0][y-1] == "S" and string[x-1][0][y+1] == "S") and (string[x+1][0][y-1] == "M" and string[x+1][0][y+1] == "M")):
                sum += 1
        
        if (string[x][0][y] == "A"):
            if ((string[x-1][0][y-1] == "M" and string[x-1][0][y+1] == "S") and (string[x+1][0][y-1] == "M" and string[x+1][0][y+1] == "S")):
                sum += 1

        if (string[x][0][y] == "A"):
            if ((string[x-1][0][y-1] == "S" and string[x-1][0][y+1] == "M") and (string[x+1][0][y-1] == "S" and string[x+1][0][y+1] == "M")):
                sum += 1

# [M][][M]
# [][A][]
# [S][][S]

# [S][][S]
# [][A][]
# [M][][M]

# [M][][S]
# [][A][]
# [M][][S]

# [S][][M]
# [][A][]
# [S][][M]

print(sum)
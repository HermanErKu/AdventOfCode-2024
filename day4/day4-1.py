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
        #vertical nested if :sob:
        if (string[x][0][y] == "X"):
            if (string[x][0][y+1] == "M"):
                if (string[x][0][y+2] == "A"):
                    if (string[x][0][y+3] == "S"):
                        sum += 1

        if (string[x][0][y] == "X"):
            if (string[x][0][y-1] == "M"):
                if (string[x][0][y-2] == "A"):
                    if (string[x][0][y-3] == "S"):
                        sum += 1
        

        #horizontal nested if
        if (string[x][0][y] == "X"):
            if (string[x+1][0][y] == "M"):
                if (string[x+2][0][y] == "A"):
                    if (string[x+3][0][y] == "S"):
                        sum += 1
        
        if (string[x][0][y] == "X"):
            if (string[x-1][0][y] == "M"):
                if (string[x-2][0][y] == "A"):
                    if (string[x-3][0][y] == "S"):
                        sum += 1
        


        #diagonal nested if
        if (string[x][0][y] == "X"):
            if (string[x+1][0][y+1] == "M"):
                if (string[x+2][0][y+2] == "A"):
                    if (string[x+3][0][y+3] == "S"):
                        sum += 1
        
        if (string[x][0][y] == "X"):
            if (string[x+1][0][y-1] == "M"):
                if (string[x+2][0][y-2] == "A"):
                    if (string[x+3][0][y-3] == "S"):
                        sum += 1
        
        if (string[x][0][y] == "X"):
            if (string[x-1][0][y+1] == "M"):
                if (string[x-2][0][y+2] == "A"):
                    if (string[x-3][0][y+3] == "S"):
                        sum += 1
        
        if (string[x][0][y] == "X"):
            if (string[x-1][0][y-1] == "M"):
                if (string[x-2][0][y-2] == "A"):
                    if (string[x-3][0][y-3] == "S"):
                        sum += 1


#vertical
# x =   x, y      x, y
# m =   x, y+1    x, y-1
# a =   x, y+2    x, y-2
# s =   x, y+3    x, y-3

#horizontal
# x =   x, y      x, y
# m =   x+1, y    x-1, y
# a =   x+2, y    x-2, y
# s =   x+3, y    x-3, y

#diagonal
# x =   x, y        x, y        x, y        x, y
# m =   x+1, y+1    x+1, y-1    x-1, y+1    x-1, y-1
# a =   x+2, y+1    x+2, y-2    x-2, y+2    x-2, y-2
# s =   x+3, y+1    x+3, y-3    x-3, y+3    x-3, y-3

print(sum)
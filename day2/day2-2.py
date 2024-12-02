def checkIfAllIncreasing(array):
    pointer = int(array[0])
    for i in range(1, len(array)):
        num = int(array[i])
        if num >= pointer:
            pointer = num
        else:
            return False
    return True

def checkIfAllDecreasing(array):
    array = array[::-1]
    pointer = int(array[0])
    for i in range(1, len(array)):
        num = int(array[i])
        if num >= pointer:
            pointer = num
        else:
            return False
    return True

def checkIfIncreasingOrDecreasingByCorrectAmount(array):
    pointer = int(array[0])
    for i in range(1, (len(array))):
        num = int(array[i])
        difference = abs(pointer-num)
        if (difference <= 3 and difference >= 1):
            pointer = num
        else:
            return False
    return True

def check(array):
    return ((checkIfAllDecreasing(array) or checkIfAllIncreasing(array)) and checkIfIncreasingOrDecreasingByCorrectAmount(array))

sum = 0
with open('input.txt','r') as file:
    for line in file.readlines():
        line = line.split("\n")[0]
        numbers = line.split(" ")

        newNumbers = numbers
        if (check(numbers) == True):
            sum += 1
        else:
            for i in range(len(newNumbers)-1):
                numberDeleted = newNumbers[i]
                newNumbers.pop(i)
                if(check(newNumbers) == True):
                    sum += 1

                newNumbers.insert(i, numberDeleted)
        
print(sum)
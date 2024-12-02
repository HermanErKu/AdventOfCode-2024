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

sum = 0
with open('input.txt','r') as file:
    for line in file.readlines():
        line = line.split("\n")[0]
        numbers = line.split(" ")
        
        if ((checkIfAllDecreasing(numbers) or checkIfAllIncreasing(numbers)) and checkIfIncreasingOrDecreasingByCorrectAmount(numbers)):
            sum += 1

print(sum)
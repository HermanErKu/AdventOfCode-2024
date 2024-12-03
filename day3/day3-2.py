import re

wholeLine = ""
with open('input.txt', 'r') as file:
    for line in file:
        for char in line:
            if (char != "\n"):
                wholeLine += char

wholeLine = re.sub(r"don't\(\).*?(?=do\(\)|$)", '', wholeLine)
regexSearchResult = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)',wholeLine)

sum = 0
for result in regexSearchResult:
    numbers = str(result).split("(")[1].split(")")[0]
    
    num1 = int(numbers.split(",")[0])
    num2 = int(numbers.split(",")[1])

    sum += (num1 * num2)

print(sum)
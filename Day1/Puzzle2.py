import re

sum = 0
inputs = []
numDict = {"one": 1,"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open("calibration.txt") as inpFile:
    inputs = inpFile.readlines()

for inputText in inputs:
    numbers = re.findall(r"(?=("+'|'.join(numDict.keys())+r"|[0-9]))", inputText)

    firstNum = numbers[0] if len(numbers[0]) == 1 else str(numDict[numbers[0]]) 
    lastNum = numbers[-1] if len(numbers[-1]) == 1 else str(numDict[numbers[-1]])

    # print(firstNum + lastNum)
    sum += int(firstNum + lastNum)

print(sum)
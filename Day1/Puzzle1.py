import re

sum = 0
inputs = []

with open("calibration.txt") as inpFile:
    inputs = inpFile.readlines()

for inputText in inputs:
    digits = re.findall("[0-9]", inputText)
    sum += int(digits[0] + digits[-1])

print(sum)
import re
from copy import deepcopy

oRegisters = {}

with open("2024/D17/input.txt") as inFile:
    registerStr, program = inFile.read().split("\n\n")

    for registerStr in registerStr.split("\n"):
        register, value = re.findall(r"(\w+): (\d+)", registerStr)[0]
        oRegisters[register] = int(value)

    program = [int(value) for value in program.split()[1].split(",")]

    registers = deepcopy(oRegisters)


print(registers)
print(program)
print()


def comboOperand(value):
    if 0 <= value <= 3:
        return value
    elif value == 4:
        return registers["A"]
    elif value == 5:
        return registers["B"]
    elif value == 6:
        return registers["C"]


def adv(operand):
    registers["A"] = registers["A"] >> comboOperand(operand)

def bxl(operand):
    registers["B"] = registers["B"] ^ operand

def bst(operand):
    registers["B"] = comboOperand(operand) % 8

def jnz(operand):
    global pointer
    if registers["A"] == 0:
        return
    pointer = operand

def bxc(operand):
    registers["B"] = registers["B"] ^ registers["C"]

def out(operand):
    programOutput.append(comboOperand(operand) % 8)

def bdv(operand):
    registers["B"] = registers["A"] >> comboOperand(operand)

def cdv(operand):
    registers["C"] = registers["A"] >> comboOperand(operand)


instructionMap = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}


def runProgram(a):
    global programOutput, registers, pointer

    currentA = a
    registers = deepcopy(oRegisters)
    registers["A"] = currentA

    programOutput = []
    pointer = 0

    while pointer < len(program):
        instruction, operand = program[pointer], program[pointer+1]
        pointer += 2
        instructionMap[instruction](operand)

    # print(currentA, ": ", ",".join([str(output) for output in programOutput]))

    return programOutput


a = 0
for i in reversed(range(len(program))):
    a <<= 3
    programOutput = []
    while runProgram(a) != program[i:]:
        a += 1

print("Part 2:", a)

import re


class Machine:
    def __init__(self, buttonA, buttonB, prize) -> None:
        self.buttonA = buttonA
        self.aCost = 3
        self.buttonB = buttonB
        self.bCost = 1
        self.prize = prize


with open("2024/D13/input.txt") as inFile:
    machineStrs = [mach for mach in inFile.read().split("\n\n")]

    machines = []
    for machineStr in machineStrs:
        config = machineStr.split("\n")
        
        buttonA = (int(re.findall(r"X\+(\d+)", config[0])[0]), int(re.findall(r"Y\+(\d+)", config[0])[0]))
        buttonB = (int(re.findall(r"X\+(\d+)", config[1])[0]), int(re.findall(r"Y\+(\d+)", config[1])[0]))
        prize = [int(re.findall(r"X=(\d+)", config[2])[0]), int(re.findall(r"Y=(\d+)", config[2])[0])]
        
        machines.append(Machine(buttonA, buttonB, prize))


def solvePuzzle(offset=0):
    minTokens = 0
    for machine in machines:
        machine.prize[0] += offset
        machine.prize[1] += offset

        buttonA = machine.buttonA
        buttonB = machine.buttonB
        prize = machine.prize

        solution = None

        a = (buttonB[1] * prize[0] - buttonB[0] * prize[1]) // (buttonB[1] * buttonA[0] - buttonB[0] * buttonA[1])
        b = (prize[0] - buttonA[0] * a) // buttonB[0]
        
        if prize[0] == buttonA[0] * a + buttonB[0] * b and prize[1] == buttonA[1] * a + buttonB[1] * b:
            solution = (a, b)

        if solution:
            # print("Solution Found", solution)
            minTokens += solution[0] * machine.aCost + solution[1] * machine.bCost
        else:
            # print("No Solution")
            pass

    return minTokens


print("Part 1 - MinTokens:", solvePuzzle())
print("Part 2 - MinTokens:", solvePuzzle(10000000000000))


def oldSol():
    # machine = machines[0]
    failed = 0
    for machine in machines:
        # print("\n\nMachine")
        solutions = []
        buttonA = machine.buttonA
        buttonB = machine.buttonB
        prize = machine.prize


        # minA = 0
        # minB = 0
        # maxA = 100
        # maxB = 100
        # maxA = min(prize[0] // buttonA[0], prize[1] // buttonA[1])
        # maxB = min(prize[0] // buttonB[0], prize[1] // buttonB[1])
        
        # Part 2
        minA = min(offset // buttonA[0] // 2, offset // buttonA[1] // 2)
        minB = min(offset // buttonB[0] // 2, offset // buttonB[1] // 2)
        maxA = min(prize[0] // buttonA[0], prize[1] // buttonA[1])
        maxB = min(prize[0] // buttonB[0], prize[1] // buttonB[1])

        print(minA, minB, maxA, maxB)
        curPos = [0, 0]
        for i in range(minA, maxA):
            for j in range(minB, maxB):
                curPos[0] = buttonA[0] * i + buttonB[0] * j  
                curPos[1] = buttonA[1] * i + buttonB[1] * j  

                if curPos[0] > prize[0] or curPos[1] > prize[1]:
                    curPos = [0, 0]
                    continue

                if curPos[0] == prize[0] and curPos[1] == prize[1]:
                    # print("\nSolution found")
                    # print(i, j)
                    solutions.append((i, j))

        if not solutions:
            # print("No Solution Found")
            failed += 1
            continue
        
        minSolution = None
        minCost = offset
        for solution in solutions:
            cost = solution[0] * machine.aCost + solution[1] * machine.bCost
            
            if cost < minCost:
                minCost = cost
                minSolution = solution

        minTokens += minCost
        # print("\nMin:", minSolution)

    print("No of machines:", len(machines))
    print("Failed:", failed)



xValues = {}
yValues = {}

gates = {}
with open("2024/D24/input.txt") as inFile:
    initial, gateStrs = inFile.read().split("\n\n")

    values = initial.split("\n")
    gateStrs = gateStrs.split("\n")

    for value in values:
        k, val = value.split(": ")
        if value.startswith("x"):
            xValues[k] = int(val)
        if value.startswith("y"):
            yValues[k] = int(val)
    
    gateStrs = [gate.split(" -> ") for gate in gateStrs]
    for gate, val in gateStrs:
        gates[gate] = val


def generateAddLogic(bit, carry):
    bit = str(bit).zfill(2)
    logicStr = ""

    print("Bit", bit)
    gate1 = f"x{bit} XOR y{bit}"
    s = gates.get(gate1, gates.get(f"y{bit} XOR x{bit}", ""))
    logicStr += gate1 + " -> " + s + "\n"
    
    gate2 = f"x{bit} AND y{bit}"
    w1 = gates.get(gate2, gates.get(f"y{bit} AND x{bit}", ""))
    logicStr += gate2 + " -> " + w1 + "\n"
    
    gate3 = f"{s} AND {carry}"
    w2 = gates.get(gate3, gates.get(f"{carry} AND {s}", ""))
    logicStr += gate3 + " -> " + w2 + "\n"
    
    gate4 = f"{w1} OR {w2}"
    cO = gates.get(gate4, gates.get(f"{w2} OR {w1}", ""))
    logicStr += gate4 + " -> " + cO + "\n"
    
    gate5 = f"{s} XOR {carry}"
    z = gates.get(gate5, gates.get(f"{carry} XOR {s}", ""))
    logicStr += gate5 + " -> " + z + "\n\n"

    print(logicStr)

    return logicStr, cO
    

swapped = ["nqk", "z07", "pcp", "fgt", "fpq", "z24", "srn", "z32"]

print(",".join(sorted(swapped)))
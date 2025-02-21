class Computer:
    def __init__(self, name) -> None:
        self.name = name
        self.connections = set()

with open("2024/D23/input.txt") as inFile:
    pairs = [pair.strip().split("-") for pair in inFile.readlines()]

print(len(pairs))

computers = {}
for comp1, comp2 in pairs:
    if comp1 not in computers:
        computers[comp1] = Computer(comp1)
    if comp2 not in computers:
        computers[comp2] = Computer(comp2)
    
    computers[comp1].connections.add(comp2)
    computers[comp2].connections.add(comp1)


# print(computers)


triples = []

for name, computer in computers.items():
    if not name.startswith("t"):
        continue
    
    for conn in computer.connections:
        for otherConn in computers[conn].connections:
            if name in computers[otherConn].connections:
                triples.append((name, conn, otherConn))

unique_triples = {tuple(sorted(triple)) for triple in triples}
print("Unique Triples:", len(unique_triples))


def findLan(lan, candidates, x):
    global lans

    if not candidates and not x:
        lans.append(lan)
        return lan
    
    for comp in list(candidates):
        connections = set(computers[comp].connections)
        findLan(lan.union({comp}), candidates.intersection(connections), x.intersection(connections))
        candidates.remove(comp)
        x.add(comp)


lans = []
findLan(set(), set(computers.keys()), set())
password = ",".join(list(sorted(max(lans, key=len))))
print(password)

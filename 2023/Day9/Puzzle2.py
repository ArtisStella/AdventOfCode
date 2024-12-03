
histories = []

with open("report.txt") as inFile:
    histories = inFile.readlines()


def getSubsequence(sequence):
    retSeq = []
    for i in range(len(sequence) - 1):
        retSeq.append(sequence[i+1] - sequence[i])
    return retSeq


def PredictNext(history):

    sequences = [list(map(lambda x: int(x), history.strip().split())), ]
    
    i = 1
    finished = False

    while not finished:
        nextSequence = getSubsequence(sequences[i-1])
        sequences.append(nextSequence)
        finished = all(value == 0 for value in nextSequence)
        i += 1

    # print(sequences)

    for i, sequence in reversed(list(enumerate(sequences))):
        if i == len(sequences) - 1:
            continue

        # print(i, sequence)
        pred = sequence[0] - sequences[i+1][0]
        sequence.insert(0, pred)
    
    # print(sequences)
    return sequences[0][0]


predictions = [PredictNext(history) for history in histories]

print(sum(predictions))

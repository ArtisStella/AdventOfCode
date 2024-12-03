
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

    for i, sequence in reversed(list(enumerate(sequences))):
        if i == len(sequences) - 1:
            continue

        # print(i, sequence)
        pred = sequence[-1] + sequences[i+1][-1]
        sequence.append(pred)
    
    return sequences[0][-1]


predictions = [PredictNext(history) for history in histories]

print(sum(predictions))

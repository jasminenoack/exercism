def distance(dna1, dna2):
    count = 0
    for el1, el2 in zip(dna1, dna2):
        if el1 != el2:
            count += 1
    return count
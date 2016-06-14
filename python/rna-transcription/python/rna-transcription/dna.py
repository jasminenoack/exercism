TO_RNA = {
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G"
}

def translate(el):
    return TO_RNA[el]

def to_rna(dna):
    return "".join(map(translate, dna))
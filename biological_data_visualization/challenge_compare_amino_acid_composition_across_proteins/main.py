import matplotlib.pyplot as plt

def plot_amino_acid_compositions(sequences, protein_labels=None):
    amino_acids = [
        'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I',
        'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'
    ]
    compositions = []
    for seq in sequences:
        seq = seq.upper()
        length = len(seq)
        comp = []
        for aa in amino_acids:
            count = seq.count(aa)
            fraction = count / length if length > 0 else 0
            comp.append(fraction)
        compositions.append(comp)
    num_proteins = len(sequences)
    if protein_labels is None or len(protein_labels) != num_proteins:
        protein_labels = [f"Protein {i+1}" for i in range(num_proteins)]
    bar_width = 0.8 / num_proteins
    x = range(len(amino_acids))
    plt.figure(figsize=(12, 6))
    for i, comp in enumerate(compositions):
        bar_positions = [xi + i * bar_width for xi in x]
        plt.bar(bar_positions, comp, width=bar_width, label=protein_labels[i])
    plt.xticks([xi + bar_width * (num_proteins-1)/2 for xi in x], amino_acids)
    plt.xlabel("Amino Acid")
    plt.ylabel("Fraction of Sequence")
    plt.title("Amino Acid Composition Across Proteins")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Sample calls
sequences = [
    "MKTFFVAGVILLLPLVSSQCVNLTTRTQ",
    "MGLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKG",
    "MKKFFDSRREQMKLQK"
]
protein_labels = ["Sample1", "Sample2", "Sample3"]
plot_amino_acid_compositions(sequences, protein_labels)

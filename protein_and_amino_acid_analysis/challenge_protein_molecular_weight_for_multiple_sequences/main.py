def calculate_molecular_weights(sequences):
    amino_acid_weights = {
        "A": 89.09,  # Alanine
        "R": 174.20, # Arginine
        "N": 132.12, # Asparagine
        "D": 133.10, # Aspartic acid
        "C": 121.15, # Cysteine
        "E": 147.13, # Glutamic acid
        "Q": 146.15, # Glutamine
        "G": 75.07,  # Glycine
        "H": 155.16, # Histidine
        "I": 131.17, # Isoleucine
        "L": 131.17, # Leucine
        "K": 146.19, # Lysine
        "M": 149.21, # Methionine
        "F": 165.19, # Phenylalanine
        "P": 115.13, # Proline
        "S": 105.09, # Serine
        "T": 119.12, # Threonine
        "W": 204.23, # Tryptophan
        "Y": 181.19, # Tyrosine
        "V": 117.15  # Valine
    }
    # Write your code here
    results = []
    for seq in sequences:
        weight = 0.0
        for aa in seq:
            if aa in amino_acid_weights:
                weight += amino_acid_weights[aa]
        results.append(weight)
    return results

# Sample calls
sequences1 = ["ACDE", "WYK", "GGG", "MSTQ"]
mw_list1 = calculate_molecular_weights(sequences1)
print(mw_list1)

sequences2 = ["AXYZ", "CDEFG", "RRR"]
mw_list2 = calculate_molecular_weights(sequences2)
print(mw_list2)

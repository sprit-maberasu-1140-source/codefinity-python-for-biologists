def amino_acid_compositions(sequences):
    valid_aas = set("ACDEFGHIKLMNPQRSTVWY")
    compositions = []
    for seq in sequences:
        seq = seq.upper()
        aa_counts = {}
        total = 0
        for aa in seq:
            if aa in valid_aas:
                aa_counts[aa] = aa_counts.get(aa, 0) + 1
                total += 1
        if total == 0:
            compositions.append({})
            continue
        comp_dict = {}
        for aa, count in aa_counts.items():
            comp_dict[aa] = (count / total) * 100
        compositions.append(comp_dict)
    return compositions

# Sample calls
seqs = [
    "MKTIIALSYIFCLVFADYKDDDDA",
    "GAVLIPFYWSTCMNQDEKRH",
    "MXXKZZ",
    ""
]
result = amino_acid_compositions(seqs)
print(result)
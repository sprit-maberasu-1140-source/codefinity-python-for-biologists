def find_motif_positions(sequences, motif):
    result = {}
    motif_len = len(motif)
    for seq in sequences:
        positions = []
        for i in range(len(seq) - motif_len + 1):
            if seq[i:i+motif_len] == motif:
                positions.append(i)
            result[seq] = positions
    return result

sequences = ["ATGCGATATCG", "GATATATGCATATACTT"]
motif = "ATAT"
motif_positions = find_motif_positions(sequences, motif)
positions_var = motif_positions
print(positions_var)

sequences2 = ["AAAAA", "TTTTT"]
motif2 = "AA"
motif_positions2 = find_motif_positions(sequences2, motif2)
positions_var2 = motif_positions2
print(positions_var2)

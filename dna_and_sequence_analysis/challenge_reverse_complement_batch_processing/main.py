def reverse_complement_batch(sequences):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = []
    for seq in sequences:
        filtered = [b.upper() for b in seq if b.upper() in complement]
        if not filtered:
            result.append("")
            continue
        reversed_seq = filtered[::-1]
        rev_comp = "".join(complement[b] for b in reversed_seq)
        result.append(rev_comp)
    return result

# Sample calls
batch1 = ["ATCG", "ggta", "ACGTN", "xyz", "AAGCCTT"]
result1 = reverse_complement_batch(batch1)
print(result1)  # ['CGAT', 'TACC', 'ACGT', '', 'AAGGCTT']

batch2 = ["", "NNNN", "AGCTAGC"]
result2 = reverse_complement_batch(batch2)
print(result2)  # ['', '', 'GCTAGCT']
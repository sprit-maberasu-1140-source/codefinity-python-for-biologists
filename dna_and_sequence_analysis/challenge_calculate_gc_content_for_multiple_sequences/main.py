def gc_content_batch(sequences):
    gc_contents = []
    for seq in sequences:
        seq = seq.upper()
        valid_bases = [base for base in seq if base in "ATGC"]
        gc_count = sum(1 for base in valid_bases if base in "GC")
        total_count = len(valid_bases)
        if total_count == 0:
            gc_percent = 0.0
        else:
            gc_percent = (gc_count / total_count) * 100
        gc_contents.append(gc_percent)
    return gc_contents

# Sample calls
sequences = ["ATGCGC", "atttggc", "NNNNNN", "GATTACA", "CGCGCG"]
results = gc_content_batch(sequences)
print(results)

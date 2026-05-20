def batch_translate_dna_to_protein(dna_sequences):
    codon_table = {
        "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
        "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
        "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
        "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
        "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
        "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
        "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
        "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
        "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
        "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
        "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
        "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
        "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
        "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
        "TAC":"Y", "TAT":"Y", "TAA":"_", "TAG":"_",
        "TGC":"C", "TGT":"C", "TGA":"_", "TGG":"W",
    }
    proteins = []

    for seq in dna_sequences:
        protein = ""
        # 1. 0 から len(seq)-2 までを3つずつ進める
        for i in range(0, len(seq) - 2, 3):
            codon = seq[i:i+3]            # 2. 3文字を切り出す
            aa = codon_table.get(codon)  # 3. 対応するアミノ酸を調べる
            if aa == "_":                # 4. ストップコドンならループを抜ける
                break
            if aa:                       # 5. 見つかったアミノ酸を追加
                protein += aa
            # （未定義コドンはスキップしてもよい）
        proteins.append(protein)

    return proteins

# Sample calls
print(batch_translate_dna_to_protein(["ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]))
print(batch_translate_dna_to_protein(["ATGTACTAA", "ATGCGT"]))
print(batch_translate_dna_to_protein(["ATGAAATGA", "ATGTTTGGGCCC"]))
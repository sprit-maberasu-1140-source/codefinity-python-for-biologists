import matplotlib.pyplot as plt
import numpy as np

def calculate_gc_content(seq):
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100 if len(seq) > 0 else 0

def plot_length_gc(sequences, groups=None):
    # 長さとGC含量を計算
    lengths = [len(s) for s in sequences]
    gc_contents = [calculate_gc_content(s) for s in sequences]

    # 外れ値検出（IQR）
    def outlier_indices(data):
        q1, q3 = np.percentile(data, [25, 75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        return [i for i, v in enumerate(data) if v < lower or v > upper]

    out_idx = set(outlier_indices(lengths) + outlier_indices(gc_contents))

    # 色の設定
    if groups is not None:
        uniq = list(set(groups))
        cmap = {g: plt.cm.tab10(i % 10) for i, g in enumerate(uniq)}
        colors = [cmap[g] for g in groups]
    else:
        colors = "blue"

    # プロット
    fig, ax = plt.subplots()
    ax.scatter(lengths, gc_contents, c=colors, edgecolor='k', alpha=0.7)

    # 外れ値にラベル
    for i in out_idx:
        ax.annotate(f"Seq {i}", (lengths[i], gc_contents[i]),
                    textcoords="offset points", xytext=(5,5),
                    ha='left', fontsize=8, color='red')

    ax.set_xlabel("Sequence Length")
    ax.set_ylabel("GC Content (%)")
    ax.set_title("Sequence Length vs GC Content")

    # 凡例（グループありの場合）
    if groups is not None:
        handles = [
            plt.Line2D([0],[0], marker='o', color='w', label=g,
                       markerfacecolor=cmap[g], markersize=8, markeredgecolor='k')
            for g in uniq
        ]
        ax.legend(handles=handles, title="Group")

    plt.tight_layout()
    plt.show()

# Example usage
sequences = [
    "ATGCGCGTAC",
    "ATATATATATAT",
    "CGCGCGCGCGCGCGCGCGCG",
    "ATGC",
    "GGGGGGGGGGGGGG",
    "TATATATATATA",
    "ATGCGC",
    "ATATATAT",
    "GCGCGCGCGCGC",
    "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTA"
]
groups = ["A", "A", "B", "A", "B", "A", "A", "A", "B", "B"]
plot_length_gc(sequences, groups)
plot_length_gc(sequences)
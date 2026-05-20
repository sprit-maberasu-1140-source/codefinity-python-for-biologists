import matplotlib.pyplot as plt

def plot_gc_content(sequences):
    # 1. 各シーケンスの GC 含量を計算してリストに格納
    gc_contents = []
    for seq in sequences:
        # a) G または C の数を数える
        gc_count = sum(1 for base in seq if base.upper() in ['G', 'C'])
        # b) シーケンス長が 0 の場合は 0%、それ以外はパーセントを計算
        gc_content = (gc_count / len(seq)) * 100 if len(seq) > 0 else 0
        gc_contents.append(gc_content)

    # 2. x 軸に使うシーケンスのインデックスを用意
    indices = list(range(len(sequences)))

    # 3. GC が 60% を超えるバーの色を赤、そうでないものを青に設定
    colors = ['red' if gc > 60 else 'blue' for gc in gc_contents]

    # 4. グラフ描画の基本設定
    plt.figure(figsize=(10, 6))
    plt.bar(indices, gc_contents, color=colors)

    # 5. 軸ラベル、タイトル、目盛りを設定
    plt.xlabel('Sequence Index')
    plt.ylabel('GC Content (%)')
    plt.title('GC Content of DNA Sequences')
    plt.xticks(indices, [str(i) for i in indices])
    plt.ylim(0, 100)

    # 6. グラフを表示
    plt.show()

# 実行例
sequences = [
    "ATGCGCGTA",
    "ATATATATAT",
    "GGGCCCGGG",
    "TTAACCGGTT",
    "GCGCGCGCGC"
]
plot_gc_content(sequences)
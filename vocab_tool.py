import csv

def main():
    # 1.读：读取data下的生词表csv
    with open("data/生词表.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        words = list(reader)

    # 2.筛：只挑HSK等级等于4的单词
    hsk4_words = [w for w in words if w["HSK等级"] == "4"]

    # 3.统计：总词数、HSK4数量、词性分布
    total_count = len(words)
    hsk4_count = len(hsk4_words)

    pos_count = {}
    for w in hsk4_words:
        pos = w["词性"]
        if pos not in pos_count:
            pos_count[pos] = 0
        pos_count[pos] += 1

    # 控制台打印统计信息
    print(f"总词汇 {total_count} 个，其中 HSK4 词汇 {hsk4_count} 个。")
    print(f"词性分布：{pos_count}")

    # 4.写：生成练习.txt
    out_lines = []
    for w in hsk4_words:
        question = f"用「{w['词汇']}」造一个句子。（{w['词性']}）"
        out_lines.append(question)

    with open("练习.txt", "w", encoding="utf-8") as out_f:
        out_f.write("\n".join(out_lines))
    print("已生成：练习.txt")

if __name__ == "__main__":
    main()

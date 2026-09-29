#1.任务与提示词 要做什么：读取 data/生词表.csv，筛选HSK4词汇，统计词性分布，生成练习题写入练习.txt。我的提示词：写Python vocab_tool.py，四步：读csv、筛选HSK4、统计词性分布、输出练习txt。csv路径数据/生词表.csv，表头词汇，HSK等级，词性，释义，用utf8编码。输出每行一道题：用“词语」造一个句子。（词性）

#2。AI初版代码导入csv with open("data/生词表.csv") as f: reader = csv.DictReader(f) words = list(reader) hsk4 = [w for w in words if w["HSK等级"]=="4"] for w in hsk4: print(w["词汇"])

#3。我的修改点（4条） 1 增加 encoding="utf-8" 原因：打开csv不指定utf8，中文会乱码，汉字变成问号。

2 增加统计代码，统计总词数、HSK4数量、词性计数 原因：PPT作业要求输出统计信息，只筛选单词没有统计，达不到任务要求。

3 增加代码写入练习.txt文件 原因：初版只打印在控制台，没有输出文本文件，缺少作业要求的输出文件。

4封装到主函数，增加if name==“main”原因：规范Python写法，方便后续扩展功能，代码结构更清晰。

#4。最终版vs初版差异说明初版：只能读取csv并筛选HSK4词汇，没有编码处理，没有统计，不会输出txt文件，中文容易乱码。最终版：增加utf-8编码解决中文乱码；新增总词数、HSK数量、词性统计；自动生成练习.txt；使用主函数组织代码，结构完整，完全匹配PPT任务需求。

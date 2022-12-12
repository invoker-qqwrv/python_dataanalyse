# jiayou
'''
DA1 用pandas查看牛客网用户数据
现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
# Nowcoder_ID：用户ID
# Level：等级
# Achievement_value：成就值
# Num_of_exercise：刷题量
# Graduate_year：毕业年份
# Language：常用语言
# 你可以使用pandas打开文件，偷偷看一下里面的内容，请输出你看到的前6行数据。
# 输入描述：
# 数据集直接从当前目录下的Nowcoder.csv文件中读取。
打开文件时需要添加dtype=object，防止年份信息读取为小数'''
import pandas as pd
# Nowcoder=pd.read_csv('Nowcoder.csv',sep=',',dtype=object)
# print(Nowcoder.head(6))#这里没这个文件，所以暂不测试输出

'''DA2 牛客网用户数据集的大小
现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
Nowcoder_ID：用户ID
Level：等级
Achievement_value：成就值
Num_of_exercise：刷题量
Graduate_year：毕业年份
Language：常用语言
你不需要输出全部数据，请直接告诉我们这个数据集的大小，即行数与列数。
输入描述：
数据集直接从当前目录下的Nowcoder.csv文件中读取。

'''
#输出该数据集的行数和列数
# import pandas as pd
# Nowcoder=pd.read_csv('Nowcoder.csv',sep=',',dtype=object)
# print(Nowcoder.shape)

'''
DA3 牛客网的第10位用户
现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
Nowcoder_ID：用户ID
Level：等级
Achievement_value：成就值
Num_of_exercise：刷题量
Graduate_year：毕业年份
Language：常用语言
现在牛牛想知道这个数据集中第10行的用户的全部信息，请你帮他输出一下。
输入描述：
数据集直接从当前目录下的Nowcoder.csv文件中读取。
输出描述：
输出该数据集第10行的全部信息，每列信息单独成行，如下所示：
'''
#第10行应该是整数索引为9。题目有误

# import pandas as pd
# Nowcoder=pd.read_csv('Nowcoder',sep=',',dtype=object)
# print(Nowcoder.loc[10])
#loc :  Selection by Label ，按标签取数据,
# loc[行索引，列名/column]
# （如果第二个参数的个数是全部即 : ，可以省略不写）。
# 例：
# print(df.loc[1,'name'])    # 索引1（行），名为‘name’的列

'''DA4 统计牛客网部分用户使用语言
现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
Nowcoder_ID：用户ID
Level：等级
Achievement_value：成就值
Num_of_exercise：刷题量
Graduate_year：毕业年份
Language：常用语言
现在牛牛想知道这个数据集中第10行到第20行的用户的常用语言分别是什么，请你帮他输出一下。
输入描述：
数据集直接从当前目录下的Nowcoder.csv文件中读取
'''
# import pandas as pd
# Nowcoder=pd.read_csv('Nowcoder',sep=',',dtype=object)
# print(Nowcoder.loc[10:20, 'Language'])
# print(Nowcoder.iloc[10:20, 5])#iloc 列的索引为第五列
# print(Nowcoder['Language'][10:20])
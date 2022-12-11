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
'''
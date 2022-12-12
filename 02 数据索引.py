'''DA5 牛客网用户没有补全的信息
现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
Nowcoder_ID：用户ID
Level：等级
Achievement_value：成就值
Num_of_exercise：刷题量
Graduate_year：毕业年份
Language：常用语言
如果你想知道这份数据是不是所有列的信息都是有数据的，有没有哪些列的数据没有补全，请输出每列信息是否有为空值。
输入描述：
数据集直接从当前目录下的Nowcoder.csv文件中读取
'''
# import pandas as pd
# Nowcoder = pd.read_csv('Nowcoder.csv',sep=',',dtype=object)#seq 参数用来指定字符的分隔符号
# print(Nowcoder.isna().any())#SNA函数，是用来检测一个值是否为#N/A，返回TRUE或FALSE
# Python中 any () 函数的基本使用 ：any () 函数用于判断给定的可迭代参数 iterable 是否都为 False，
# 如果是，any ()操作后的结果返回 False，如果给定的可迭代参数 iterable其中有一个为 True，any ()操作后的结果则返回 True。
# axis=0:方向沿着列；axis=1方向沿着行
# import pandas as pd
# Nowcoder = pd.read_csv('Nowcoder.csv',sep=',',dtype=object)
# print(Nowcoder.isna().any(axis=0))
'''DA6 查看牛客网哪些用户使用Python
现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
Nowcoder_ID：用户ID
Level：等级
Achievement_value：成就值
Num_of_exercise：刷题量
Graduate_year：毕业年份
Language：常用语言
如果你想知道哪些人经常使用Python这门语言，并且他们的其他信息是怎么样的，该怎么输出？

输入描述：
数据集直接从当前目录下的Nowcoder.csv文件中读取。
'''
# import pandas as pd
# Nowcoder = pd.read_csv('Nowcoder.csv',sep=',',dtype=object)#seq 参数用来指定字符的分隔符号
# print(Nowcoder.query('Language=="Python"'))#查询query，language这一行的代码是python的
'''DA7 牛客网Python用户的成就值
现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
Nowcoder_ID：用户ID
Level：等级
Achievement_value：成就值
Num_of_exercise：刷题量
Graduate_year：毕业年份
Language：常用语言
假如你正在学习Python，你想知道牛客网的Python用户的成就值都有多高，请问该如何输出？
输入描述：
数据集直接从当前目录下的Nowcoder.csv文件中读取。
'''
# import pandas as pd
# Nowcoder = pd.read_csv('Nowcoder.csv',sep=',',dtype=object)#seq 参数用来指定字符的分隔符号
#
#
# print(Nowcoder.query('Language=="Python"')['Achievement_value'])
'''DA8 文件最后用户的部分数据
现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
Nowcoder_ID：用户ID
Level：等级
Achievement_value：成就值
Num_of_exercise：刷题量
Graduate_year：毕业年份
Language：常用语言
Continuous_check_in_days：最近连续签到天数
Number_of_submissions：提交代码次数
Last_submission_time：最后一次提交题目日期
假设你想查看该文件最后5行用户的用户ID、等级、成就值、常用语言，请尝试输出。
输入描述：
数据集直接从当前目录下的Nowcoder.csv文件中读取。
'''
import pandas as pd
Nowcoder = pd.read_csv('Nowcoder.csv',sep=',')#seq 参数用来指定字符的分隔符号
#type=object主要是防止年份信息读取错误
# print(Nowcoder.tail(5)[["Nowcoder_ID", "Level", "Achievement_value", "Language"]])#为什么这里有两个中括号
#
print(Nowcoder.iloc[-5:,[0,1,2,5]])#-5行到最后，而且是0 1 2 5列

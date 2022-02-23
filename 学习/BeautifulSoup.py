"""
==================================
@author:    陈杰
@time:      2022/1/27:21:58
==================================
"""

from bs4 import BeautifulSoup

def print_list(list):
    for _ in list:
        print(_)

# 打开文件
file = open("../test.html", "rb")
# 读取文件
html = file.read()
# 使用Beautiful Soup中的"html.parser"解析器解析上面的html文件
bs = BeautifulSoup(html, "html.parser")

# 打印网页文件的第一个title标签
# print(bs.title)
# 打印网页文件的第一个title标签的内容
# print(bs.title.string)

# 文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])

# 字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# print(t_list.content())

import re
# 正则表达式搜索；使用search()方法匹配内容
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

# 指定函数查找
# def name_is_exist(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exist)
# print(t_list)

# 指定参数查找
# t_list = bs.find_all(id="nv")
# print_list(t_list)

# text参数
# t_list = bs.find_all(text = "22")
# t_list = bs.find_all(text=["22","33"])
# t_list = bs.find_all(test = re.compile("\d"))
# print_list(t_list)

# limit参数(获取上限)
# t_list = bs.find_all("a", limit=3)
# print_list(t_list)

# css选择器
# t_list = bs.select("title") # 通过标签查找
# t_list = bs.select(".mnav") # 通过类名查找
# t_list = bs.select("#u1") # 通过id查找
# t_list = bs.select("a[class='bri']") # 通过标签中的属性进行查找
# t_list = bs.select("head > title") # 通过子标签来查找
# print_list(t_list)

t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())









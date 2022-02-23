"""
==================================
@author:    陈杰
@time:      2022/2/3:19:16
==================================
"""

import re

# -------------------search：搜索第一个符合的内容-------------------
# pat = re.compile("AA") # 此处的AA是正则表达式，用来验证其他的字符串
# m = pat.search("ABCAADD")
# print(m)
# m = pat.search("ABBCAADDCCAAA") # 只找到第一个符合规则的内容
# print(m)
#
# 没有模式对象
# m = re.search("asd", "Aasd") # 前面的字符串是规则，后面的字符串是被校验的对象
# print(m)

# -------------------findall：找到所有符合的内容-------------------
print(re.findall("a", "ASDaDFGAa")) # 前面的字符串是规则，后面的字符串是被校验的对象
print(re.findall("[A-Z]", "ASDaDFGAa")) # 只搜索大写字母
print(re.findall("[A-Z]+", "ASDaDFGAa")) # 只搜索大写字母，可以组合搜索

# -------------------sub：替换符合的内容-------------------
print(re.sub("a","A","abcdcasd")) # 第一个参数是

# 建议在正则表达式中，被比较的字符串前面加上r，这样可以不用担心转义字符的问题
a = "\aabd-\'"
print(a)
b = r"\aabd-\'"
print(b)





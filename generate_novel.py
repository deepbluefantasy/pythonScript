"""
==================================
@author:    陈杰
@time:      2022/2/1:22:33
@function:  html论坛小说转换为txt文本
==================================
"""
import re

from bs4 import BeautifulSoup

def main():
    file_name = input("请将html文件拽进来：")
    file_name = file_name.replace("\"", "")
    txt_name = file_name.replace(".html",".txt")

    # 打开文件
    file = open(file_name, "rb")
    # 读取文件
    html = file.read()
    # 使用Beautiful Soup中的"html.parser"解析器解析上面的html文件
    soup = BeautifulSoup(html, "html.parser")

    text = ""
    for item in soup.find_all("div", class_="t_fsz"):
        text += str(item)

    # 替换杂七杂八的标签
    text = re.sub(r'<div class="t_fsz">',"",text)
    text = re.sub(r'<div align="left">',"\r\n",text)
    text = re.sub(r'</div>',"",text)
    text = re.sub(r"<span.*?>.*?</span>","",text)
    text = re.sub(r"<font class.*?>.*?</font>","",text)

    # 处理作者对话
    text = re.sub(r"<table.*>","-------------------------------",text)
    text = re.sub(r"</i>","",text)
    text = re.sub(r"</blockquote>","\r\n-------------\r\n【作者回复】",text)

    # 处理剩余对话
    text = re.sub(r"<.*?>","",text)

    # 替换屏蔽词
    text = re.sub(r"PI‘YAN","屁眼", text)
    text = re.sub(r"JI‘BA","鸡巴", text)

    # text = re.sub(r"(\r\n)+","\r\n",text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    # text = re.sub(r"","\r\n",text)

    # 写入文件
    with open(txt_name, "w", encoding="utf-8") as f:
        f.write(text)
        print("\n转换完成，文件位置：%s" % txt_name)

    # 在系统中打开文件
    import os
    os.startfile(txt_name)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("\n程序出错，错误信息如下：")
        print(e)
    for _ in range(10):
        if(input("\n---------输入空格并回车继续转换，直接回车结束程序---------") != " "):
            break
        main()

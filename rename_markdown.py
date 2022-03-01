"""
==================================
@author:    陈杰
@time:      2022/1/27:20:10
@function:  检索Markdown文件，更改图片引用路径，同时修改配置文件夹路径
==================================
"""
import re, os


def rename_mdfile():
    # 获取文件的绝对路径，如果文件名中含有空格，则绝对路径左右两边会自动加上"
    # 因此需要去掉引号
    old_file = input("请将要修改名字的md文件拽进来：")
    old_file = old_file.replace("\"", "")

    # 从文件的绝对路径中解析所在目录
    path = re.match(r".*(?=\\)", old_file).group() + "\\"
    print("这个文件的文件位置是：" + path)

    # 获得旧文件名
    old_name = old_file.replace(path, "").replace(".md", "").replace("\"", "")
    print("这个文件的旧文件名是：" + old_name)

    # 获得新文件名
    new_name = input("\n请输入md文件的新名字（不包含后缀）：")
    # 检查新旧文件名是否一致
    for _ in range(10):
        # 新文件的绝对路径
        new_file = path + new_name + ".md"
        if (new_name == old_name):
            new_name = input("\n新文件名与旧文件名相同，请重新输入：")
        elif ("\\" in new_name or "/" in new_name or ":" in new_name or "*" in new_name or "?" in new_name \
                or "\"" in new_name or "<" in new_name or ">" in new_name or "|" in new_name):
            new_name = input("\n新文件名中不得包含这些字符：\\/:*?\"<>|，请重新输入：")
        elif (os.path.exists(new_file)):
            new_name = input("\n新文件名与目录下其他文件重名，请重新输入：")
        else:
            break


    # 新旧配置文件目录的绝对路径
    old_dict = path +  old_name + ".assets"
    new_dict = path +  new_name + ".assets"
    print("\n配置文件（如图片文件）保存的文件夹将保存在"+ new_dict +"中。")

    try:
        print("\n\n1. 开始修改md文件名，同时修改文件中的引用")
        alter(old_file, new_file, old_name, new_name)
        print("(1/2)md文件中的引用修改完成~")

        print("\n2. 开始修改配置文件夹名")
        os.rename(old_dict, new_dict)
        print("(2/2)配置文件夹名修改完成~")

        os.remove(old_file)

    except Exception as error:
        print("\n程序出错，错误信息如下：")
        print(error)
    else:
        print("\n改好啦(￣▽￣)~*")


# 修改文件内容
def alter(old_file, new_file, old_name, new_name):
    old_str = "(" + old_name + ".assets"
    new_str = "(" + new_name + ".assets"
    with open(old_file, "r", encoding="utf-8") as f1, open(new_file, "w", encoding="utf-8") as f2:
        counter = 0
        for line in f1:
            if (old_str in line):
                line = line.replace(old_str, new_str)
                counter += 1
            f2.write(line)
        print("--共修改了【%s】行引用~" % counter)


# 主程序
if __name__ == '__main__':
    rename_mdfile()
    input("\n\n---------按任意键退出---------")

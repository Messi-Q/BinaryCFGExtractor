import os
import sys
import re

"""
先执行 secondPhase；在执行 thirdPhase
"""


# 获取block所在行内容
def secondPhase(n):
    inputFileDir = "./assemblycodes/timestamp/"
    dirs = os.listdir(inputFileDir)
    # dirs.sort(key=lambda x: int(x[:-4]))
    print(dirs)
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r")
        lines = f.readlines()
        nodes = "./new_binary_data/node/timestamp/" + str(file)[0:-4] + ".txt"
        edges = "./new_binary_data/edge/timestamp/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, 'a')
        f_edge = open(edges, "a")

        flag = 0

        for line in lines:
            if "block" in line and flag == 0:
                f_node.write(line.strip() + "\n")
            if "block" in line and flag != 0:
                f_edge.write(line.strip() + "\n")
            if "}" in line:
                flag += 1
                continue


# 再次提取，将\l删除
def thirdPhase(n):
    inputFileDir = "./new_binary_data/node/timestamp/"
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./new_binary_data/new_node/timestamp/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, "w")
        lines = f.readlines()
        for line in lines:
            tt = re.sub(r'\\l', r' ', line)
            f_node.write(tt)


# 只保留指令，无block
def reserve_1(n):
    inputFileDir = "./new_binary_data/new_node/1/"  # neww是测试文件
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./reserve/reserve_1/1/" + str(n) + ".txt"
        f_node = open(nodes, "w")
        s = ''
        lines = f.readlines()
        for line in lines:
            list = line.split(" ")
            for i in list:
                if i[0:1].isupper() != 0:
                    s += i
                s += ' '
            s += '\n'
        s = s.replace("  ", " ")
        f_node.write(s)


# 保留指令和block
def reserve_2(n):
    inputFileDir = "./neww/"
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./reserve/reserve_2/" + str(n) + ".txt"
        f_node = open(nodes, "w")
        s = ''
        lines = f.readlines()
        i = 0
        for line in lines:
            list = line.split(" ")
            for i in list:
                if i[0:5] == "block":
                    s += i
                if i[0:1].isupper() != 0:
                    s += i
                s += ' '
            s += '\n'
        s = s.replace("  ", " ")
        print(s)
        # f_node.write(s)


# 保留地址，不保留block
def reserve_3(n):
    inputFileDir = "./new_binary_data/new_node/timestamp/"
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./reserve/reserve_3/timestamp/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, "w")
        s = ''
        lines = f.readlines()
        i = 0
        for line in lines:
            list = line.split(" ")
            for i in list:
                if i[0:2] == "0x":
                    s += i
                if i[0:1].isupper() != 0:
                    s += i
                s += ' '
            s += '\n'
        s = s.replace("  ", " ")
        print(s)
        f_node.write(s)


# 保留地址，保留block
def reserve_4(n):
    inputFileDir = "./neww/"
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./reserve/reserve_4/" + str(n) + ".txt"
        f_node = open(nodes, "w")
        s = ''
        lines = f.readlines()
        i = 0
        for line in lines:
            list = line.split(" ")
            for i in list:
                if i[0:5] == "block":
                    s += i
                if i[0:2] == "0x":
                    s += i
                if i[0:1].isupper() != 0:
                    s += i
                s += ' '
            s += '\n'
        s = s.replace("  ", " ")
        print(s)
        f_node.write(s)


# 将一个文件夹中的所有合成一个.txt,中间加空行
def combine():
    inputFileDir = "./reserve/reserve_3/only_bytecode/"
    dirs = os.listdir(inputFileDir)
    # dirs.sort(key=lambda x: int(x[:-4]))
    nodes = "./combine/" + "only_bytecode" + ".txt"
    f_node = open(nodes, 'w')
    s = ''
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        byte = f.read()
        s += byte
        s += '\n'
    print(s)
    f_node.write(s)


# 将一个文件夹中的所有合成一个.txt,中间加空行
def last_combine():
    inputFileDir = "./combine/"
    dirs = os.listdir(inputFileDir)
    # dirs.sort(key=lambda x: int(x[:-9]))
    nodes = "./last/" + "bert_node_train_data" + ".txt"
    f_node = open(nodes, 'w')
    s = ''
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        byte = f.read()
        s += byte
        s += '\n'
    print(s)
    f_node.write(s)


# 对vocab的操作
def vocab():
    nodes = "./" + "new_vocab1" + ".txt"
    f_node = open(nodes, 'w')
    s = ''
    with open('./new_vocab.txt') as f:
        s = f.read()
        # print(s)
        s = s.lower()
    print(s)
    f_node.write(s)


# 对vocab的操作
def ectract_0x():
    nodes = "./" + "new_vocab4" + ".txt"
    f_node = open(nodes, 'w')
    s = ''
    s1 = ''
    list = ['0', ' 1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for i in list:
        for j in list:
            s += '##'
            s += i
            s += j
            s += '\n'
    for i in list:
        for j in list:
            for k in list:
                s1 += '##'
                s1 += i
                s1 += j
                s1 += k
                s1 += '\n'
    for i in list:
        for j in list:
            for k in list:
                for m in list:
                    s1 += '0x'
                    s1 += i
                    s1 += j
                    s1 += k
                    s1 += m
                    s1 += '\n'
    # s = s + s1
    print(s1)
    f_node.write(s1)


# extract the pure bytecode
def bytecode(n):
    inputFileDir = "./bytecodes/integerovrflow_bytecode/"
    dirs = os.listdir(inputFileDir)
    print(dirs)
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./only_bytecode/timestamp_bytecodes/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, "w")
        s = ''
        lines = f.readlines()
        i = 0
        for line in lines:
            list = line.split(" ")
            for i in list:
                if i[0:4] == "6080":
                    s += i
        s = s.replace("  ", " ")
        print(s)
        f_node.write(s)


if __name__ == "__main__":
    n = 0
    # secondPhase->thirdPhase->reserve_
    # secondPhase(n)
    # thirdPhase(n)
    # reserve_1(n)
    # reserve_2(n)
    reserve_3(n)
    # reserve_4(n)
    # combine()
    # last_combine()
    # vocab()
    # ectract_0x()
    # bytecode(n)
    # timestamp_bytecode(n)

import os
import re


# obtain the specific line of the block
def firstPhase(n):
    inputFileDir = "./binary_cfg_code/delegatecall/"
    dirs = os.listdir(inputFileDir)
    # dirs.sort(key=lambda x: int(x[:-4]))
    print(dirs)
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r")
        lines = f.readlines()
        nodes = "./binary_graph_data/node/" + str(file)[0:-4] + ".txt"
        edges = "./binary_graph_data/edge/" + str(file)[0:-4] + ".txt"
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


# remove the symbols of '\l'
def secondPhase(n):
    inputFileDir = "./binary_graph_data/node/"
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./binary_graph_data/new_node/" + str(file)[0:-4] + ".txt"
        f_node = open(nodes, "w")
        lines = f.readlines()
        for line in lines:
            tt = re.sub(r'\\l', r' ', line)
            f_node.write(tt)


# reserve '0x' and remove 'block'
def thirdPhase(n):
    inputFileDir = "./binary_graph_data/new_node/"
    dirs = os.listdir(inputFileDir)
    dirs.sort(key=lambda x: int(x[:-4]))
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./binary_graph_data/new_node1/" + str(file)[0:-4] + ".txt"
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


# extract the pure bytecode
def extractPureBytecode(n):
    inputFileDir = "./bytecode/delegatecall/"
    dirs = os.listdir(inputFileDir)
    print(dirs)
    for file in dirs:
        inputFilePath = inputFileDir + file
        f = open(inputFilePath, "r+")
        n = n + 1
        nodes = "./binary_cfg_code/delegatecall/" + str(file)[0:-4] + ".txt"
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
    firstPhase(n)
    # secondPhase(n)
    # thirdPhase(n)
    # extractPureBytecode(n)

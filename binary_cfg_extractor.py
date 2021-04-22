import os
from binary_extractor.analysis.graph import CFGGraph
from binary_extractor.platforms.ETH.cfg import EthereumCFG
from shutil import copyfile


def main():
    fileList1 = os.listdir("./bytecode/integeroverflow/")
    fileList = []
    for file_name in fileList1:
        if '.txt' in file_name:
            fileList.append(file_name)

    currentpath = os.getcwd()

    for file_name in fileList:
        f = open('./bytecode/integeroverflow/' + file_name, 'r')

        # global bytecode_hex
        bytecode_hex = f.read()
        f.close()

        # create the CFG
        cfg = EthereumCFG(bytecode_hex)

        # generic visualization api
        graph = CFGGraph(cfg)
        graph.view()

        print(file_name + " is done!")

        os.chdir(currentpath)
        cfgList = os.listdir("./binary_cfg_code/integeroverflow/")
        cfgList.sort(key=lambda x: int(x[:-4]))

        if (str(file_name)[0:-4] + '.' + 'txt') not in cfgList:
            copyfile('./graph.cfg.gv',
                     './binary_cfg_code/integeroverflow/' + str(file_name)[0:-4] + '.' + 'txt')
            os.chdir("./binary_cfg_code/integeroverflow/")
            print(str(file_name)[0:-4])

        os.chdir(currentpath)


if __name__ == '__main__':
    main()

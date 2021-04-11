# BinaryCFGExtractor

**BinaryCFGExtractor is an automated tool for extracting binary code control flow graph (CFG).**

BinaryCFGExtractor, which is able to extract binary code control flow graph, provides an easy way to analyze smart contracts bytecode to understand deeper their internal behaviours,



## Features

- **Disassembler**: BinaryCFGExtractor can translate bytecode into binary code control flow graph, consists of blocks and control flow edges. 



## Requirements

BinaryCFGExtractor is supported on Linux (ideally Ubuntu 16.04) and requires Python >=3.5 (ideally 3.6).

Dependencies:
* Graph generation: [graphviz](https://graphviz.gitlab.io/download/)
* Explorer: [requests](http://docs.python-requests.org/en/master/#)
* Symbolic Execution: [z3-solver](https://pypi.org/project/z3-solver/)
* Wasm: [wasm](https://github.com/athre0z/wasm)



## Architecture
```shell
${BinaryCFGExtractor}
├── binary_cfg_code
│   ├── integeroverflow
│   ├── reentrancy
│   └── timestamp
├── binary_extractor
└── bytecode
    ├── integeroverflow
    ├── reentrancy
    └── timestamp
```

* `binary_cfg_code`: the binary code control flow graph consisting of blocks and edges that are extracted by the BinaryCFGExtractor.
* `binary_extractor`: the core code of the binary code control flow graph extractor.
* `bytecode`: the code complied from the source code of smart contract.



## Quick Start

- Install system dependencies
```
# Install system dependencies
sudo apt-get update && sudo apt-get install python-pip graphviz xdg-utils -y
```

- Install BinaryCFGExtractor
```
# Download BinaryCFGExtractor
git clone https://github.com/Messi-Q/BinaryCFGExtractor
```

- Run BinaryCFGExtractor
```
cd BinaryCFGExtractor
python3 evm_cfg.extractore.py
```

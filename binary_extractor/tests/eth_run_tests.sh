# echo '[*] ETH Explorer [*]'
# python3 -m unittest binary2assembly/tests/ETH/test_explorer.py
echo '[*] ETH Disassembler [*]'
python3 -m unittest ETH/test_disassembler.py
echo '[*] ETH ControlFlowGraph analysis [*]'
python3 -m unittest ETH/test_cfg.py
# -*- coding: utf-8 -*-
import sys, os
from .parser import Parser
from .renderer import render

def render_file(inp_path, out_path):
    text = open(inp_path, 'r', encoding='utf-8').read()
    p = Parser(text)
    nodes = p.parse()
    html = render(nodes)
    open(out_path, 'w', encoding='utf-8').write(html)
    print('Wrote', out_path)

def main():
    if len(sys.argv) < 4:
        print('Usage: python -m aneez.cli render input.aneez output.html')
        return
    cmd = sys.argv[1]
    if cmd == 'render':
        inp = sys.argv[2]; out = sys.argv[3]
        render_file(inp, out)
    else:
        print('Unknown command', cmd)

if __name__ == '__main__':
    main()

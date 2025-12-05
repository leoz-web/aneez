from aneez.parser import Parser
from aneez.renderer import render

def test_render_example():
    txt = open('examples/example.aneez','r',encoding='utf-8').read()
    p = Parser(txt)
    nodes = p.parse()
    out = render(nodes)
    assert '<header' in out
    assert 'تطبيقي الجميل' in out

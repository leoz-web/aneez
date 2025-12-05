# -*- coding: utf-8 -*-
from .ast import Element, Text
import html
from . import elements as elems

def escape(s):
    return html.escape(s)

def render_children(children):
    out = []
    for c in children:
        if isinstance(c, Text):
            out.append(escape(c.text))
        elif isinstance(c, Element):
            out.append(render_element(c))
    return ''.join(out)

def render_element(elem):
    name = elem.name.strip()
    # map to element renderers
    mapping = {
        'رأس': elems.render_رأس,
        'اسم تطبيق الويب': elems.render_اسم_تطبيق_الويب,
        'الشريط العلوي': elems.render_الشريط_العلي if False else elems.render_الشريط_العلوي,
        'جسم': elems.render_جسم,
        'قائمة': elems.render_قائمة,
        'بطاقة': elems.render_بطاقة,
        'زر': elems.render_زر,
        'نموذج': elems.render_نموذج,
        'صورة': elems.render_صورة,
        'قسم': elems.render_قسم,
        'تذييل': elems.render_تذييل,
    }
    if name in mapping:
        return mapping[name](elem, render_children)
    if name == 'style':
        return f'<style>{render_children(elem.children)}</style>'
    # default
    inner = render_children(elem.children)
    return f'<div data-aneez-tag="{escape(name)}">{inner}</div>'

def render(nodes):
    parts = []
    head_elems = []
    body_parts = []
    for n in nodes:
        if isinstance(n, Element) and n.name == 'رأس':
            head_elems.append(render_element(n))
        else:
            body_parts.append(render_element(n) if isinstance(n, Element) else escape(n.text))
    head_html = '\n'.join(head_elems)
    body_html = '\n'.join(body_parts)
    html_out = ('<!doctype html>\n<html lang="ar">\n<head>\n'
                '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
                f'{head_html}\n</head>\n<body dir="rtl">\n{body_html}\n</body>\n</html>')
    return html_out

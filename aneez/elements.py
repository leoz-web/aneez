# -*- coding: utf-8 -*-
# Element helpers to be used by renderer for mapping semantic elements to HTML snippets.
# Each function receives (elem: Element) and should return HTML string.

def render_رأس(elem, render_children):
    # Support .عنوان(), .وصف(), .كلمات() inside children as text nodes
    title = ''
    desc = ''
    keywords = ''
    for c in elem.children:
        t = getattr(c, 'text', '')
        if t.startswith('عنوان:'):
            title = t.split(':',1)[1].strip()
        elif t.startswith('وصف:'):
            desc = t.split(':',1)[1].strip()
        elif t.startswith('كلمات:'):
            keywords = t.split(':',1)[1].strip()
    head = []
    if title:
        head.append(f'<title>{title}</title>')
        head.append(f'<meta name="description" content="{desc}">')
        head.append(f'<meta name="keywords" content="{keywords}">')
    return '\n'.join(head)

def render_اسم_تطبيق_الويب(elem, render_children):
    inner = render_children(elem.children)
    return f'<h1 class="aneez-title">{inner}</h1>'

def render_الشريط_العلوي(elem, render_children):
    return f'<header class="aneez-top">{render_children(elem.children)}</header>'

def render_جسم(elem, render_children):
    return f'<main class="aneez-body">{render_children(elem.children)}</main>'

def render_قائمة(elem, render_children):
    # children expected to be Text nodes like 'عنصر:الاسم|/url'
    items = []
    for c in elem.children:
        t = getattr(c, 'text', '')
        if t.startswith('عنصر:'):
            parts = t.split(':',1)[1].split('|')
            label = parts[0].strip()
            href = parts[1].strip() if len(parts)>1 else '#'
            items.append(f'<li><a href="{href}">{label}</a></li>')
    return '<nav class="aneez-menu"><ul>' + ''.join(items) + '</ul></nav>'

def render_بطاقة(elem, render_children):
    inner = render_children(elem.children)
    return f'<div class="aneez-card">{inner}</div>'

def render_زر(elem, render_children):
    # button text or attributes: 'نص:...','لون:#...'
    text = 'زر'
    style = ''
    for c in elem.children:
        t = getattr(c, 'text', '')
        if t.startswith('نص:'):
            text = t.split(':',1)[1].strip()
        if t.startswith('لون:'):
            style = f'style="background:{t.split(':',1)[1].strip()};"'
    return f'<button class="aneez-btn" {style}>{text}</button>'

def render_نموذج(elem, render_children):
    inner = render_children(elem.children)
    return f'<form class="aneez-form">{inner}</form>'

def render_صورة(elem, render_children):
    src = elem.attrs.get('src','')
    w = elem.attrs.get('width','')
    h = elem.attrs.get('height','')
    attrs = ''
    if src: attrs += f' src="{src}"'
    if w: attrs += f' width="{w}"'
    if h: attrs += f' height="{h}"'
    return f'<img class="aneez-img"{attrs} />'

def render_قسم(elem, render_children):
    return f'<section class="aneez-section">{render_children(elem.children)}</section>'

def render_تذييل(elem, render_children):
    return f'<footer class="aneez-footer">{render_children(elem.children)}</footer>'

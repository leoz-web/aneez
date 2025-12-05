# -*- coding: utf-8 -*-
class Node:
    pass

class Element(Node):
    def __init__(self, name, attrs=None, children=None):
        self.name = name
        self.attrs = attrs or {}
        self.children = children or []

    def __repr__(self):
        return f'Element({self.name!r}, attrs={self.attrs}, children={len(self.children)})'

class Text(Node):
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Text({self.text!r})'

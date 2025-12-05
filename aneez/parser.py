# -*- coding: utf-8 -*-
from .lexer import tokenize
from .ast import Element, Text

class Parser:
    def __init__(self, text):
        self.tokens = list(tokenize(text))
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        t = self.peek()
        if t:
            self.pos += 1
        return t

    def parse(self):
        nodes = []
        while self.peek():
            node = self.parse_node()
            if node is not None:
                nodes.append(node)
        return nodes

    def parse_node(self):
        tok = self.peek()
        if tok is None:
            return None
        if tok.type == 'TEXT':
            self.consume()
            text = tok.value.strip()
            if not text:
                return None
            return Text(text)
        if tok.type == 'TAG_OPEN':
            _, attrs = tok.value
            name = tok.value[0]
            self.consume()
            children = []
            while True:
                nxt = self.peek()
                if nxt is None:
                    break
                if nxt.type == 'TAG_CLOSE' and nxt.value == name:
                    self.consume()
                    break
                child = self.parse_node()
                if child is not None:
                    children.append(child)
            return Element(name, attrs, children)
        if tok.type == 'TAG_SELF':
            name, attrs = tok.value
            self.consume()
            return Element(name, attrs, [])
        if tok.type == 'TAG_CLOSE':
            # stray close
            self.consume()
            return None
        return None

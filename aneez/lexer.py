# -*- coding: utf-8 -*-
import re
from collections import namedtuple

Token = namedtuple('Token', ['type','value'])

TAG_OPEN = re.compile(r'<([@A-Za-z\u0600-\u06FF0-9_\- ]+)(?:\s+[^>]*)?>', re.UNICODE)
TAG_CLOSE = re.compile(r'</([@A-Za-z\u0600-\u06FF0-9_\- ]+)>', re.UNICODE)
TAG_SELF = re.compile(r'<([@A-Za-z\u0600-\u06FF0-9_\- ]+)(?:\s+[^>]*)?/>', re.UNICODE)
ATTRS = re.compile(r'([A-Za-z؀-ۿ0-9_\-]+)\s*=\s*"([^"]*)"', re.UNICODE)
NASS_PATTERN = re.compile(r'\.نص\((.*?)\)', re.UNICODE | re.DOTALL)

def tokenize(text):
    pos = 0
    length = len(text)
    while pos < length:
        m_self = TAG_SELF.match(text, pos)
        m_open = TAG_OPEN.match(text, pos)
        m_close = TAG_CLOSE.match(text, pos)
        m_nass = NASS_PATTERN.match(text, pos)
        if m_self:
            tag = m_self.group(1).strip()
            attrs_raw = text[m_self.start():m_self.end()]
            attrs = dict(ATTRS.findall(attrs_raw))
            yield Token('TAG_SELF', (tag, attrs))
            pos = m_self.end()
        elif m_open:
            tag = m_open.group(1).strip()
            attrs_raw = text[m_open.start():m_open.end()]
            attrs = dict(ATTRS.findall(attrs_raw))
            yield Token('TAG_OPEN', (tag, attrs))
            pos = m_open.end()
        elif m_close:
            tag = m_close.group(1).strip()
            yield Token('TAG_CLOSE', tag)
            pos = m_close.end()
        elif m_nass:
            yield Token('TEXT', m_nass.group(1).strip())
            pos = m_nass.end()
        else:
            # read until next special
            nxt = min([i for i in [text.find('<', pos), text.find('.نص(', pos)] if i!=-1] + [length])
            chunk = text[pos:nxt]
            if chunk.strip():
                yield Token('TEXT', chunk)
            pos = nxt

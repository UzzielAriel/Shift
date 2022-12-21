from tokens import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ctok = self.tokens[self.pos]

    def advance(self):
        if self.pos + 1 < len(self.tokens):
            self.pos += 1
            self.ctok = self.tokens[self.pos]

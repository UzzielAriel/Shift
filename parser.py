from tokens import *

class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'


class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.right_node = right_node
        self.op_tok = op_tok

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_tok = self.tokens[self.pos]

    def advance(self):
        if self.pos + 1 < len(self.tokens):
            self.pos += 1
            self.current_tok = self.tokens[self.pos]

    def parse(self):
        res = self.expr()
        return res

    def term(self):
        return self.bin_op(self.factor, (TokenType.MUL, TokenType.DIV))

    def bin_op(self, func, ops):
        left = func()

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            self.advance()
            right = self.factor()
            left = BinOpNode(left, op_tok, right)
        return left

    def expr(self):
        return self.bin_op(self.term, (TokenType.ADD, TokenType.SUB))

    def factor(self):
        tok = self.current_tok
        if tok.type in (TokenType.INT, TokenType.FLOAT):
            self.advance()
            return NumberNode(tok)
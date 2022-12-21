from enum import Enum


class Token:
    integers = '0123456789'

    def __init__(self, type, ln, col, lexeme):
        self.type = type
        self.ln = ln
        self.col = col
        self.lexeme = lexeme

    def __repr__(self):
        return f'(TOKEN: {self.type}: \'{self.lexeme}\', {self.ln}:{self.col})'


class TokenType(Enum):
    NULL = 0
    INT = 8
    FLOAT = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    EOF = 7
    LPAR = 9
    RPAR = 10

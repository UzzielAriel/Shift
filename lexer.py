import sys
from tokens import *
from parser import *


class Pos:
    def __init__(self):
        self.col = 0
        self.pos = 0
        self.ln = 1

    def advance(self):
        self.col += 1
        self.pos += 1

    def lnAdvance(self):
        self.ln += 1
        self.col = 0


class Lexer:
    def __init__(self, filename):
        self.src = list(''.join(open(filename, 'r').readlines()))
        self.src.append('\0')
        self.pos = Pos()
        self.tokens = []
        self.chr = self.src[self.pos.pos]

    def advance(self):
        if self.pos.pos + 1 < len(self.src):
            self.pos.advance()
            self.chr = self.src[self.pos.pos]
        else:
            self.tokens.append(
                Token(TokenType.EOF, self.pos.ln, self.pos.col, '\\0'))
            self.chr = None

    def tokenizer(self):
        while self.chr != None:
            if self.chr == '\n':
                self.pos.lnAdvance()
            elif self.chr in ' \t':
                self.advance()
            elif self.chr == '+':
                self.tokens.append(
                    Token(TokenType.ADD, self.pos.ln, self.pos.col, '+'))
                self.advance()
            elif self.chr == '-':
                self.tokens.append(
                    Token(TokenType.SUB, self.pos.ln, self.pos.col, '-'))
                self.advance()
            elif self.chr == '/':
                self.tokens.append(
                    Token(TokenType.DIV, self.pos.ln, self.pos.col, '/'))
                self.advance()
            elif self.chr == '*':
                self.tokens.append(
                    Token(TokenType.MUL, self.pos.ln, self.pos.col, '*'))
                self.advance()
            elif self.chr in Token.integers:
                self.makeNumber()
            elif self.chr == '(':
                self.tokens.append(
                    Token(TokenType.LPAR, self.pos.ln, self.pos.col, '('))
                self.advance()
            elif self.chr == ')':
                self.tokens.append(
                    Token(TokenType.RPAR, self.pos.ln, self.pos.col, ')'))
                self.advance()
            else:
                self.advance()

        return self.tokens

    def makeNumber(self):
        pos = self.pos
        dot_count = 0
        number = ''
        while self.chr != None and self.chr in Token.integers + '.':
            number += self.chr
            if self.chr == '.':
                dot_count += 1
            self.advance()
        if dot_count == 0:
            self.tokens.append(
                Token(TokenType.INT, pos.ln, pos.col, int(number)))
        elif dot_count == 1:
            self.tokens.append(
                Token(TokenType.FLOAT, pos.ln, pos.col, float(number)))


if (__name__ == "__main__" and not (len(sys.argv) < 2)):
    lexer = Lexer(sys.argv[1])
    print(lexer.tokenizer())

else:
    print("""\

		Usage: python3 lexer.py filename.sft

	""")

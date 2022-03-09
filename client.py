from antlr4 import *
from marzo.marzoParser import marzoParser


import sys

def GenCode(marzoListener):
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")

    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        print("load $1, " + ctx.Numero)

    def exitSuma(self, ctx:marzoParser.SumaContext):
        print("ADD")

def main():
    parser = marzoParser(CommonTokenStream(marzoLexer(FileStream("input.txt"))))
    tree = parser.program()



    gencode = GenCode()
    walker = ParseTreeWalker()
    walker.walk(gencode, tree)


if __name__ == '__main__':
    main()
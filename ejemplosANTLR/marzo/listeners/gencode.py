from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

import asm

class GenCode(marzoListener):
    def __init__(self):
        self.r = ''
        self.stack = []
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        self.r += asm.tpl_start;
    
    def exitProgram(self, ctx: marzoParser.ProgramContext):
        self.r += self.stack.pop()
        self.r += asm.tpl_end

    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        self.stack.append(
            asm.tpl_immediate.substitute(immediate=ctx.getText())
            )

    def exitSuma(self, ctx:marzoParser.SumaContext):
        self.stack.append(
            asm.tpl_suma.substitute(
                right=self.stack.pop(), 
                left=self.stack.pop())
                )
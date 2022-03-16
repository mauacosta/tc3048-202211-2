from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

import asm


class DataGenerator(marzoListener):
    def enterProgram(self, ctx: marzoParser.ProgramContext):
        return super().enterProgram(ctx)

    def enterDeclaracion(self, ctx: marzoParser.DeclaracionContext):
        return

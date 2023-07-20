# Generated from PL.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PLParser import PLParser
else:
    from PLParser import PLParser

# This class defines a complete generic visitor for a parse tree produced by PLParser.

class PLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLParser#program.
    def visitProgram(self, ctx:PLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Tell.
    def visitTell(self, ctx:PLParser.TellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Ask.
    def visitAsk(self, ctx:PLParser.AskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Remove.
    def visitRemove(self, ctx:PLParser.RemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#HornTell.
    def visitHornTell(self, ctx:PLParser.HornTellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#HornAsk.
    def visitHornAsk(self, ctx:PLParser.HornAskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#HornProper.
    def visitHornProper(self, ctx:PLParser.HornProperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#HornSingle.
    def visitHornSingle(self, ctx:PLParser.HornSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#hornClauseHead.
    def visitHornClauseHead(self, ctx:PLParser.HornClauseHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#hornClauseTail.
    def visitHornClauseTail(self, ctx:PLParser.HornClauseTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Disjunction.
    def visitDisjunction(self, ctx:PLParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#TruthLiteral.
    def visitTruthLiteral(self, ctx:PLParser.TruthLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Negation.
    def visitNegation(self, ctx:PLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Nested.
    def visitNested(self, ctx:PLParser.NestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Conjunction.
    def visitConjunction(self, ctx:PLParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Biconditional.
    def visitBiconditional(self, ctx:PLParser.BiconditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Implication.
    def visitImplication(self, ctx:PLParser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#Atom.
    def visitAtom(self, ctx:PLParser.AtomContext):
        return self.visitChildren(ctx)



del PLParser
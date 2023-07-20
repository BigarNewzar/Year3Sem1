from plast import *

from parser.PLParser import *
from parser.PLVisitor import PLVisitor

class PLInterpreter(PLVisitor):
    def __init__(self, ctx):
        self.__ctx = ctx


    def visit(self, tree):
        if isinstance(tree, PLParser.HornClauseContext):
            return self.visitHornClause(tree)
        elif isinstance(tree, PLParser.NegationContext):
            return self.visitNegation(tree)
        elif isinstance(tree, PLParser.AtomContext):
            return self.visitAtom(tree)
        elif isinstance(tree, PLParser.NestedContext):
            return self.visitNested(tree)
        elif isinstance(tree, PLParser.ConjunctionContext):
            return self.visitConjunction(tree)
        elif isinstance(tree, PLParser.DisjunctionContext):
            return self.visitDisjunction(tree)
        elif isinstance(tree, PLParser.ImplicationContext):
            return self.visitImplication(tree)
        elif isinstance(tree, PLParser.BiconditionalContext):
            return self.visitBiconditional(tree)


    def visitProgram(self, ctx: PLParser.ProgramContext):
        statcount = ctx.getChildCount()
        i = 0
        while i < statcount:
            stat = ctx.getChild(i)
            if isinstance(stat, PLParser.HornTellContext):
                self.visitHornTell(stat)
            elif isinstance(stat, PLParser.HornAskContext):
                self.visitHornAsk(stat)
            elif isinstance(stat, PLParser.TellContext):
                self.visitTell(stat)
            elif isinstance(stat, PLParser.AskContext):
                self.visitAsk(stat)
            i += 1

    def visitHornTell(self, ctx:PLParser.HornTellContext):
        i = 0
        sen = ctx.hornClause(i)
        while sen is not None:
            self.__ctx.tell(self.visitHornClause(sen))
            i += 1
            sen = ctx.hornClause(i)


    def visitHornAsk(self, ctx:PLParser.HornAskContext):
        if ctx.query is not None:
            self.__ctx.ask(self.visitAtom(ctx.SYMBOL()))


    def visitTell(self, ctx:PLParser.TellContext):
        sencount = ctx.getChildCount()
        i = 0
        while i < sencount:
            sen = ctx.getChild(i)
            if isinstance(sen, PLParser.SentenceContext):
                self.__ctx.tell(self.visit(sen))
            i += 1


    def visitAsk(self, ctx:PLParser.AskContext):
        if ctx.sentence() is not None:
            self.__ctx.ask(self.visit(ctx.sentence()))


    def visitAtom(self, ctx:PLParser.AtomContext):
        result = AtomExpression(ctx.getText())
        self.__ctx.know(result)
        return result


    def visitBiconditional(self, ctx:PLParser.BiconditionalContext):
        return BiconditionalExpression(self.visit(ctx.lhs), self.visit(ctx.rhs))


    def visitNested(self, ctx:PLParser.NestedContext):
        return self.visit(ctx.sentence())


    def visitConjunction(self, ctx:PLParser.ConjunctionContext):
        return ConjunctionExpression(self.visit(ctx.lhs), self.visit(ctx.rhs))


    def visitDisjunction(self, ctx:PLParser.DisjunctionContext):
        return DisjunctionExpression(self.visit(ctx.lhs), self.visit(ctx.rhs))


    def visitNegation(self, ctx:PLParser.NegationContext):
        return NegationExpression(self.visit(ctx.sentence()))


    def visitImplication(self, ctx:PLParser.ImplicationContext):
        return ImplicationExpression(self.visit(ctx.lhs), self.visit(ctx.rhs))


    def visitHornClauseHead(self, ctx:PLParser.HornClauseHeadContext):
        i = 0
        result = set()
        sym = ctx.SYMBOL(i)
        while sym is not None:
            result.add(self.visitAtom(sym))
            i += 1
            sym = ctx.SYMBOL(i)
        return result

    def visitHornClause(self, ctx:PLParser.HornClauseContext):
        if isinstance(ctx, PLParser.HornSingleContext):
            return self.visitAtom(ctx.SYMBOL())
        else:
            head = ctx.hornClauseHead()
            tail = ctx.hornClauseTail()
            return HornClause(self.visitHornClauseHead(head), self.visitAtom(tail))

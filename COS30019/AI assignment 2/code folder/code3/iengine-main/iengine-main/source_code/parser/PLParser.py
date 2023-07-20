# Generated from PL.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,5,0,24,8,0,10,0,12,
        0,27,9,0,3,0,29,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,
        12,1,41,9,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,2,1,2,1,2,1,2,1,
        2,5,2,56,8,2,10,2,12,2,59,9,2,1,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,3,
        1,3,1,3,1,3,1,3,3,3,73,8,3,1,4,1,4,1,4,5,4,78,8,4,10,4,12,4,81,9,
        4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,93,8,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,107,8,6,10,6,12,6,110,9,
        6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,0,121,0,28,1,0,0,0,2,48,1,0,0,0,
        4,65,1,0,0,0,6,72,1,0,0,0,8,74,1,0,0,0,10,82,1,0,0,0,12,92,1,0,0,
        0,14,17,3,4,2,0,15,17,5,12,0,0,16,14,1,0,0,0,16,15,1,0,0,0,17,20,
        1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,29,1,0,0,0,20,18,1,0,0,0,
        21,24,3,2,1,0,22,24,5,12,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,27,1,
        0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,28,
        18,1,0,0,0,28,25,1,0,0,0,29,30,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,
        0,32,33,5,1,0,0,33,39,5,12,0,0,34,35,3,12,6,0,35,36,5,2,0,0,36,38,
        1,0,0,0,37,34,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,
        40,42,1,0,0,0,41,39,1,0,0,0,42,49,5,12,0,0,43,44,5,3,0,0,44,45,5,
        12,0,0,45,46,3,12,6,0,46,47,5,12,0,0,47,49,1,0,0,0,48,32,1,0,0,0,
        48,43,1,0,0,0,49,3,1,0,0,0,50,51,5,1,0,0,51,57,5,12,0,0,52,53,3,
        6,3,0,53,54,5,2,0,0,54,56,1,0,0,0,55,52,1,0,0,0,56,59,1,0,0,0,57,
        55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,66,5,12,
        0,0,61,62,5,3,0,0,62,63,5,12,0,0,63,64,5,6,0,0,64,66,5,12,0,0,65,
        50,1,0,0,0,65,61,1,0,0,0,66,5,1,0,0,0,67,68,3,8,4,0,68,69,5,10,0,
        0,69,70,3,10,5,0,70,73,1,0,0,0,71,73,5,6,0,0,72,67,1,0,0,0,72,71,
        1,0,0,0,73,7,1,0,0,0,74,79,5,6,0,0,75,76,5,7,0,0,76,78,5,6,0,0,77,
        75,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,9,1,0,0,
        0,81,79,1,0,0,0,82,83,5,6,0,0,83,11,1,0,0,0,84,85,6,6,-1,0,85,86,
        5,4,0,0,86,87,3,12,6,0,87,88,5,5,0,0,88,93,1,0,0,0,89,90,5,9,0,0,
        90,93,3,12,6,6,91,93,5,6,0,0,92,84,1,0,0,0,92,89,1,0,0,0,92,91,1,
        0,0,0,93,108,1,0,0,0,94,95,10,5,0,0,95,96,5,7,0,0,96,107,3,12,6,
        6,97,98,10,4,0,0,98,99,5,8,0,0,99,107,3,12,6,5,100,101,10,3,0,0,
        101,102,5,10,0,0,102,107,3,12,6,4,103,104,10,2,0,0,104,105,5,11,
        0,0,105,107,3,12,6,3,106,94,1,0,0,0,106,97,1,0,0,0,106,100,1,0,0,
        0,106,103,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,
        0,109,13,1,0,0,0,110,108,1,0,0,0,14,16,18,23,25,28,39,48,57,65,72,
        79,92,106,108
    ]

class PLParser ( Parser ):

    grammarFileName = "PL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TELL'", "';'", "'ASK'", "'('", "')'", 
                     "<INVALID>", "'&'", "'||'", "'~'", "'=>'", "'<=>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SYMBOL", "CONJUNCTION", 
                      "DISJUNCTION", "NEGATION", "IMPLICATION", "BICONDITIONAL", 
                      "NEWLINE", "WHITESPACE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_hornStatement = 2
    RULE_hornClause = 3
    RULE_hornClauseHead = 4
    RULE_hornClauseTail = 5
    RULE_sentence = 6

    ruleNames =  [ "program", "statement", "hornStatement", "hornClause", 
                   "hornClauseHead", "hornClauseTail", "sentence" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    SYMBOL=6
    CONJUNCTION=7
    DISJUNCTION=8
    NEGATION=9
    IMPLICATION=10
    BICONDITIONAL=11
    NEWLINE=12
    WHITESPACE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PLParser.EOF, 0)

        def hornStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLParser.HornStatementContext)
            else:
                return self.getTypedRuleContext(PLParser.HornStatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PLParser.NEWLINE)
            else:
                return self.getToken(PLParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLParser.StatementContext,i)


        def getRuleIndex(self):
            return PLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4106) != 0):
                    self.state = 16
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3]:
                        self.state = 14
                        self.hornStatement()
                        pass
                    elif token in [12]:
                        self.state = 15
                        self.match(PLParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 20
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4106) != 0):
                    self.state = 23
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3]:
                        self.state = 21
                        self.statement()
                        pass
                    elif token in [12]:
                        self.state = 22
                        self.match(PLParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 30
            self.match(PLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TellContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PLParser.NEWLINE)
            else:
                return self.getToken(PLParser.NEWLINE, i)
        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLParser.SentenceContext)
            else:
                return self.getTypedRuleContext(PLParser.SentenceContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTell" ):
                return visitor.visitTell(self)
            else:
                return visitor.visitChildren(self)


    class AskContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PLParser.NEWLINE)
            else:
                return self.getToken(PLParser.NEWLINE, i)
        def sentence(self):
            return self.getTypedRuleContext(PLParser.SentenceContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsk" ):
                return visitor.visitAsk(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = PLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PLParser.TellContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(PLParser.T__0)
                self.state = 33
                self.match(PLParser.NEWLINE)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 592) != 0):
                    self.state = 34
                    self.sentence(0)
                    self.state = 35
                    self.match(PLParser.T__1)
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.match(PLParser.NEWLINE)
                pass
            elif token in [3]:
                localctx = PLParser.AskContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(PLParser.T__2)
                self.state = 44
                self.match(PLParser.NEWLINE)
                self.state = 45
                self.sentence(0)
                self.state = 46
                self.match(PLParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HornStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLParser.RULE_hornStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HornTellContext(HornStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.HornStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PLParser.NEWLINE)
            else:
                return self.getToken(PLParser.NEWLINE, i)
        def hornClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLParser.HornClauseContext)
            else:
                return self.getTypedRuleContext(PLParser.HornClauseContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHornTell" ):
                return visitor.visitHornTell(self)
            else:
                return visitor.visitChildren(self)


    class HornAskContext(HornStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.HornStatementContext
            super().__init__(parser)
            self.query = None # Token
            self.copyFrom(ctx)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PLParser.NEWLINE)
            else:
                return self.getToken(PLParser.NEWLINE, i)
        def SYMBOL(self):
            return self.getToken(PLParser.SYMBOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHornAsk" ):
                return visitor.visitHornAsk(self)
            else:
                return visitor.visitChildren(self)



    def hornStatement(self):

        localctx = PLParser.HornStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_hornStatement)
        self._la = 0 # Token type
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PLParser.HornTellContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(PLParser.T__0)
                self.state = 51
                self.match(PLParser.NEWLINE)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 52
                    self.hornClause()
                    self.state = 53
                    self.match(PLParser.T__1)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self.match(PLParser.NEWLINE)
                pass
            elif token in [3]:
                localctx = PLParser.HornAskContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(PLParser.T__2)
                self.state = 62
                self.match(PLParser.NEWLINE)
                self.state = 63
                localctx.query = self.match(PLParser.SYMBOL)
                self.state = 64
                self.match(PLParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HornClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLParser.RULE_hornClause

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HornProperContext(HornClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.HornClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def hornClauseHead(self):
            return self.getTypedRuleContext(PLParser.HornClauseHeadContext,0)

        def IMPLICATION(self):
            return self.getToken(PLParser.IMPLICATION, 0)
        def hornClauseTail(self):
            return self.getTypedRuleContext(PLParser.HornClauseTailContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHornProper" ):
                return visitor.visitHornProper(self)
            else:
                return visitor.visitChildren(self)


    class HornSingleContext(HornClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.HornClauseContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def SYMBOL(self):
            return self.getToken(PLParser.SYMBOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHornSingle" ):
                return visitor.visitHornSingle(self)
            else:
                return visitor.visitChildren(self)



    def hornClause(self):

        localctx = PLParser.HornClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_hornClause)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = PLParser.HornProperContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.hornClauseHead()
                self.state = 68
                self.match(PLParser.IMPLICATION)
                self.state = 69
                self.hornClauseTail()
                pass

            elif la_ == 2:
                localctx = PLParser.HornSingleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                localctx.atom = self.match(PLParser.SYMBOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HornClauseHeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(PLParser.SYMBOL)
            else:
                return self.getToken(PLParser.SYMBOL, i)

        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(PLParser.CONJUNCTION)
            else:
                return self.getToken(PLParser.CONJUNCTION, i)

        def getRuleIndex(self):
            return PLParser.RULE_hornClauseHead

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHornClauseHead" ):
                return visitor.visitHornClauseHead(self)
            else:
                return visitor.visitChildren(self)




    def hornClauseHead(self):

        localctx = PLParser.HornClauseHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_hornClauseHead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(PLParser.SYMBOL)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 75
                self.match(PLParser.CONJUNCTION)
                self.state = 76
                self.match(PLParser.SYMBOL)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HornClauseTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self):
            return self.getToken(PLParser.SYMBOL, 0)

        def getRuleIndex(self):
            return PLParser.RULE_hornClauseTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHornClauseTail" ):
                return visitor.visitHornClauseTail(self)
            else:
                return visitor.visitChildren(self)




    def hornClauseTail(self):

        localctx = PLParser.HornClauseTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hornClauseTail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(PLParser.SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLParser.RULE_sentence

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DisjunctionContext(SentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.SentenceContext
            super().__init__(parser)
            self.lhs = None # SentenceContext
            self.rhs = None # SentenceContext
            self.copyFrom(ctx)

        def DISJUNCTION(self):
            return self.getToken(PLParser.DISJUNCTION, 0)
        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLParser.SentenceContext)
            else:
                return self.getTypedRuleContext(PLParser.SentenceContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction" ):
                return visitor.visitDisjunction(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(SentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.SentenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEGATION(self):
            return self.getToken(PLParser.NEGATION, 0)
        def sentence(self):
            return self.getTypedRuleContext(PLParser.SentenceContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class NestedContext(SentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.SentenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sentence(self):
            return self.getTypedRuleContext(PLParser.SentenceContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested" ):
                return visitor.visitNested(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionContext(SentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.SentenceContext
            super().__init__(parser)
            self.lhs = None # SentenceContext
            self.rhs = None # SentenceContext
            self.copyFrom(ctx)

        def CONJUNCTION(self):
            return self.getToken(PLParser.CONJUNCTION, 0)
        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLParser.SentenceContext)
            else:
                return self.getTypedRuleContext(PLParser.SentenceContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)


    class BiconditionalContext(SentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.SentenceContext
            super().__init__(parser)
            self.lhs = None # SentenceContext
            self.rhs = None # SentenceContext
            self.copyFrom(ctx)

        def BICONDITIONAL(self):
            return self.getToken(PLParser.BICONDITIONAL, 0)
        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLParser.SentenceContext)
            else:
                return self.getTypedRuleContext(PLParser.SentenceContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiconditional" ):
                return visitor.visitBiconditional(self)
            else:
                return visitor.visitChildren(self)


    class ImplicationContext(SentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.SentenceContext
            super().__init__(parser)
            self.lhs = None # SentenceContext
            self.rhs = None # SentenceContext
            self.copyFrom(ctx)

        def IMPLICATION(self):
            return self.getToken(PLParser.IMPLICATION, 0)
        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLParser.SentenceContext)
            else:
                return self.getTypedRuleContext(PLParser.SentenceContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplication" ):
                return visitor.visitImplication(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(SentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.SentenceContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def SYMBOL(self):
            return self.getToken(PLParser.SYMBOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def sentence(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PLParser.SentenceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_sentence, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = PLParser.NestedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 85
                self.match(PLParser.T__3)
                self.state = 86
                self.sentence(0)
                self.state = 87
                self.match(PLParser.T__4)
                pass
            elif token in [9]:
                localctx = PLParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(PLParser.NEGATION)
                self.state = 90
                self.sentence(6)
                pass
            elif token in [6]:
                localctx = PLParser.AtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                localctx.atom = self.match(PLParser.SYMBOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 106
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = PLParser.ConjunctionContext(self, PLParser.SentenceContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sentence)
                        self.state = 94
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 95
                        self.match(PLParser.CONJUNCTION)
                        self.state = 96
                        localctx.rhs = self.sentence(6)
                        pass

                    elif la_ == 2:
                        localctx = PLParser.DisjunctionContext(self, PLParser.SentenceContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sentence)
                        self.state = 97
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 98
                        self.match(PLParser.DISJUNCTION)
                        self.state = 99
                        localctx.rhs = self.sentence(5)
                        pass

                    elif la_ == 3:
                        localctx = PLParser.ImplicationContext(self, PLParser.SentenceContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sentence)
                        self.state = 100
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 101
                        self.match(PLParser.IMPLICATION)
                        self.state = 102
                        localctx.rhs = self.sentence(4)
                        pass

                    elif la_ == 4:
                        localctx = PLParser.BiconditionalContext(self, PLParser.SentenceContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sentence)
                        self.state = 103
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 104
                        self.match(PLParser.BICONDITIONAL)
                        self.state = 105
                        localctx.rhs = self.sentence(3)
                        pass

             
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.sentence_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def sentence_sempred(self, localctx:SentenceContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





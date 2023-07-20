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
        4,1,15,120,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,5,0,24,8,0,10,0,12,
        0,27,9,0,3,0,29,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,
        12,1,41,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,54,8,
        1,1,2,1,2,1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,2,1,2,1,
        2,3,2,70,8,2,1,2,3,2,73,8,2,1,3,1,3,1,3,1,3,1,3,3,3,80,8,3,1,4,1,
        4,1,4,5,4,85,8,4,10,4,12,4,88,9,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,101,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,5,6,115,8,6,10,6,12,6,118,9,6,1,6,0,1,12,7,0,2,4,6,8,10,
        12,0,1,1,0,7,8,132,0,28,1,0,0,0,2,53,1,0,0,0,4,72,1,0,0,0,6,79,1,
        0,0,0,8,81,1,0,0,0,10,89,1,0,0,0,12,100,1,0,0,0,14,17,3,4,2,0,15,
        17,5,14,0,0,16,14,1,0,0,0,16,15,1,0,0,0,17,20,1,0,0,0,18,16,1,0,
        0,0,18,19,1,0,0,0,19,29,1,0,0,0,20,18,1,0,0,0,21,24,3,2,1,0,22,24,
        5,14,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,28,18,1,0,0,0,28,25,1,
        0,0,0,29,30,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,33,5,1,0,0,33,
        39,5,14,0,0,34,35,3,12,6,0,35,36,5,2,0,0,36,38,1,0,0,0,37,34,1,0,
        0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,
        1,0,0,0,42,54,5,14,0,0,43,44,5,3,0,0,44,45,5,14,0,0,45,46,3,12,6,
        0,46,47,5,14,0,0,47,54,1,0,0,0,48,49,5,4,0,0,49,50,5,14,0,0,50,51,
        3,12,6,0,51,52,5,14,0,0,52,54,1,0,0,0,53,32,1,0,0,0,53,43,1,0,0,
        0,53,48,1,0,0,0,54,3,1,0,0,0,55,56,5,1,0,0,56,62,5,14,0,0,57,58,
        3,6,3,0,58,59,5,2,0,0,59,61,1,0,0,0,60,57,1,0,0,0,61,64,1,0,0,0,
        62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,73,5,
        14,0,0,66,67,5,3,0,0,67,69,5,14,0,0,68,70,7,0,0,0,69,68,1,0,0,0,
        69,70,1,0,0,0,70,71,1,0,0,0,71,73,5,14,0,0,72,55,1,0,0,0,72,66,1,
        0,0,0,73,5,1,0,0,0,74,75,3,8,4,0,75,76,5,12,0,0,76,77,3,10,5,0,77,
        80,1,0,0,0,78,80,5,8,0,0,79,74,1,0,0,0,79,78,1,0,0,0,80,7,1,0,0,
        0,81,86,5,8,0,0,82,83,5,9,0,0,83,85,5,8,0,0,84,82,1,0,0,0,85,88,
        1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,9,1,0,0,0,88,86,1,0,0,0,89,
        90,7,0,0,0,90,11,1,0,0,0,91,92,6,6,-1,0,92,93,5,5,0,0,93,94,3,12,
        6,0,94,95,5,6,0,0,95,101,1,0,0,0,96,97,5,11,0,0,97,101,3,12,6,7,
        98,101,5,7,0,0,99,101,5,8,0,0,100,91,1,0,0,0,100,96,1,0,0,0,100,
        98,1,0,0,0,100,99,1,0,0,0,101,116,1,0,0,0,102,103,10,6,0,0,103,104,
        5,9,0,0,104,115,3,12,6,7,105,106,10,5,0,0,106,107,5,10,0,0,107,115,
        3,12,6,6,108,109,10,4,0,0,109,110,5,12,0,0,110,115,3,12,6,5,111,
        112,10,3,0,0,112,113,5,13,0,0,113,115,3,12,6,4,114,102,1,0,0,0,114,
        105,1,0,0,0,114,108,1,0,0,0,114,111,1,0,0,0,115,118,1,0,0,0,116,
        114,1,0,0,0,116,117,1,0,0,0,117,13,1,0,0,0,118,116,1,0,0,0,15,16,
        18,23,25,28,39,53,62,69,72,79,86,100,114,116
    ]

class PLParser ( Parser ):

    grammarFileName = "PL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TELL'", "';'", "'ASK'", "'REMOVE'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "'&'", "'||'", 
                     "'~'", "'=>'", "'<=>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VALUE", "SYMBOL", 
                      "CONJUNCTION", "DISJUNCTION", "NEGATION", "IMPLICATION", 
                      "BICONDITIONAL", "NEWLINE", "WHITESPACE" ]

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
    T__5=6
    VALUE=7
    SYMBOL=8
    CONJUNCTION=9
    DISJUNCTION=10
    NEGATION=11
    IMPLICATION=12
    BICONDITIONAL=13
    NEWLINE=14
    WHITESPACE=15

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
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16394) != 0):
                    self.state = 16
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3]:
                        self.state = 14
                        self.hornStatement()
                        pass
                    elif token in [14]:
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
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16410) != 0):
                    self.state = 23
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 4]:
                        self.state = 21
                        self.statement()
                        pass
                    elif token in [14]:
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


    class RemoveContext(StatementContext):

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
            if hasattr( visitor, "visitRemove" ):
                return visitor.visitRemove(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = PLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 53
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
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2464) != 0):
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
            elif token in [4]:
                localctx = PLParser.RemoveContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(PLParser.T__3)
                self.state = 49
                self.match(PLParser.NEWLINE)
                self.state = 50
                self.sentence(0)
                self.state = 51
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
        def VALUE(self):
            return self.getToken(PLParser.VALUE, 0)
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PLParser.HornTellContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(PLParser.T__0)
                self.state = 56
                self.match(PLParser.NEWLINE)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 57
                    self.hornClause()
                    self.state = 58
                    self.match(PLParser.T__1)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.match(PLParser.NEWLINE)
                pass
            elif token in [3]:
                localctx = PLParser.HornAskContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(PLParser.T__2)
                self.state = 67
                self.match(PLParser.NEWLINE)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7 or _la==8:
                    self.state = 68
                    localctx.query = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==7 or _la==8):
                        localctx.query = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 71
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = PLParser.HornProperContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.hornClauseHead()
                self.state = 75
                self.match(PLParser.IMPLICATION)
                self.state = 76
                self.hornClauseTail()
                pass

            elif la_ == 2:
                localctx = PLParser.HornSingleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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
            self.state = 81
            self.match(PLParser.SYMBOL)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 82
                self.match(PLParser.CONJUNCTION)
                self.state = 83
                self.match(PLParser.SYMBOL)
                self.state = 88
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

        def VALUE(self):
            return self.getToken(PLParser.VALUE, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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


    class TruthLiteralContext(SentenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PLParser.SentenceContext
            super().__init__(parser)
            self.val = None # Token
            self.copyFrom(ctx)

        def VALUE(self):
            return self.getToken(PLParser.VALUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTruthLiteral" ):
                return visitor.visitTruthLiteral(self)
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
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = PLParser.NestedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 92
                self.match(PLParser.T__4)
                self.state = 93
                self.sentence(0)
                self.state = 94
                self.match(PLParser.T__5)
                pass
            elif token in [11]:
                localctx = PLParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.match(PLParser.NEGATION)
                self.state = 97
                self.sentence(7)
                pass
            elif token in [7]:
                localctx = PLParser.TruthLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                localctx.val = self.match(PLParser.VALUE)
                pass
            elif token in [8]:
                localctx = PLParser.AtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                localctx.atom = self.match(PLParser.SYMBOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = PLParser.ConjunctionContext(self, PLParser.SentenceContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sentence)
                        self.state = 102
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 103
                        self.match(PLParser.CONJUNCTION)
                        self.state = 104
                        localctx.rhs = self.sentence(7)
                        pass

                    elif la_ == 2:
                        localctx = PLParser.DisjunctionContext(self, PLParser.SentenceContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sentence)
                        self.state = 105
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 106
                        self.match(PLParser.DISJUNCTION)
                        self.state = 107
                        localctx.rhs = self.sentence(6)
                        pass

                    elif la_ == 3:
                        localctx = PLParser.ImplicationContext(self, PLParser.SentenceContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sentence)
                        self.state = 108
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 109
                        self.match(PLParser.IMPLICATION)
                        self.state = 110
                        localctx.rhs = self.sentence(5)
                        pass

                    elif la_ == 4:
                        localctx = PLParser.BiconditionalContext(self, PLParser.SentenceContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_sentence)
                        self.state = 111
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 112
                        self.match(PLParser.BICONDITIONAL)
                        self.state = 113
                        localctx.rhs = self.sentence(4)
                        pass

             
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         





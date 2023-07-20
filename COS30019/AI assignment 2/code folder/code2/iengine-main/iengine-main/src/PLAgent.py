from KB import KB
from PLInterpreter import PLInterpreter
from antlr4 import CommonTokenStream, FileStream

from algorithms import tt_entail, bc_entail, fc_entail, dpll_entail

from parser.PLLexer import *
from parser.PLParser import *

class PLAgent:
    def __init__(self, stream):
        self.__kb = KB()
        # For slight improve on tt_entail's efficiency
        self.__symbols = set() # Keeps track of all atoms in kb and query
        self.__methods = {'ttentail': tt_entail, 'fc': fc_entail, 'bc': bc_entail, 'dpll': dpll_entail}
        self.__parser = self.__getparser__(stream)
        self.__method = 'ttentail'


    def tell(self, expr):
        self.__kb.add(expr)


    def ask(self, query):
        self.__methods[self.__method](self.__kb, query, self.__symbols)


    def know(self, expr):
        self.__symbols.add(expr)


    def interpret(self, method):
        if method not in self.__methods.keys():
            print('No method with matching codename found, using truth table enumeration.')
            method = 'ttentail'
        else:
            self.__method = method
        self.__interpreter = PLInterpreter(self)
        self.__interpreter.visitProgram(self.__parser.program())

    def __getparser__(self, stream):
        lexer = PLLexer(FileStream(stream))
        parser = PLParser(CommonTokenStream(lexer))
        return parser

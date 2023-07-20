# KB is not a specialization of PLExpression
# Cannot add a KB to another KB, can only merge
from plast import AtomExpression, ConjunctionExpression


class KB:
    def __init__(self):
        self.__expr_collection = set()


    def evaluate(self, model):
        for expr in self.__expr_collection:
            if not expr.evaluate(model):
                return False
        return True


    def reduce(self):
        count = len(self.__expr_collection)
        exprlist = list(self.__expr_collection)
        i = 0
        if count > 0:
            if count > 1:
                res = ConjunctionExpression(exprlist[i], exprlist[i+1])
                i += 2
                while i < count:
                    res = ConjunctionExpression(res, exprlist[i])
                    i += 1
                return res.reduce()
            else:
                return exprlist[0].reduce()
        else:
            return AtomExpression('False')


    def add(self, expr):
        self.__expr_collection.add(expr)


    def remove(self, expr):
        for e in self.__expr_collection:
            if e == expr:
                self.__expr_collection.remove(e)


    def __iter__(self):
        return iter(self.__expr_collection)

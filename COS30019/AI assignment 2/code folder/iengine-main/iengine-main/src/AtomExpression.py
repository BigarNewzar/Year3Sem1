from PLExpression import PLExpression


class AtomExpression(PLExpression):
    def __init__(self, symbol):
        self.__symbol = symbol


    def __str__(self):
        return self.__symbol


    def evaluate(self, model):
        return model[self]


    def __eq__(self, other):
        return isinstance(other, AtomExpression) \
            and self.__symbol == other.__symbol


    def __ne__(self, other):
        return self.__eq__(other)


    def __hash__(self):
        return hash(('', self.__symbol))


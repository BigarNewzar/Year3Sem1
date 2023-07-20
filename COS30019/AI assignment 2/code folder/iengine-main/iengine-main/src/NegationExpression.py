from PLExpression import PLExpression


class NegationExpression(PLExpression):
    def __init__(self, operand: PLExpression):
        self.__operand = operand


    def evaluate(self, model):
        return not self.__operand.evaluate(model)


    def __eq__(self, other):
        return isinstance(other, NegationExpression) \
            and self.__operand == other.__operand


    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(('~', self.__operand))
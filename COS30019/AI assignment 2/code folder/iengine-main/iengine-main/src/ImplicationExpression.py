from PLExpression import PLExpression


class ImplicationExpression(PLExpression):
    def __init__(self, lhs: PLExpression, rhs: PLExpression):
        self.__lhs = lhs
        self.__rhs = rhs


    def evaluate(self, model):
        return not self.__lhs.evaluate(model) \
            or self.__rhs.evaluate(model)


    def __eq__(self, other):
        return isinstance(other, ImplicationExpression) \
            and self.__lhs == self.__lhs \
            and self.__rhs == self.__rhs


    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(('=>', self.__lhs, self.__rhs))

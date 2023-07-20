from PLExpression import PLExpression


class ConjunctionExpression(PLExpression):
    def __init__(self, lhs: PLExpression, rhs: PLExpression):
        self.__lhs = lhs
        self.__rhs = rhs


    def evaluate(self, model):
        return self.__lhs.evaluate(model) \
            and self.__rhs.evaluate(model)


    def __eq__(self, other):
        return isinstance(other, ConjunctionExpression) \
            and self.__lhs == other.__lhs \
            and self.__rhs == other.__rhs


    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(('&', self.__lhs, self.__rhs))
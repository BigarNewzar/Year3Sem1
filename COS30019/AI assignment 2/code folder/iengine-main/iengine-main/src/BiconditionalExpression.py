from PLExpression import PLExpression


class BiconditionalExpression:
    def __init__(self, lhs: PLExpression, rhs: PLExpression):
        self.__lhs = lhs
        self.__rhs = rhs


    def evaluate(self, model):
        lhs = self.__lhs.evaluate(model)
        rhs = self.__rhs.evaluate(model)
        return (not lhs or rhs) and (not rhs or lhs)

    def __eq__(self, other):
        return isinstance(other, BiconditionalExpression) \
            and self.__lhs == other.__lhs \
            and self.__rhs == other.__rhs

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(('<=>', self.__lhs, self.__rhs))

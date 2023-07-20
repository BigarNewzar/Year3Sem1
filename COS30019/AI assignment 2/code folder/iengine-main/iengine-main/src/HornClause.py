from ImplicationExpression import ImplicationExpression
from ConjunctionExpression import ConjunctionExpression
from AtomExpression import AtomExpression


class HornClause(ImplicationExpression):
    # Horn clause is an implication expression
    # whose lhs is a conjunction expression of atom expressions
    # and rhs is an atom expression

    def __init__(self, head, tail):
        self.__head = head
        self.__tail = tail
        super().__init__(self.__getheadexpr__(list(head)), tail)


    def __getheadexpr__(self, head):
        count = len(head)
        if count > 1:
            aux = ConjunctionExpression(head[count - 1], head[count - 2])
            count -= 2
            while count:
                aux = ConjunctionExpression(aux, head[count - 1])
                count -= 1
            return aux
        else:
            return head[0]


    # Return a collection of atoms
    def head(self):
        return self.__head


    # Return an atom
    def tail(self):
        return self.__tail

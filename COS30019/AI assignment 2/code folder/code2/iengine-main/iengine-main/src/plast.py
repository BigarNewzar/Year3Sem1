class AtomExpression():
    def __init__(self, symbol):
        self.__symbol = symbol


    def reduce(self):
        return self


    def __str__(self):
        return self.__symbol


    def evaluate(self, model):
        if self.__symbol == 'True':
            return True
        elif self.__symbol == 'False':
            return False
        return model[self]


    def __eq__(self, other):
        return isinstance(other, AtomExpression) \
            and self.__symbol == other.__symbol


    def __ne__(self, other):
        return self.__eq__(other)


    def __hash__(self):
        return hash(('', self.__symbol))

    def find(self, literal, count):
        if self == literal:
            return count + 1
        return count

    def unit(self, model):
        if self not in model:
            return self, True
        else:
            return None, None


    def cnfeval(self, model):
        if self in model:
            return model[self]
        else:
            return None

    def flatten(self):
        return {self}


class NegationExpression():
    def __init__(self, operand):
        self.__operand = operand


    def __str__(self):
        return ('~' + str(self.__operand))


    def reduce(self):
        op = self.__operand.reduce()
        if isinstance(op, NegationExpression):
            return op.__operand

        if isinstance(op, DisjunctionExpression):
            return DisjunctionExpression(
                NegationExpression(op.lhs()),
                NegationExpression(op.rhs())
            ).reduce()
        if isinstance(op, ConjunctionExpression):
            return ConjunctionExpression(
                NegationExpression(op.lhs()),
                NegationExpression(op.rhs())
            ).reduce()

        return NegationExpression(op)


    def evaluate(self, model):
        return not self.__operand.evaluate(model)


    def __eq__(self, other):
        return isinstance(other, NegationExpression) \
            and self.__operand == other.__operand


    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(('~', self.__operand))


    def find(self, literal, count):
        if self == literal:
            return count + 1
        return count


    def unit(self, model):
        if self.__operand not in model:
            return self.__operand, False
        else:
            return None, None


    def cnfeval(self, model):
        if self.__operand.cnfeval(model) is not None:
            return not self.__operand.cnfeval(model)
        else:
            return None

    def flatten(self):
        return {self}

class ImplicationExpression():
    def __init__(self, lhs, rhs):
        self.__lhs = lhs
        self.__rhs = rhs


    def reduce(self):
        return DisjunctionExpression(
            NegationExpression(self.__lhs),
            self.__rhs
        ).reduce()


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

class ConjunctionExpression():
    def __init__(self, lhs, rhs):
        self.__lhs = lhs
        self.__rhs = rhs


    def __str__(self):
        return '(' + str(self.__lhs) + '&' + str(self.__rhs) + ')'

    def reduce(self):
        # CNF of a disjunction: lhs and rhs in cnf
        lhs = self.__lhs.reduce()
        rhs = self.__rhs.reduce()

        return ConjunctionExpression(lhs, rhs)


    def evaluate(self, model):
        return self.__lhs.evaluate(model) \
            and self.__rhs.evaluate(model)


    def rhs(self):
        return self.__rhs


    def lhs(self):
        return self.__lhs


    def __eq__(self, other):
        return isinstance(other, ConjunctionExpression) \
            and self.__lhs == other.__lhs \
            and self.__rhs == other.__rhs


    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(('&', self.__lhs, self.__rhs))

    def find(self, literal, count):
        return self.__lhs.find(literal, count) + self.__rhs.find(literal, count)

    def unit(self, model):
        left = self.__lhs.unit(model)
        if left != set():
            return left

        right = self.__rhs.unit(model)
        if right != set():
            return right

        return set()

    def cnfeval(self, model):
        lhs = self.__lhs.cnfeval(model)
        if lhs is not None:
            if not lhs:
                return False
            else:
                rhs = self.__rhs.cnfeval(model)
                if rhs is not None:
                    return rhs
                return None
        else:
            rhs = self.__rhs.cnfeval(model)
            if rhs is not None and not rhs:
                return False
            return None

    def flatten(self):
        res = set()
        if isinstance(self.__lhs, DisjunctionExpression) or isinstance(self.__lhs, AtomExpression) or isinstance(
            self.__lhs, NegationExpression):
            res.add(frozenset(self.__lhs.flatten()))
        else:
            res = res | self.__lhs.flatten()
        if isinstance(self.__rhs, DisjunctionExpression) or isinstance(self.__rhs, AtomExpression) or isinstance(
            self.__rhs, NegationExpression):
            res.add(frozenset(self.__rhs.flatten()))
        else:
            res = res | self.__rhs.flatten()
        return res



class BiconditionalExpression:
    def __init__(self, lhs, rhs):
        self.__lhs = lhs
        self.__rhs = rhs


    def reduce(self):
        return ConjunctionExpression(
            ImplicationExpression(self.__lhs, self.__rhs),
            ImplicationExpression(self.__rhs, self.__lhs)
        ).reduce()


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

class DisjunctionExpression():
    def __init__(self, lhs, rhs):
        self.__lhs = lhs
        self.__rhs = rhs

    def __str__(self):
        return '('  + str(self.__lhs) + '||' + str(self.__rhs) + ')'

    def flatten(self):
        return self.__lhs.flatten() | self.__rhs.flatten()
    def lhs(self):
        return self.__lhs


    def rhs(self):
        return self.__rhs


    def evaluate(self, model):
        return self.__lhs.evaluate(model) \
            or self.__rhs.evaluate(model)


    def reduce(self):
        # CNF of a disjunction: lhs and rhs in cnf
        # If either (or both) is a conjunction, distribute
        # (a & b) || (c & d) = (a || (c & d)) & (b || (c & d))
        lhs = self.__lhs.reduce()
        rhs = self.__rhs.reduce()

        if isinstance(lhs, ConjunctionExpression):
            return ConjunctionExpression(
                DisjunctionExpression(lhs.lhs(), rhs),
                DisjunctionExpression(lhs.rhs(), rhs)
            ).reduce()

        if isinstance(rhs, ConjunctionExpression):
            return ConjunctionExpression(
                DisjunctionExpression(lhs, rhs.lhs()),
                DisjunctionExpression(lhs, rhs.rhs())
            ).reduce()

        return DisjunctionExpression(lhs, rhs)


    def __eq__(self, other):
        return isinstance(other, DisjunctionExpression) \
            and self.__lhs == other.__lhs \
            and self.__rhs == other.__rhs


    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(('||', self.__lhs, self.__rhs))


    def find(self, literal, count):
        return self.__lhs.find(literal, count) + self.__rhs.find(literal, count)


    def unit(self, model):
        tree = self.__lhs.unit(model).union(self.__rhs.unit(model))

        if len(tree) == 1:
            return tree
        else:
            return set()

    def cnfeval(self, model):
        lhs = self.__lhs.cnfeval(model)
        if lhs is not None:
            if lhs:
                return True
            else:
                rhs = self.__rhs.cnfeval(model)
                if rhs is not None:
                    return rhs
                return None
        else:
            rhs = self.__rhs.cnfeval(model)
            if rhs is not None and rhs:
                return True
            return None


    def flatten(self):
        return (self.__lhs.flatten() | self.__rhs.flatten())

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

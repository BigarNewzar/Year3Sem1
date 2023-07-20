# KB is not a specialization of PLExpression
# Cannot add a KB to another KB, can only merge
class KB:
    def __init__(self):
        self.__expr_collection = set()


    def evaluate(self, model):
        for expr in self.__expr_collection:
            if not expr.evaluate(model):
                return False
        return True


    def add(self, expr):
        self.__expr_collection.add(expr)


    def remove(self, expr):
        for e in self.__expr_collection:
            if e == expr:
                self.__expr_collection.remove(e)


    def __iter__(self):
        return iter(self.__expr_collection)


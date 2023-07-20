from abc import abstractmethod


class PLExpression:
    @abstractmethod
    def evaluate(self, model):
        ...


    # Called by forward chaining and backward chaining
    def to_cnf(self):
        ...


    @abstractmethod
    def __eq__(self, other):
        ...


    @abstractmethod
    def __ne__(self, other):
        ...


    @abstractmethod
    def __hash__(self):
        ...

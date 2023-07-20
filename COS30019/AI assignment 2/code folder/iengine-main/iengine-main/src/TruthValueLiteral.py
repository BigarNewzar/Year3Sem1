class TruthValueLiteral:
    def __init__(self, value):
        self.__value = value


    def evaluate(self, model):
        return self.__value

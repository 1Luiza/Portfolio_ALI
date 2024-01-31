"""
Создать метакласс для паттерна Синглтон
"""


class Singleton(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class FirstMyClass(metaclass=Singleton):
    def __init__(self, param):
        self.param = param


class SecondMyClass(metaclass=Singleton):
    def __init__(self, param):
        self.param = param


FMC = FirstMyClass(1)
FMC_1 = FirstMyClass(2)
SMC = SecondMyClass('one')
SMC_1 = SecondMyClass('two')

print('FMC is FMC_1', FMC is FMC_1)
print('SMC is SMC_1', SMC is SMC_1)
print('FMC is SMC_1', SMC is SMC_1)

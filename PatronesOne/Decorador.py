# Este patron permite unir funciones a objetosdentro de otros objetos.

import abc
class Componente(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def oper(self):
        pass

class Decorator(Componente, metaclass=abc.ABCMeta):
    def __init__(self, component):
        self._componente = component

    @abc.abstractmethod
    def oper(self,component):
        pass

class ConcreteDecoratorA(Decorator):
    def oper(self):
        self._componente.oper()
    
class ConcreteDecoratorB(Decorator):
    def oper(self):
        self._componente.oper()

class ConcreteComponent(Component):
    def operOne(self):
        pass

def main():
    concrete_componente = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_componente)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.oper()

if __name__ == "__main__":
    main()
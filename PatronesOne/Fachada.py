# En este patron es un diseño en el que se permite interfaz esquematizado 
# a un framework o una biblioteca o otros tipos de clases.

class Fachada:
    def __init__(self):
        self._subsystem_1 = Subsystem1()
        self._subsystem_2 = Subsystem2()
    
    def operation(self):
        self._subsystem_1.oper1()
        self._subsystem_1.oper2()
        self._subsystem_2.oper1()
        self._subsystem_2.oper2()
    
class Subsystem1:
    def oper1(self):
        pass

    def oper2(self):
        pass
    
class Subsystem2:
    def oper1(self):
        pass

    def oper2(self):
        pass
    
def main():
    fachada = Fachada()
    fachada.operation()

if __name__ == "__main__":
    main()
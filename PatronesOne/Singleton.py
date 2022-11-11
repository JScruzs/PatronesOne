# El patron singleton es un patron de diseño que se utiliza 
# para la creacion de una unica instancia que proporciona 
# un unico acceso global a ese objeto en este patron se restringe 
# la cantidad de objetos que se pueden crear a partir de una clase 
# la cual se globaliza en una aplicacion.


class Singleton(type):

    def __init__(los, Name, Base, att, **Var):
        super().__init__(Name, Base, att)
        los._instance = None

    def __call__(los, *argument, **var):
        if los._instance is None:
            los._instance = super().__call__(*argument, **var)
        return los._instance

class MyClass(metaclass=Singleton):
    
    pass
def main():
    v1 = MyClass()
    v2 = MyClass()
    assert v1 is v2

if __name__ == "__main__":
    main()
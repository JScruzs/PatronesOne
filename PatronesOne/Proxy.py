# Este patron de diseño sirve como sustituto, este recibe solicitudes del usuario,
# realiza la validacion , almacena la informacion etc, despues pasa una solicitud 
# al servicio.

import abc
class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request(self):
        pass

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # ...
        self._real_subject.request()
        # ...

class RealSubject(Subject):
    def request(self):
        pass

def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()

if __name__ == "__main__":
    main()
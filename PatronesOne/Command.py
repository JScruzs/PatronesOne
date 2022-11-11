# Este patron es en un diseño de comportamiento lo qeu convierte una solicitud 
# en un objeto indeoendiente y que la informacion esta en la solicitud.

import abc
class Invoker:
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

class Command(metaclass=abc.ABCMeta):
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        self._receiver.action()

class Receiver:
    def action(self):
        pass

def main():
    receiver = Receiver()
    concrete_command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.store_command(concrete_command)
    invoker.execute_commands()

if __name__ == "__main__":
    main()
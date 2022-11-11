# Es un patron dediseño en el cual las funciones dependen de otros objetos.

class calc:
    def sum(num1, num2):
        return num1 + num2
    def res(num1, num2):
        return num1 - num2
    def multi(num1, num2):
        return num1 * num2
    def div(num1, num2):
        if num2 == 0:
            return print("No es posible dividir por 0")
        else:
            return num1 / num2
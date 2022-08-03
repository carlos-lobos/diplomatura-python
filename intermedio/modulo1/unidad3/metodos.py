class OperacionesM():

    variable = "Metodo de clase"

    @classmethod
    def sumar2(cls, a, b):
        c = a + b
        print(cls.variable)
        return c

    @staticmethod
    def sumar(a, b):
        c = a + b
        print("Metodo estatico")
        return c

    def sumar3(self, a, b):
        c = a + b
        print("Metodo de instancia")
        return c

obj=OperacionesM()

print(obj.sumar(2, 3))
print(OperacionesM.sumar(2, 3))

print(obj.sumar2(2, 3))
print(OperacionesM.sumar2(2, 3))

print(obj.sumar3(2, 3))

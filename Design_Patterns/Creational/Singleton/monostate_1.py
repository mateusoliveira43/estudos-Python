"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self):
        params = [f'{k} = {v}' for k, v in self.__dict__.items()]
        params = ', '.join(params)
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


# class A(StringReprMixin):
#     def __init__(self, nome):
#         self.nome = nome
#         self.x = 10
#         self.y = 20

#     # def __str__(self):
#     #     # return 'Classe A: exemplo de padrão MONOSTATE.'
#     #     params = [f'{k} = {v}' for k, v in self.__dict__.items()]
#     #     params = ', '.join(params)
#     #     return f'{self.__class__.__name__}({params})'

#     # def __repr__(self):
#     #     return self.__str__()

class MonoStateSimple(StringReprMixin):
    # _state = {
    #     'x': 10,
    #     'y': 20,
    # }
    _state: dict = {}

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state
        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    # a = A('Mateus')
    # print(a)
    # print(a.__dict__)
    m1 = MonoStateSimple(nome='Mateus')
    m2 = MonoStateSimple(sobrenome='Oliveira')
    # m1.x = 'Mudei'
    print(m1)
    print(m2)

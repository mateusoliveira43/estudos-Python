# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('INIT é executado')
#         self.nome = nome

#     def __call__(self):
#         print('call chamado')


# if __name__ == "__main__":
#     p1 = Pessoa('Mateus')
#     p1()
#     print(p1.nome)
class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        # o init será chamdo todas as vezes
        self.tema = 'Tema Escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'Tema Claro'
    print(as1.tema)
    as2 = AppSettings()
    as3 = AppSettings()
    print(as2.tema)

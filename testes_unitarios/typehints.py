from typing import List, Union, Tuple, Dict, NewType, \
    Callable, Sequence, Iterable
# Primitivos

numero: int = 10
flutuante: float = 10.5
booleano: bool = False
sting: str = 'string'

# Sequeências
# lista: list = [1, 2, 3]
lista: List[int] = [1, 2, 3]
lista_mista: List[Union[int, str]] = [1, 2, 3, 'mateus']
# tupla: tuple = (1, 2, 3)
tupla: Tuple[int, int, int] = (1, 2, 3)

# Dicionários e conjuntos
meudict = Dict[str, Union[str, int, List[int]]]
pessoa: meudict = {'nome': 'Mateus',
                   'sobrenome': 'Oliveira', 'idade': 24, 'l': [1, 2]}

# Outro tipo
tipo = NewType('tipo', int)
teste = tipo(12)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(x: int, y: int) -> int:
    return x+y


retorna_funcao(soma)(10, 20)


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} está falando')


def iterar(sequencia: Sequence[int]):
    return [x*2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x*2 for x in sequencia]

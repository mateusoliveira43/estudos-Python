"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscando o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    def __init__(self, tipo):
        super().__init__(tipo)
        print()
        print('Buscando veículo na Zona Norte...')

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        elif tipo == 'popular':
            return CarroPopular()
        elif tipo == 'moto':
            return Moto()
        assert 0, 'Veículo não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):
    def __init__(self, tipo):
        super().__init__(tipo)
        print()
        print('Buscando veículo na Zona Sul...')

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe'


if __name__ == '__main__':
    filiais = [ZonaNorteVeiculoFactory, ZonaSulVeiculoFactory]
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto']
    veiculos_disponiveis_zona_sul = ['popular']

    for i in range(10):
        filial = choice(filiais)
        if filial == ZonaNorteVeiculoFactory:
            carro = filial(
                choice(veiculos_disponiveis_zona_norte))
            carro.buscar_cliente()
        if filial == ZonaSulVeiculoFactory:
            carro = filial(
                choice(veiculos_disponiveis_zona_sul))
            carro.buscar_cliente()

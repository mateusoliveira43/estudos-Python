"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = [f'{k} = {v}' for k, v in self.__dict__.items()]
        params = ', '.join(params)
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self):
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    marco = Person('Marco', 'Oliveira')
    endereco_marco = Address('Av. Brasil', '1253A2')
    marco.add_address(endereco_marco)
    esposa_marco = marco.clone()
    esposa_marco.firstname = 'Maria'
    esposa_marco.lastname = 'Souza'
    print(marco)
    print(esposa_marco)

"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle):
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        value *= 0.8
        return value


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        value *= 0.5
        return value


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self,  discount):
        self.discount = 1-discount/100

    def calculate(self, value: float) -> float:
        value *= self.discount
        return value


if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    custom_discount = CustomDiscount(30)
    order = Order(100, twenty_percent)
    print(order.total, order.total_with_discount)
    order = Order(100, fifty_percent)
    print(order.total, order.total_with_discount)
    order = Order(100, no_discount)
    print(order.total, order.total_with_discount)
    order = Order(100, custom_discount)
    print(order.total, order.total_with_discount)

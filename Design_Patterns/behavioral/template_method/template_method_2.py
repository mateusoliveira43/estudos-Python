from abc import ABC, abstractmethod


class Pizza(ABC):
    """Classe Abstrata"""

    def prepare(self) -> None:
        """Template Method"""
        self.hook_before_add_ingredients()  # Hook
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredients()  # Hook
        self.cook()  # Abstract
        self.cut()  # Concrete
        self.serve()  # Concrete

    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f'Cortando pizza {self.__class__.__name__}.')

    def serve(self) -> None:
        print(f'Servindo pizza {self.__class__.__name__}.')

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class Portuguesa(Pizza):
    def add_ingredients(self) -> None:
        print(
            'Adicionando presunto, queijo, ovo, cebola e ervilha à pizza '
            f'{self.__class__.__name__}.')

    def cook(self) -> None:
        print(
            f'Cozinhando a pizza {self.__class__.__name__} por 45 min no forno'
            ' à lenha.')


class Vegetariana(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print('Lavando as verduras.')

    def add_ingredients(self):
        print(
            f'Adicionando tomate, queijo, brócolis, cebola e ervilha à pizza '
            f'{self.__class__.__name__}.')

    def cook(self) -> None:
        print(
            f'Cozinhando a pizza {self.__class__.__name__} por 40 min no forno'
            ' à lenha.')


if __name__ == "__main__":
    p1 = Portuguesa()
    p1.prepare()
    p2 = Vegetariana()
    p2.prepare()

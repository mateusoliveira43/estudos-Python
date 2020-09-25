"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    """ Receiver - Luz Inteligente """

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'Light {self.name} in {self.room_name} is now ON')

    def off(self) -> None:
        print(f'Light {self.name} in {self.room_name} is now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'Light {self.name} in {self.room_name} is now {self.color}')


class ICommand(ABC):
    """ Interface de Comando """

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    """ Comando Concreto """

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand):
    """ Comando Concreto """

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """ invoker """

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_commnd(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._undos:
            print('nothing to undo')
            return None

        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == "__main__":
    bedroom_light = Light('Luz do quarto', 'Quarto')
    bathroom_light = Light('Luz do banheiro', 'Banehiro')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'Red')
    bathroom_light_on = LightOnCommand(bathroom_light)

    remote = RemoteController()
    remote.button_add_commnd('first_button', bedroom_light_on)
    remote.button_add_commnd('second_button', bathroom_light_on)
    remote.button_add_commnd('third_button', bedroom_light_blue)
    remote.button_add_commnd('fourth_button', bedroom_light_red)
    remote.button_execute('first_button')
    remote.button_undo('first_button')
    remote.button_execute('second_button')
    remote.button_undo('second_button')
    remote.button_execute('third_button')
    remote.button_undo('third_button')
    remote.button_execute('fourth_button')
    remote.button_undo('fourth_button')
    print()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()

from __future__ import annotations
from abc import ABC, abstractmethod
import state_pattern.context as context

class State(ABC):
    @property
    def context(self) -> context.Context:
        return self._context

    @context.setter
    def context(self, context: context.Context) -> None:
        self._context = context

    @abstractmethod
    def taskLoop(self) -> None:
        pass

class Yellow(State):
    def __changeStateCondition(self) -> bool:
        gpio = self._context.getGpioController()
        return gpio.get_input(1)

    def taskLoop(self) -> None:
        if not self.__changeStateCondition():
            return

        self._context.setState(Red())

class Red(State):
    def __changeStateCondition(self) -> bool:
        gpio = self._context.getGpioController()
        return gpio.get_input(1)

    def taskLoop(self) -> None:
        if not self.__changeStateCondition():
            return

        self._context.setState(Yellow())

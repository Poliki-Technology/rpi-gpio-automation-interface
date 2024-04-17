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
    def taskOne(self) -> None:
        pass

    @abstractmethod
    def taskTwo(self) -> None:
        pass

class StateA(State):
    def taskOne(self) -> None:
        print("Running taskOne in stateA...")
        self._context.setState(StateB())

    def taskTwo(self) -> None:
        print("Running taskTwo in stateA...")

class StateB(State):
    def taskOne(self) -> None:
        print("Running taskOne in stateB...")

    def taskTwo(self) -> None:
        print("Running taskTwo in stateB...")
        self._context.setState(StateA())

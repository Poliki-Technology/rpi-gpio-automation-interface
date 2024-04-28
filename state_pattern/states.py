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

class StateA(State):
    def taskLoop(self) -> None:
        print("Running taskOne in stateA...")
        self._context.setState(StateB())

class StateB(State):
    def taskLoop(self) -> None:
        print("Running taskOne in stateB...")
        self._context.setState(StateA())


from __future__ import annotations
import state_pattern.states as states

# the context class contains a _state that references the concrete state and setState method to change between states.
class Context:
    _state = None

    def __init__(self, state: states.State) -> None:
        self.setState(state)

    def setState(self, state: states.State):
        print(f"Context: Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def taskOne(self):
        self._state.taskOne()
    
    def taskTwo(self):
        self._state.taskTwo()

from __future__ import annotations
import state_pattern.states as states
from gpio.gpio_controller import GpioController
from logger.i_logger import ILogger

# the context class contains a _state that references the concrete state and setState method to change between states.
class Context:
    _state = None
    _gpioController = None
    _logger = None

    def __init__(self, state: states.State, logger: ILogger) -> None:
        self._logger = logger
        self.setState(state)
        self._gpioController = GpioController()

    def getGpioController(self) -> GpioController:
        return self._gpioController

    def setState(self, state: states.State):
        self._logger.log(f"Context: Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def taskLoop(self):
        self._state.taskLoop()

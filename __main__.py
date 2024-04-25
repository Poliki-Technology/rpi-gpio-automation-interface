import state_pattern.context as context
import state_pattern.states as states
from dotenv import load_dotenv
import gpio.gpio_controller

load_dotenv()

myContext = context.Context(states.StateA())

myContext.taskTwo()
myContext.taskOne()
myContext.taskOne()
myContext.taskTwo()

import state_pattern.context as context
import state_pattern.states as states

myContext = context.Context(states.StateA())

myContext.taskTwo()
myContext.taskOne()
myContext.taskOne()
myContext.taskTwo()

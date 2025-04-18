from hw2_q2 import meetup
from hw2_q2 import Agent
from hw2_q2 import Condition

data0 = (
    Agent("Adam", Condition.SICK),
    Agent("Cure0", Condition.CURE),
    Agent("Cure1", Condition.CURE),
    Agent("Bob", Condition.HEALTHY),
    Agent("Alice", Condition.DEAD),
    Agent("Charlie", Condition.DYING),
    Agent("Vaccine", Condition.SICK),
    Agent("Darlene", Condition.DYING),
    Agent("Emma", Condition.SICK),
    Agent("Cure2", Condition.CURE),
)

print(set(meetup(data0)))
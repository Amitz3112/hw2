from itertools import batched
from enum import Enum
from collections import namedtuple

Condition=Enum("condition",("CURE","HEALTHY","SICK","DEAD","DYING"))
Agent=namedtuple("Agent",("name","category"))
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
    Agent("Cure2", Condition.CURE))

def only_meeters(agent_list: tuple) -> tuple:
    return tuple(agent for agent in agent_list if agent.category not in (Condition.DEAD, Condition.HEALTHY))

#meeters=batched(data0, n=2)
    
meeters=only_meeters(data0)
#print(meeters)

def now_we_meet(meeters:tuple)->list:
    """
    Sets the meetings between each agent and the consecutive one. 
    if the meeters n is uneven, the last agent remains unchanges.

    Parametes
    ---------
    meeters: Tuple of Agents
    list of Agents of the conditions "SICK", "DYING", and "CURE".  
    """
    updated_agents=[]
    for pair in batched(meeters, 2):
        if len(pair) == 2 and pair[0].category == Condition.SICK and pair[1].category == Condition.SICK:
            updated_agents.append(pair[0]._replace(category=Condition.DYING))
            updated_agents.append(pair[1]._replace(category=Condition.DYING))
        elif len(pair) == 2 and pair[0].category == Condition.SICK and pair[1].category == Condition.DYING:
            updated_agents.append(pair[0]._replace(category=Condition.DYING))
            updated_agents.append(pair[1]._replace(category=Condition.DEAD))
        elif len(pair) == 2 and pair[0].category == Condition.SICK and pair[1].category == Condition.CURE:
            updated_agents.append(pair[0]._replace(category=Condition.HEALTHY))
            updated_agents.append(pair[1]._replace(category=Condition.CURE))
        elif len(pair) == 2 and pair[0].category == Condition.CURE and pair[1].category == Condition.SICK:
            updated_agents.append(pair[0]._replace(category=Condition.CURE))
            updated_agents.append(pair[1]._replace(category=Condition.HEALTHY))
        elif len(pair) == 2 and pair[0].category == Condition.DYING and pair[1].category == Condition.DYING:
            updated_agents.append(pair[0]._replace(category=Condition.DEAD))
            updated_agents.append(pair[1]._replace(category=Condition.DEAD))
        elif len(pair) == 2 and pair[0].category == Condition.DYING and pair[1].category == Condition.SICK:
            updated_agents.append(pair[0]._replace(category=Condition.DEAD))
            updated_agents.append(pair[1]._replace(category=Condition.DYING))
        elif len(pair) == 2 and pair[0].category == Condition.DYING and pair[1].category == Condition.DYING:
            updated_agents.append(pair[0]._replace(category=Condition.DEAD))
            updated_agents.append(pair[1]._replace(category=Condition.DEAD))
        elif len(pair) == 2 and pair[0].category == Condition.DYING and pair[1].category == Condition.CURE:
            updated_agents.append(pair[0]._replace(category=Condition.SICK))
            updated_agents.append(pair[1]._replace(category=Condition.CURE))
        elif len(pair) == 2 and pair[0].category == Condition.CURE and pair[1].category == Condition.DYING:
            updated_agents.append(pair[0]._replace(category=Condition.CURE))
            updated_agents.append(pair[1]._replace(category=Condition.SICK))
        else:
            updated_agents.extend(pair)
    
    return updated_agents

updated_agents=now_we_meet(meeters)

for Agent in data0:
        if Agent.category == Condition.HEALTHY or Agent.category == Condition.DEAD:
            updated_agents.append(Agent)
print(updated_agents)


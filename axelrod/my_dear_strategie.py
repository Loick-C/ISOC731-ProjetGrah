import axelrod as axl
from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D

class MyDearStrategie(Player):
    """A player who only ever defects.

    Names:

    - Defector: [Axelrod1984]_
    - ALLD: [Press2012]_
    - Always defect: [Mittal2009]_
    """

    name = "MyDearStrategie"
    classifier = {
        "memory_depth": 0,
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    @staticmethod
    def strategy(self,opponent: Player) -> Action:
        if len(self.history) == 0:
            return C
        if opponent.history[-1] == C :
            return C
        return D
    
players = (axl.Cooperator(), axl.MyDearStrategie())

print(axl.MyDearStrategie())
# dependencies
from .basenode import Node
from .. import ACTION
from random import randint
# action base node
class Action(Node):
    """Base node designed to have multiple children."""
    def __init__(self, config):
        """Constructor."""
        Node.__init__(self, config)
        self.type = "action"# str
    def __repr__(self):# str
        """String representation."""
        return "<Action()>"
# actions
class Succeeder(Action):
    """Designed to return true."""
    def __init__(self, config):
        """Constructor."""
        Action.__init__(self, config)
    def __repr__(self):# str
        """String representation."""
        return "<Succeeder>"
    def execute(self):
        """Return true."""
        return True
class Failer(Action):
    """Designed to return false."""
    def __init__(self, config):
        """Constructor."""
        Action.__init__(self, config)
    def __repr__(self):# str
        """String representation."""
        return "<Failer>"
    def execute(self):
        """Return false."""
        return False

# functions (action nodes)
class toConsole(Action):
    """Print the given value to console and return true."""
    def __init__(self, config):
        """Constructor."""
        Action.__init__(self, config)
        self.value = config["properties"]["value"]# str
    def __repr__(self):# str
        """String representation."""
        return "<toConsole()>"
    def execute(self):
        """Print the property to console and return true."""
        if self.value != "":
            print(ACTION["to_console"], self.value)

        return True
class random(Action):
    """Return a random int between the two given numbers."""
    def __init__(self, config):
        """Constructor."""
        Action.__init__(self, config)
        self.number = 0# int
    def __repr__(self):# str
        """String representation."""
        return "<random()>"
    def execute(self):
        """Return true after generating a random number."""
        if len(self.properties) > 0:
            for k, v in self.properties.items():
                if k == "between":
                    start, end = [int(i) for i in v.split(":")]
                    self.number = randint(start, end)

        return True

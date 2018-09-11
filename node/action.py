# dependencies
from .basenode import Node
from .. import ACTION
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

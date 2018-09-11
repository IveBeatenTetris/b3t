# dependencies
from .basenode import Node
from .. import ERROR

class Decorator(Node):
    """Base node designed to one single children."""
    def __init__(self, config, child):
        """Constructor."""
        Node.__init__(self, config)
        self.type = "decorator"# str
        self.child = child# b3t.node
        if child is None:
            print(ERROR["missing_decorator_node"])
    def __repr__(self):# str
        """String representation."""
        return "<Decorator>"
class Inverter(Decorator):
    """Designed to return true if all child nodes return true."""
    def __init__(self, config, child={}):
        """Constructor."""
        Decorator.__init__(self, config, child)
    def __repr__(self):# str
        """String representation."""
        return "<Inverter>"
    def execute(self):
        """Simply invert the output and return it as this decorators state."""
        if self.child.execute() is True:
            return False
        else:
            return True

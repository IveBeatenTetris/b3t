"""
The correct order of children for cpomposites is fundamental for returning
correct values.
"""
# dependencies
from .basenode import Node
from .. import ERROR
from random import randint

class Composite(Node):
    """Base node designed to have multiple children."""
    def __init__(self, config, children):
        """Constructor."""
        Node.__init__(self, config)
        self.type = "composite"# str
        self.children = children# list
        if children is None or len(children) == 0:
            print(ERROR["missing_composite_nodes"])
    def __repr__(self):# str
        """String representation."""
        return "<Composite>"

class Random(Composite):
    """Return a random child-state."""
    def __init__(self, config, children={}):
        """Constructor."""
        Composite.__init__(self, config, children)
    def __repr__(self):# str
        """String representation."""
        return "<Random>"
    def execute(self):
        """
        Generate an int between 0 and the count of children. Use this int to
        return a child feedback on that list-index.
        """
        i = randint(0, len(self.children) - 1)
        return self.children[i].execute()
class Selector(Composite):
    """Return true if any child also does."""
    def __init__(self, config, children={}):
        """Constructor."""
        Composite.__init__(self, config, children)
    def __repr__(self):# str
        """String representation."""
        return "<Selector>"
    def execute(self):
        """
        Return true if any child succeeds. Only False if all children fail.
        """
        for node in self.children:
            if node.execute() is False:
                pass
            else:
                return True

        return False
class Sequence(Composite):
    """Designed to return true if all child nodes return true."""
    def __init__(self, config, children={}):
        """Constructor."""
        Composite.__init__(self, config, children)
    def __repr__(self):# str
        """String representation."""
        return "<Sequence>"
    def execute(self):
        """
        Return true if every child succeeded. If any sends false then this
        sequence returns false as well.
        """
        for node in self.children:
            if node.execute() is True:
                pass
            else:
                return False

        return True

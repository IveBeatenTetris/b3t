"""Base node for all other nodes in this behavior tree."""
class Node:
    """Base node."""
    def __init__(self, config):
        """Constructor."""
        self.config = config# dict
        self.id = config["id"]# str
        self.name = config["name"]# str
        self.type = None# none > str
    def __repr__(self):# str
        """String representation."""
        return "<Node>"
    def execute(self):
        """For overwriting purpose."""
        pass

"""
Create behavior trees at https://www.behaviortrees.com/ and feed them here.
"""
# dependencies
from ..node.basenode import Node
from ..node.composite import *
from ..node.decorator import *
from ..node.action import *
from .. import ERROR

class BehaviorTree:
    """Acts as a simple finite state machine."""
    def __init__(self, config):
        """Constructor."""
        self.config = config# dict
        self.root = config["root"]# str > b3t.node
        self.nodes = self.getNodes()# dict
    def __repr__(self):# str
        """String representation."""
        return "<Behavior()>"
    def determineNode(self, config):# b3t.node
        """
        Determine the type and declare a new b3t.node of it for returning.
        """
        child = None
        children = []

        # creating a single chid node for decorators
        try:
            child = self.determineNode(self.config["nodes"][config["child"]])
        except KeyError:
            pass
        # creating multiple children nodes for composites
        try:
            for each in config["children"]:
                children.append(self.determineNode(self.config["nodes"][each]))
        except KeyError:
            pass

        # composite nodes
        if config["name"] == "Random":
            node = Random(config, children)
        elif config["name"] == "Sequence":
            node = Sequence(config, children)
        elif config["name"] == "Selector":
            node = Selector(config, children)
        # action nodes
        elif config["name"] == "Succeeder":
            node = Succeeder(config)
        elif config["name"] == "Inverter":
            node = Inverter(config, child)
        elif config["name"] == "Failer":
            node = Failer(config)
        # action nodes - functions
        elif config["name"][-1] == ")" or config["name"][-2] == "(":
            if config["name"] == "toConsole()":
                node = toConsole(config)

        else:
            node = Node(config)

        return node
    def execute(self):
        """Start at the root element."""
        try:
            return self.root.execute()
        except AttributeError:
            print(ERROR["missing_root_node"])
    def getNodes(self):# dict
        """
        Return a list of nodes. If the id matches the root's id then overwrite
        'self.root'with that newly created node.
        """
        nodes = {}

        for key, value in self.config["nodes"].items():
            node = self.determineNode(value)
            # make self.root a b3t.node
            if key == self.root:
                self.root = node

            nodes.update({key: node})

        return nodes

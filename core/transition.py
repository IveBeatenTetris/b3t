class Transition:
    def __init__(self, to_state):
        self.tostate = to_state# str
    def execute(self):
        print("-- transitioning to...")

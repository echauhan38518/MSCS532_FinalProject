class LoopImplementation:
    def __init__(self, name):
        self.name = name

    def run(self, n):
        """
        Subclasses must implement this method.
        Executes the loop for input size n.
        """
        raise NotImplementedError("Subclasses must implement the run() method.")

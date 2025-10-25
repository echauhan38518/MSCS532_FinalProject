from loop_base import LoopImplementation

class NonOptimizedLoop(LoopImplementation):
    def __init__(self):
        super().__init__("Non-Optimized Loop")

    def run(self, n):
        result = 0
        for i in range(n):
            for j in range(n):
                result += (i * 2) * (j * 2)
        return result

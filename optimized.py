import numpy as np
from loop_base import LoopImplementation

class OptimizedLoop(LoopImplementation):
    def __init__(self):
        super().__init__("Optimized Loop")

    def run(self, n):
        result = 0
        i_values = np.arange(n) * 2
        j_values = np.arange(n) * 2
        for i_val in i_values:
            result += i_val * np.sum(j_values)
        return result

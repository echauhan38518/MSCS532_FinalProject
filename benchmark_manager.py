import time
import numpy as np
import matplotlib.pyplot as plt

class BenchmarkManager:
    def __init__(self, implementations, sizes, repeat=3):
        self.implementations = implementations
        self.sizes = sizes
        self.repeat = repeat
        self.results = {imp.name: [] for imp in implementations}

    def benchmark(self):
        for n in self.sizes:
            print(f"Running benchmarks for input size n={n}")
            for imp in self.implementations:
                times = []
                for _ in range(self.repeat):
                    start = time.time()
                    imp.run(n)
                    end = time.time()
                    times.append(end - start)
                avg_time = np.mean(times)
                self.results[imp.name].append(avg_time)
                print(f"{imp.name}: {avg_time:.5f} s")
            print("-" * 40)
        return self.results

    def plot_results(self):
        plt.figure(figsize=(8,5))
        for name, times in self.results.items():
            plt.plot(self.sizes, times, marker='o', label=name)
        plt.title("Loop Optimization Performance Comparison")
        plt.xlabel("Input Size (n)")
        plt.ylabel("Execution Time (seconds)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

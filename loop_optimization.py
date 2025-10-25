from non_optimized import NonOptimizedLoop
from optimized import OptimizedLoop
from benchmark_manager import BenchmarkManager

if __name__ == "__main__":
    # Create loop instances
    loop_versions = [
        NonOptimizedLoop(),
        OptimizedLoop()
    ]

    # Define input sizes
    input_sizes = [200, 400, 600, 800, 1000, 1500, 2000]

    # Initialize benchmark manager
    manager = BenchmarkManager(loop_versions, input_sizes, repeat=3)

    # Run benchmarks
    manager.benchmark()

    # Plot results
    manager.plot_results()

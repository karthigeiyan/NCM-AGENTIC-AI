from simulation.benchmark import SystemBenchmark

if __name__ == "__main__":
    bm = SystemBenchmark()
    res = bm.run_benchmark()
    print("=== Enterprise NCM System Benchmark Results ===")
    for k, v in res.items():
        print(f"{k}: {v}")

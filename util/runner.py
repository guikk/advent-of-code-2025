import time

class Runner:
    def __init__(self, process_input, filename, *strategies):
      self.process_input = process_input
      self.filename = filename
      self.strategies = strategies

    def run(self):   
      processed_input = self.process_input(self.filename)
      for i, strategy in enumerate(self.strategies, 1):
        print(f"\n{'='*50}")
        print(f"Strategy {i}: {strategy.__name__}")
        
        start_time = time.perf_counter()
        result = strategy(processed_input)
        elapsed_time = time.perf_counter() - start_time
        
        print(f"Result: {result}")
        if elapsed_time > 1:
          print(f"Time: {elapsed_time:.4f}s")
        elif elapsed_time > 0.001:
          print(f"Time: {elapsed_time*1000:.0f}ms")
        else:
          print(f"Time: {elapsed_time*1000000:.0f}µs")
        print(f"{'='*50}")
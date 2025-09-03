"""
Threading Concept:
Threading in Python allows true parallel execution of tasks using multiple OS threads.
Unlike asyncio which uses cooperative multitasking on a single thread, threading creates
actual separate threads that can run simultaneously. However, Python's Global Interpreter
Lock (GIL) means that only one thread can execute Python bytecode at a time, making 
threading most effective for I/O-bound operations where threads can release the GIL
while waiting for external resources.

Best for I/O-bound tasks (file operations, network requests, database queries) where
threads spend time waiting. In our cooking example, each dish is prepared by a separate
"chef" (thread) working in parallel, allowing true concurrent preparation of multiple dishes.
"""

import threading
import time

def cook_with_result(dish_name, cook_time, results, index):
    """Cook task that stores result in shared list"""
    thread_name = threading.current_thread().name
    print(f"[*] Thread {thread_name}: Starting to cook {dish_name}...")
    time.sleep(cook_time)
    print(f"[OK] Thread {thread_name}: {dish_name} is ready!")
    results[index] = dish_name  # Store result at specific index

def main():
    """Main function that coordinates the threads"""
    print("[CHEF] Starting to cook multiple dishes with threads...")
    start_time = time.time()
    
    # Prepare dishes and cooking times
    dishes = [("Pizza", 3), ("Pasta", 2), ("Salad", 1)]
    results = [None] * len(dishes)  # Shared list to store results
    threads = []
    
    # Create and start threads
    for i, (dish_name, cook_time) in enumerate(dishes):
        thread = threading.Thread(
            target=cook_with_result,
            args=(dish_name, cook_time, results, i),
            name=f"Chef-{i+1}"
        )
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"\n[SUCCESS] All dishes completed: {results}")
    print(f"[TIME] Total time: {end_time - start_time:.2f} seconds")
    print(f"[THREADS] Active threads: {threading.active_count()}")

def cook_task(dish_name, cook_time):
    """Simulates cooking a specific dish in a separate thread"""
    thread_name = threading.current_thread().name
    print(f"[*] Thread {thread_name}: Starting to cook {dish_name}...")
    time.sleep(cook_time)  # Simulates cooking time (blocks this thread only)
    print(f"[OK] Thread {thread_name}: {dish_name} is ready!")
    return dish_name

def main_with_executor():
    """Alternative approach using ThreadPoolExecutor"""
    from concurrent.futures import ThreadPoolExecutor, as_completed
    
    print("[CHEF] Starting to cook with ThreadPoolExecutor...")
    start_time = time.time()
    
    dishes = [("Pizza", 3), ("Pasta", 2), ("Salad", 1)]
    
    # Using ThreadPoolExecutor for cleaner thread management
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix="Chef") as executor:
        # Submit all tasks
        future_to_dish = {
            executor.submit(cook_task, dish_name, cook_time): dish_name 
            for dish_name, cook_time in dishes
        }
        
        # Collect results as they complete
        results = []
        for future in as_completed(future_to_dish):
            dish_name = future_to_dish[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                print(f"[ERROR] {dish_name} generated an exception: {exc}")
    
    end_time = time.time()
    print(f"\n[SUCCESS] All dishes completed: {results}")
    print(f"[TIME] Total time: {end_time - start_time:.2f} seconds")

# Run the threading examples
if __name__ == "__main__":
    print("=== Example 1: Manual Thread Management ===")
    main()
    
    print("\n=== Example 2: ThreadPoolExecutor ===")
    main_with_executor()

"""
USEFUL THREADING FUNCTIONS AND EXAMPLES:

Core Threading Classes:
- threading.Thread(target=function, args=tuple): Create a new thread
- threading.Lock(): Mutex for synchronizing access to shared resources
- threading.RLock(): Reentrant lock (can be acquired multiple times by same thread)
- threading.Semaphore(value): Limit number of threads accessing a resource
- threading.Event(): Simple communication between threads

Thread Management:
- thread.start(): Start thread execution
- thread.join(timeout=None): Wait for thread to complete
- thread.is_alive(): Check if thread is still running
- threading.current_thread(): Get current thread object
- threading.active_count(): Number of active threads

Synchronization Primitives:
- threading.Barrier(parties): Synchronization point for multiple threads
- threading.Condition(): More complex synchronization with wait/notify
- queue.Queue(): Thread-safe queue for communication between threads

High-Level Threading:
- concurrent.futures.ThreadPoolExecutor: Manage pool of worker threads
- concurrent.futures.as_completed(): Iterate over futures as they complete
- concurrent.futures.wait(): Wait for futures to complete with various options

Real-World Examples:
1. File processing:
   def process_file(filename):
       with open(filename, 'r') as f:
           return len(f.read())
   
   with ThreadPoolExecutor() as executor:
       results = list(executor.map(process_file, file_list))

2. Web scraping:
   def fetch_url(url):
       response = requests.get(url)
       return response.text
   
   with ThreadPoolExecutor(max_workers=10) as executor:
       futures = [executor.submit(fetch_url, url) for url in urls]

3. Thread-safe counter:
   lock = threading.Lock()
   counter = 0
   
   def increment():
       global counter
       with lock:
           counter += 1

4. Producer-Consumer with Queue:
   import queue
   q = queue.Queue()
   
   def producer():
       for i in range(10):
           q.put(f"item-{i}")
   
   def consumer():
       while True:
           item = q.get()
           print(f"Processing {item}")
           q.task_done()

Threading vs Asyncio:
- Threading: True parallelism, good for I/O-bound tasks, uses more memory
- Asyncio: Cooperative concurrency, single-threaded, more efficient for many I/O operations
- Use threading when you need true parallelism or working with blocking libraries
- Use asyncio for high-concurrency I/O operations or when you can use async libraries

Common Pitfalls:
- Race conditions: Use locks to protect shared data
- Deadlocks: Be careful with lock ordering
- GIL limitation: Threading doesn't help with CPU-bound tasks in Python
- Resource sharing: Use thread-safe data structures
"""
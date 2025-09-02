"""
Asyncio Concept:
Asyncio is Python's built-in library for asynchronous programming, enabling concurrent 
execution of tasks without using multiple threads or processes. It's based on an event 
loop that manages and switches between tasks efficiently. The key insight is cooperative 
multitasking: when a task encounters a blocking operation (like await asyncio.sleep()), 
it voluntarily yields control back to the event loop, allowing other tasks to run. 

Perfect for I/O-bound operations (network requests, file operations, database queries) 
where tasks spend time waiting. In our cooking example, without asyncio it would take 
6 seconds (3+2+1) sequentially, but with asyncio it takes only 3 seconds because all 
dishes cook concurrently.
"""

import asyncio
import time

async def cook_task(dish_name, cook_time):
    """Simulates cooking a specific dish"""
    print(f"[*] Starting to cook {dish_name}...")
    await asyncio.sleep(cook_time)  # Simulates cooking time
    print(f"[OK] {dish_name} is ready!")
    return dish_name

async def main():
    """Main function that coordinates the tasks"""
    print("[CHEF] Starting to cook multiple dishes...")
    start_time = time.time()
    
    # Execute tasks concurrently
    tasks = [
        cook_task("Pizza", 3),
        cook_task("Pasta", 2),
        cook_task("Salad", 1)
    ]
    
    # Wait for all tasks to complete
    completed_dishes = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"\n[SUCCESS] All dishes completed: {completed_dishes}")
    print(f"[TIME] Total time: {end_time - start_time:.2f} seconds")

# Run the asynchronous program
if __name__ == "__main__":
    asyncio.run(main())

"""
USEFUL ASYNCIO FUNCTIONS AND EXAMPLES:

Core Functions:
- asyncio.run(main()): Entry point to run async programs (Python 3.7+)
- await asyncio.sleep(seconds): Non-blocking sleep, allows other tasks to run
- asyncio.gather(*tasks): Run multiple tasks concurrently, wait for all to complete
- asyncio.create_task(coroutine): Schedule a coroutine to run concurrently

Task Management:
- asyncio.wait_for(task, timeout): Run task with timeout limit
- asyncio.wait(tasks): Wait for tasks with more control options
- asyncio.as_completed(tasks): Iterate over tasks as they complete
- asyncio.shield(task): Protect task from cancellation

Real-World Examples:
1. Web API calls:
   async with aiohttp.ClientSession() as session:
       response = await session.get('https://api.example.com/data')

2. Database operations:
   async with aiopg.create_pool(dsn) as pool:
       async with pool.acquire() as conn:
           result = await conn.fetch('SELECT * FROM users')

3. File operations:
   async with aiofiles.open('file.txt', 'r') as f:
       content = await f.read()

4. Multiple HTTP requests concurrently:
   urls = ['url1', 'url2', 'url3']
   tasks = [fetch_url(url) for url in urls]
   results = await asyncio.gather(*tasks)

5. Producer-Consumer pattern:
   queue = asyncio.Queue()
   producer_task = asyncio.create_task(producer(queue))
   consumer_task = asyncio.create_task(consumer(queue))

Common Patterns:
- Use asyncio for I/O-bound tasks (network, file, database)
- Don't use for CPU-intensive tasks (use multiprocessing instead)
- Always use 'await' with async functions
- Create tasks with asyncio.create_task() for concurrent execution
- Handle exceptions properly in async code with try/except blocks
"""
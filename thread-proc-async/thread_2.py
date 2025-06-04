from threading import current_thread, Thread
from time import sleep, perf_counter

thread = current_thread()
print(f"Thread name: {thread.name}")


def task():
    print("Starting task...")
    sleep(1)
    print("Task completed!")


if __name__ == "__main__":
    start_time = perf_counter()
    t1 = Thread(target=task)
    t2 = Thread(target=task)
    t3 = Thread(target=task)
    t1.start()
    t2.start()
    t3.start()
    t1.join()  # Ensure t1 completes before starting t2 and t3
    t2.join()  # Ensure t2 completes before starting t3
    t3.join()  # Wait for all threads to complete
    end_time = perf_counter()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

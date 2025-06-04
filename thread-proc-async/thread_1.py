from threading import current_thread
from time import sleep, perf_counter
import sys

gil_enabled = sys._is_gil_enabled()
sys.gil

print(f"GIL enabled: {gil_enabled}")
# https://geekpython.in/how-to-disable-gil-in-python

thread = current_thread()
print(f"Thread name: {thread.name}")


def task():
    print("Starting task...")
    sleep(1)
    print("Task completed!")


if __name__ == "__main__":
    start_time = perf_counter()
    task()
    task()
    task()
    end_time = perf_counter()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

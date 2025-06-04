from threading import current_thread, Thread
from time import sleep, perf_counter


def task(id):
    # print(f"Thread {id} starting task...")
    sleep(1)
    # print(f"Thread {id} completed task!")


if __name__ == "__main__":
    start_time = perf_counter()
    threads = []
    for i in range(100000):
        thread = Thread(target=task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = perf_counter()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

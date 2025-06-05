from time import sleep, perf_counter
from multiprocessing import Process, Queue, set_start_method


def worker(duration, queue):
    sleep(duration)
    queue.put(f"Process completed after ~{duration} seconds")


def start_processes(count):
    processes = []
    for duration in range(1, count + 1):
        queue = Queue()
        proc = Process(target=worker, args=(duration, queue))
        proc.start()
        processes.append((proc, queue, duration))
    return processes


def handle_processes(processes, timeout):
    deadline = perf_counter() + timeout
    for proc, queue, duration in processes:
        remaining = deadline - perf_counter()
        if remaining > 0:
            proc.join(timeout=remaining)
        if proc.is_alive():
            proc.terminate()
            proc.join()
            print(f"Process {duration} terminated (took longer than {timeout} seconds)")
        elif not queue.empty():
            print(queue.get())


def main():
    processes = start_processes(10)
    handle_processes(processes, 5)


if __name__ == "__main__":
    set_start_method("spawn")
    start = perf_counter()
    main()
    stop = perf_counter()
    print(f"Time taken: {stop - start:.4f} seconds")

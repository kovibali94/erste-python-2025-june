from time import sleep, perf_counter
from multiprocessing import Process, Queue
import multiprocessing


def proc(sec, queue):
    sleep(sec)
    queue.put(f"Process completed after {sec} seconds")


def main():
    processes = []

    for i in range(1, 11):
        q = Queue()
        p = Process(target=proc, args=(i, q))
        p.start()
        processes.append((p, q, i))

    deadline = perf_counter() + 5 

    for p, q, i in processes:
        remaining = deadline - perf_counter()
        if remaining > 0:
            p.join(timeout=remaining)
        if p.is_alive():
            p.terminate()
            p.join()
            print(f"Process {i} terminated (took longer than 5 seconds)")
        else:
            if not q.empty():
                result = q.get()
                print(result)


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    start = perf_counter()
    main()
    stop = perf_counter()
    print(f"Time taken: {stop - start:.4f} seconds")

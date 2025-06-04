from time import sleep, perf_counter
import multiprocessing


def proc():
    sleep(2)


if __name__ == "__main__":
    start = perf_counter()
    # sync
    # proc()
    # proc()
    p1 = multiprocessing.Process(target=proc)
    p2 = multiprocessing.Process(target=proc)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    stop = perf_counter()
    print(f"Time taken: {stop - start:.4f} seconds")

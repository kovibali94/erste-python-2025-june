from time import sleep, perf_counter
import multiprocessing


def proc(sec):
    sleep(sec)
    return f"Process completed after {sec} seconds"


def main():
    pool = multiprocessing.Pool(processes=10)
    args = [i for i in range(1, 11)]
    results = pool.map(proc, args)
    pool.close()
    print(results)


if __name__ == "__main__":
    start = perf_counter()
    main()
    stop = perf_counter()
    print(f"Time taken: {stop - start:.4f} seconds")

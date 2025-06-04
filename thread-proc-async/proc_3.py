from time import sleep, perf_counter
import multiprocessing


results = []


def proc(sec):
    sleep(sec)
    return f"Process completed after {sec} seconds"


def succeess_callback(proc_result):
    global results
    results = proc_result


def error_callback(proc_result):
    try:
        print(f"Error occurred: {proc_result}")
    except Exception as e:
        print(f"Exception in error callback: {e}")


def main():
    pool = multiprocessing.Pool(processes=10)
    args = [i for i in range(1, 11)]
    # pool.map_async(proc, args, callback=succeess_callback)
    # pool.close()
    # én mondom, hogy várjuk meg míg a processzek lefutnak
    # pool.join()
    # print(results)
    res = pool.map_async(
        proc, args, callback=succeess_callback, error_callback=error_callback
    )
    print(res.get(timeout=5))  # Get results with a timeout


if __name__ == "__main__":
    start = perf_counter()
    main()
    stop = perf_counter()
    print(f"Time taken: {stop - start:.4f} seconds")

import multiprocessing
import time
import random


def worker(name, result_queue):
    sleep_time = random.randint(1, 10)
    print(f"{name} indul, vár {sleep_time} másodpercet...")
    time.sleep(sleep_time)
    result = f"{name} kész, eredmény: {sleep_time}"
    result_queue.put(result)


def main():
    processes = []
    result_queue = multiprocessing.Queue()
    process_names = ["P1", "P2", "P3"]

    for name in process_names:
        p = multiprocessing.Process(target=worker, args=(name, result_queue))
        p.start()
        processes.append(p)

    # Várunk az első eredményre
    result = result_queue.get()
    print(f"\nELSŐ befejezett folyamat eredménye: {result}")

    # A többi folyamatot megpróbáljuk leállítani
    for p in processes:
        if p.is_alive():
            print(f"{p.name} megszakítása...")
            p.terminate()
            p.join()

    print("Összes többi folyamat leállítva.")


if __name__ == "__main__":
    main()

from concurrent.futures import ThreadPoolExecutor
from time import sleep


def log_service(thread_name, id):
    while logging:
        sleep(1)
        print(f"Log service running in thread with ID: {id}, thread: {thread_name}")


if __name__ == "__main__":
    max_workers = 5
    logging = True
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # args = ((f"Thread-{i}", i) for i in range(1, max_workers + 1))
        # executor.map(log_service, *zip(*args))
        for i in range(max_workers):
            thread_name = f"LogServiceThread{i + 1}"
            executor.submit(log_service, thread_name, i + 1)
        sleep(5)
        logging = False

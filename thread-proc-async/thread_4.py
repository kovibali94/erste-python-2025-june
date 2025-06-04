from threading import current_thread, Thread
from time import sleep


def log_service(id):
    while True:
        sleep(1)
        thread = current_thread()
        print(f"Log service running in thread: {thread.name} with ID: {id}")


if __name__ == "__main__":
    Thread(target=log_service, args=(1,), daemon=True, name="LogServiceThread1").start()
    Thread(target=log_service, args=(2,), daemon=True, name="LogServiceThread2").start()
    print("Main thread is doing other work...")
    sleep(5)
    print("Main thread ended.")

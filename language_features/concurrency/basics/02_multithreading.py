import threading
import time


def task(name):
    print(f"Starting task {name}")
    time.sleep(2)  # Simulates an I/O operation
    print(f"Finished task {name}")


if __name__ == "__main__":
    """Multithreading => best for I/O-bound tasks"""

    # Run tasks concurrently using threads
    start: float = time.time()

    t1 = threading.Thread(target=task, args=("A"))
    t2 = threading.Thread(target=task, args=("B"))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end: float = time.time()
    print(f"Total time: {end - start:.2f} seconds")

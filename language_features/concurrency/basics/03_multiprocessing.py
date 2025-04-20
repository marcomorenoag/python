import time
from multiprocessing import Process


def task(name):
    print(f"Starting task {name}")
    time.sleep(2)  # Simulates CPU work (normally math-heavy work)
    print(f"Finished task {name}")


if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=task, args=("A"))
    p2 = Process(target=task, args="B")

    # Start different processes
    p1.start()
    p2.start()

    # Wait till all processes end
    p1.join()
    p2.join()

    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")

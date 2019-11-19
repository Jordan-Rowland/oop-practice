from multiprocessing import Process, cpu_count
from threading import Thread
import time
import os


class MuchCPU(Thread):
    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass


if __name__ == "__main__":
    procs = [MuchCPU() for f in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(f"Work took {time.time() - t} seconds.")

import multiprocessing as mp
import queue
import time
import numpy as np

def my_fn(x):
    time.sleep(np.random.rand())
    print(-x)
    return x

def worker(fn, jobs_q, results_q):

    for args in iter(jobs_q.get, None):

        res = fn(*args)
        results_q.put(res)

def apply_async_ll(fn, iterable, nprocs=2):

    jobs_q = mp.Queue(maxsize=nprocs)
    results_q = mp.Queue()

    procs = [mp.Process(target=worker, args=(fn, jobs_q, results_q)) for _ in range(nprocs)]
    for proc in procs:
        proc.start()

    it = iter(iterable)
    results = []

    consumed = True
    while True:

        try:
            if consumed:
                x = next(it)
                consumed = False
            jobs_q.put(x, block=False)
            consumed = True
        except queue.Full:
            res = results_q.get(block=True)
            results.append(res)
        except StopIteration:
            break

    for _ in range(nprocs):
        jobs_q.put(None, block=True)

    for proc in procs:
        proc.join()

    return results

if __name__ == '__main__':

    apply_async_ll(my_fn, ([x] for x in range(10)))

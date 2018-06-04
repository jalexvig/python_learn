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
    num_in, num_out = 0, 0
    while True:

        try:
            if consumed:
                x = next(it)
                consumed = False
            jobs_q.put(x, block=False)
        except queue.Full:
            res = results_q.get(block=True)
            results.append(res)
            num_out += 1
        except StopIteration:
            break
        else:
            num_in += 1
            consumed = True

    for _ in range(nprocs):
        jobs_q.put(None, block=True)

    # Need this bit since the process might not exit if there is still data left in the results_q. When objects in the
    # queue are large they are buffered. The process won't exit until the buffer is flushed
    # https://stackoverflow.com/questions/26025486/python-processes-not-joining
    while num_out < num_in:
        res = results_q.get(block=True)
        results.append(res)
        num_out += 1

    for proc in procs:
        proc.join()

    return results


if __name__ == '__main__':

    apply_async_ll(my_fn, ([x] for x in range(10)))

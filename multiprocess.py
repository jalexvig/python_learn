import multiprocessing as mp


def g(y):
    for x in range(y):
        print('gen ', x)
        yield x


def myfn(x):
    print('fn ', x)
    return x


if __name__ == '__main__':

    pool = mp.Pool(processes=2)

    # figure out if imap is effective
    # res = pool.imap(myfn, g(15))
    # input('pause')
    # for x in res:
    #     input('res %d' % x)

    pool.close()
    pool.join()

    res = map(myfn, g(15))
    input('pause')
    for x in res:
        input('res %d' % x)

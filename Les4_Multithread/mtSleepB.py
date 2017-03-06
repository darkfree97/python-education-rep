import _thread
from time import ctime, sleep


loops = [4, 2]


def loop(n_loop, n_sec, lock):
    print("Start loop ", n_loop, " at: ", ctime())
    sleep(n_sec)
    print("Loop ", n_loop, " done at: ", ctime())
    lock.release()


def main():
    print("Starting at: ", ctime())
    locks = []
    n_loops = range(len(loops))

    for i in n_loops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in n_loops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in n_loops:
        while locks[i].locked():
            pass

    print("All done at: ", ctime())

main()

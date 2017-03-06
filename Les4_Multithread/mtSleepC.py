import threading
from time import ctime, sleep


loops = [4, 2]


def loop(n_loop, n_sec, lock):
    print("Start loop ", n_loop, " at: ", ctime())
    sleep(n_sec)
    print("Loop ", n_loop, " done at: ", ctime())


def main():
    print("Starting at: ", ctime())
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print("All done at: ", ctime())

main()

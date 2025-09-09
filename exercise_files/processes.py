# Going to try here in a python file since it's not working
# in the jupyter notebook
from multiprocess import Process
import time
# now add threads
import threading

def long_square(num, results):
    time.sleep(1)
    print(num ** 2)
    print('Finished computing!')


results = {}
# - On Windows (and on platforms that use the “spawn” start method), each child process re-imports the main module.
# If process creation happens at import time (top-level), it recurses and the runtime aborts with the
# “An attempt has been made to start a new process before the current process has finished its bootstrapping phase” error.
# - The fix is to protect process creation with the if **name** == "**main**": guard.
# This is required whether you use the standard library multiprocessing or the third-party multiprocess.
if __name__ == '__main__':
    # This code sets up 2 processes
    # p1 = Process(target=long_square, args=(1, results))
    # p2 = Process(target=long_square, args=(2, results))
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    # This code shows how to setup multiple processes in one line
    # This is setting up 10 processes
    # processes = [Process(target=long_square, args=(n, results)) for n in range(0, 10)]
    # [p.start() for p in processes]
    # [p.join() for p in processes]

    # print(results)

    # Threads
    results = {}
    threads = [threading.Thread(target=long_square, args=(n, results)) for n in range(0, 10)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(results)
import threading

def do_every (interval, worker_func, iterations):
    if iterations != 0:
        threading.Timer (
            interval,
            do_every, [interval, worker_func, iterations-1]
        ).start ()

        worker_func ()

def print_hw ():
    print "hello world"

def print_so ():
    print "test = " , test
    c = 0
    for i in range(10000):
        c = i
    print c


# call print_so every second, 5 times total
do_every (0.0001, print_so, 3)
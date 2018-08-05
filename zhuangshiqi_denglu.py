import time


def consumer(name):
    while True:
        baozi = yield
        if baozi == 0:
            print("bao zi mei you hao!!!!!!")
        else:
            print("bao zi [%s] lai le , bei [%s] chi le" % (baozi, name))


def producer(name):
    c = consumer('A')
    c1 = consumer('B')
    next(c)
    next(c1)
    print("Some one start cooking bao zi !!!!!")
    for i in range(10):
        time.sleep(1)
        print("create 2 bao zi")
        c.send(i)
        c1.send(i)


producer("Alex")

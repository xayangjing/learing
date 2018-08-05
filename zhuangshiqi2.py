import time


def logger(flag=False):
    def show_time(f):
        def inner(*a, **b):
            start = time.time()
            f(*a, **b)
            end = time.time()
            print('spend: %s' % (end - start))
            if flag == 'true':
                print('runing time logged')
        return inner
    return show_time


@logger('true')
def add(*a, **b):
    sum = 0
    for i in a:
        sum += i
    print('sum= %i' % (sum))
    time.sleep(2)


def bar():
    print('Bar---------------------')


add(1, 2, 5, 7, 20)
bar()
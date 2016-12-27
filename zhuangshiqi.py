import time

print('Runing program 1')


def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('caculate runing time')
        print('running time: %s' % (end - start))
    return inner


@show_time
def foo():
    print('foo.........')


@show_time
def bar():
    print('bar ---------------')


foo()
bar()

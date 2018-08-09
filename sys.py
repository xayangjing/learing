import sys
print(sys.argv)


def post():
    print('ok')


def download():
    pass


if sys.argv[1] == 'post':
    post()

elif sys.argv[1] == 'dwonload':
    download()

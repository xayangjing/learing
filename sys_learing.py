import sys_learing
print(sys_learing.argv)


def post():
    print('ok')


def download():
    pass


if sys_learing.argv[1] == 'post':
    post()

elif sys_learing.argv[1] == 'dwonload':
    download()

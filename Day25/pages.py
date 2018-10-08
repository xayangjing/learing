import reflect


inp = input('please input url:>> ')

if hasattr(reflect, inp):
    func = getattr(reflect, inp)
    result = func()
    print (result)
else:
    print('404')
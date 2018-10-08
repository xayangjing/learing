import pickle

def foo():
    print ('ok')

f = open('pickle_test', 'wb')
data = pickle.dumps(foo)
f.write(data)
f.close()
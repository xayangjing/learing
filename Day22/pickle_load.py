import pickle


f = open('pickle_test', 'rb')

data = f.read()

data = pickle.loads(data)



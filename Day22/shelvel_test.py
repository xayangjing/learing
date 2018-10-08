import shelve


f = shelve.open('shelvel_test')


f['info'] = {'name': 'alex', 'age' : '22'}
f['shopping'] = {'name': 'alex', 'price': '-1000'}

# data = shelve.open('shelvel_test')
#
# f = data.get('info')
#
# print(data['info'])
#
# print(f)


data = f.get('info')

print(data)

data = f.get('shopping')

print(data)
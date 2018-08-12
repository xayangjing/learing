import re


s = 'hello world'

print(s.find('llo'))

ret = s.replace('ll','xx')

print(ret)

print(s.split(' '))

print(re.findall('alex', 'yuanshialexhaobuhao'))

ret = re.findall('w\w{2}l', 'hello world')
print(ret)

print(re.findall('w\w{2}l', 'hello world hello world'))


ret = re.findall('w..l', 'hello world')

print(ret)
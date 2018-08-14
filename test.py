import re
ret = re.search('\([^()]+\)', '((2+5)*2)')
print(ret.group())


s = '5.2/2222*200'

ret = re.search('\d+\.?\d* [*,/] \d+\.?\d* ', s)
ret = re.search('\d+\.?\d*[*,/]\d+\.?\d*', s)
print(ret.group())

print(re.findall('a[bcdad]c', 'abc'))

print(re.findall('[0-9]', '45abc3'))

print(re.findall('[^0-9]', '45abc3'))

print(re.findall('[\d]', '45abc3'))

print(re.findall('[^ab]', '44bdh"ab"3'))

print(re.findall(r'(ad)+', 'add'))


ret = re.findall('www.(?:\w+).com', 'www.baidu.com')
print(ret)


ret = re.split('[ab]', 'abcd')

print(ret)


ret = re.sub('\d', 'hello', 'abc5dcad6', 1)
print(ret)


ret = re.sub('\d', 'hello', 'abc5dcad6')
print(ret)


ret = re.subn('\d', 'hello', 'abc5dcad6')
print(ret)


ret = re.finditer('\d', 'ds3sys478a')
print(ret)

for i in ret:
     print(i.group())
# print(next(ret).group())


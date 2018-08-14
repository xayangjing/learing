import re


# s = 'hello world'
#
# print(s.find('llo'))
#
# ret = s.replace('ll','xx')
#
# print(ret)
#
# print(s.split(' '))
#
# print(re.findall('alex', 'yuanshialexhaobuhao'))
#
# ret = re.findall('w\w{2}l', 'hello world')
# print(ret)
#
# print(re.findall('w\w{2}l', 'hello world hello world'))
#
#
# ret = re.findall('w..l', 'hello world')
#
# print(ret)
#
# print(re.findall('^h...o', 'hjasfhello'))
#
# print(re.findall('^h...o', 'hjashello'))
#
#
# print(re.findall('a..x', 'hjasalexehello'))
#
# print(re.findall('a..x$', 'hjasalexehelloauyx'))
#
# print(re.findall('a.*li', 'fjjadfasdfalexli'))
# print(re.findall('a', 'uuadfasdfcca'))
# print(re.findall('ba*', 'uuadfasdfccba'))
#
#
# print(re.findall('.*', 'uuadfasdfccba'))
#
#
# print(re.findall('ab+', 'uuadfasdfccbab990123'))
# print(re.findall('a+b', 'uuadfasdfccbaaaaaaabccccb990123'))
#
#
# print(re.findall('a?b', 'uuadfasdfccbaaaaaaabccccb990123'))
#
#
# print(re.findall('a{5}b', 'aaaaab'))
#
# print(re.findall('a{3,5}b', 'aaaaab'))
#
# print(re.findall('^ab', 'aaaaab'))
#
# print(re.findall('a{2}b', 'abaaab'))
#
#
# print(re.findall('a[c,d,e]x', 'acxadxaex'))
#
#
# print(re.findall('[a-z]', 'adx'))
#
#
# print(re.findall('[.,*,,]', 'adx.*,'))


print(re.findall('[1-9,a-z,A-Z]', '123tyAS'))

print(re.findall('[^[a-z]', 'iui123kabc'))

print(re.findall('\d', 'abc123'))

print(re.findall('\d{11}', '13379297753johnyang18502990638'))
print(re.findall('\sasd', 'fak asd'))
print(re.findall('\Sasd', 'fak asd'))


print(re.findall('\W', 'fak asd'))


print(re.findall(r'I\b', 'Hellow, I am a LI$ST'))


print(re.search('sb','fajsbadfadsfsb'))

ret = re.search('sb', 'adadkkasbkkersb')

print(ret.group())




print(re.search('a.','ajss').group())
print(re.search('a+','ajss').group())

print(re.findall(r'\\', 'abc\de'))



m = re.search(r'\bblow', 'blow')
print(m)


print(re.search('(as)+', 'sdjkfasas').group())
print(re.search('(as)|3', 'sdjkf3as').group())

ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})', 'wakdsfa123/ooo')
print(ret.group())
print(ret.group('id'))
print(ret.group('name'))

print(re.match('asd', 'fhsasd'))

print(re.match('asd', 'asdfhsasd').group())

print(re.split('[k]', 'ajksal'))

print(re.split('[j,s]', '1sajksal'))

print(re.split('[j,s]', 'sdjksal'))

print(re.sub('a..x', 's..b', 'hfjasalexhf'))

obj = re.compile('\.com')

ret = obj.findall('fahasdasdf.comakkdf')

print(ret)
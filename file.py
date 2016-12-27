import sys
import time

file = open('file.txt', 'a', encoding='utf8')
# file.write('\n Hello world \n')
# file.write('\n Hello John \n')

file.close()

file = open('file.txt', 'r', encoding='utf8')

data = file.read()
# print(data)

file.close()

f = open('file.txt', 'r', encoding='utf-8')

for i in f:
    print(i.strip())

print(f.tell())

f.close()


for i in range(30):
    print('*', end='', flush=True)
    time.sleep(0.1)

f = open('file.txt', 'w+', encoding='utf8')
print(f.read())

f.write('\n好好好!!!!!')

f.close()

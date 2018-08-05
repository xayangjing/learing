import time

struct_time = time.localtime()
print(struct_time)
print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time))
print(time.strptime('2018-08-03 23:57:00', '%Y-%m-%d %H:%M:%S'))
a = time.strptime('2018-08-03 23:57:00', '%Y-%m-%d %H:%M:%S')
print(a.tm_year)
print(a.tm_mon)
print(a.tm_wday)

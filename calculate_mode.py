import re

source = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'


def check(s):
    flag = True

    if(re.findall('[a-zA-Z]', s)):
        print('Invalid')
        flag = False

    return flag


def format(s):
    s = s.replace(' ', '')
    s = s.replace('++', '+')
    s = s.replace('--', '-')


def cal_mul_div(s):

    return s

def cal_add_sub(s):

    return s

if (check(source)):
    strs = format(source)

    while re.search('\('):
        strs = re.search('\([^()]+\)', strs).group()
        strs = cal_mul_div(strs)
        strs = cal_add_sub(strs)

    else:
        strs = cal_mul_div(strs)
        strs = cal_add_sub(strs)





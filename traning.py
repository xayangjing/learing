# coding=utf-8
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'google': {},
                '网易': {},
                'souhu': {},
                '快手': {}
            },
            '中关村': {
                '优酷': {},
                '汽车之家': {}
            }

        },
        '朝阳': {
            '国贸': {
                'CICC': {},
                'HP': {},
                '渣打银行': {},
                'CCTV': {}
            },
            '望京': {
                '陌陌': {},
                '奔驰': {},
                '360': {},
            },
            '三里屯': {
                '优衣库': {},
                '苹果': {},
            }
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '阿太包子': {}
            },
            '天通苑': {
                '链家': {},
                '我爱我家': {}
            },
            '回龙观': {},
        },
    },
    '上海': {

    },
    '山东': {

    },
}
#print (menu)


while True:
    for key in menu:
        print(key)
    choice = input('>>>:').strip()
    if choice in menu:
        while True:
            for key2 in menu[choice]:
                print(key2)
            choice2 = input('>>>:').strip()
            if choice2 in menu[choice]:
                while True:
                    for key3 in menu[choice][choice2]:
                        print(key3)
                    choice3 = input('>>>:').strip()
                    if choice3 in menu[choice][choice2]:
                        while True:
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            choice4 = input('>>>:').strip()
                            print(choice4)
                            print('last leve')
                            print()

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

current_layer = menu
parent_layers = [] 

while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:
        continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == "b":
        if parent_layers:
            current_layer = parent_layers.pop()
    else:
        print("not found")


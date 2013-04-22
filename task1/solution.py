SIGNS = ['Водолей', 'Риби', 'Овен', 'Телец', 'Близнаци', 'Рак',
         'Лъв', 'Дева', 'Везни', 'Скорпион', 'Стрелец', 'Козирог']
DAYS = [20, 19, 21, 21, 21, 21, 22, 23, 23, 23, 22, 22]


def what_is_my_sign(day, month):
    if DAYS[month - 1] <= day:
        return signs[month - 1]
    return signs[month - 2]

"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    return (number+19)//20*20


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    return string[::-1]


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    return str(dictionary)[1:-1].replace(',', ';').replace("'", "")


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    if sub_string[::-1] in string:
        return True
    else:
        return False


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    b = {}
    for i in range(len(strings)):
        s = strings[i].split(' ')
        if int(s[3]) == int(s[0]) * int(s[1]) * int(s[2]):
            b[i] = strings[i]
    return list(b.values())


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    for j in string:
        if j == '#':
            string.find('#')
            string = string[:string.find('#') - 1] + string[string.find('#') + 1:]
    string = string.replace('#', '')
    return string


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    d = {}
    i = 0
    for j in lst:
        if j in d:
            d[j] += 1

        else:
            d[j] = 1
    k = 0
    for f in d.keys():
        if d[f] < 2:
            k += f
    return k


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    import re
    s = re.findall(r'\d+', string)
    for i in range(len(s)):
        s[i] = int(s[i])
    return max(s)


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    if len(str(number)) < 5:
        s = 5 - len(str(number))
        return '0' * s + str(number)
    #elif len(str(number)) > 5:
       # s = len(str(number)) - 5
       # return number / 10 ** s
    else:
        return str(number)


def t10(string):
    """
    Произведите смешивание цветов. Вам будет дана строка, необходимо смешать все пары цветов и вернуть результируюший
        цвет

    Комбинации цветов:    G G     B G    R G   B R
    Результирующий цвет:   G       R      B     G

    R R G B R G B B  <- ввод
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G  <-- вывод

    """
    mydict = {'GG': 'G', 'BG': 'R', 'GB': 'R', 'RG': 'B', 'GR': 'B', 'BR': 'G', 'RB': 'G', 'BB': 'B', 'RR': 'R'}
    s = ''
    for t in string:
        s += t + ' '
    s = s[:len(s) - 1].split(' ')
    d = {}
    while len(s) != 1:
        for i in range(len(s) - 1):
            d[i] = mydict.get(''.join([s[i], s[i + 1]]))
        s = list(d.values())
        d = {}
    return s[0]


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    s = lst[::-1]
    d = {}
    for i in range(1, len(lst) - 1):
        x = 0
        y = 0
        for k in lst[:i]:
            for t in lst[i + 1:]:
                x += k
                y += t
                if x == y:
                    d[i] = i

    if d == {}:
        return -1
    else:
        return list(d.values())[0]


def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    import re
    s = {}
    for i in range(len(lst)):
        s[i] = re.findall(r'\d+', lst[i])
    r = list(s.values())
    t = {}
    o = ''
    for j in range(len(r)):
        for i in r[j]:
            o += i
            t[j] = o
        o = ''
    v = {}
    for m in range(len(list(t.values()))):
        if list(t.values())[m][0] == '7':
            v[m] = '8' + list(t.values())[m][1:]
        else:
            v[m] = list(t.values())[m]

    return list(v.values())


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """

    s = {}
    f = {}
    d = max(len(str(number_1)), len(str(number_2))) - min(len(str(number_1)), len(str(number_2)))
    k = min(len(str(number_1)), len(str(number_2)))
    for i in range(1, k + 1):
        s[i] = (int(str(number_1)[-i]) + int(str(number_2)[-i]))
        if len(str(number_1)) != len(str(number_2)):
            for j in range(0, d):
                if len(str(number_1)) > len(str(number_2)):
                    f[j] = int(str(number_1)[j])
                else:
                    f[j] = int(str(number_2)[j])
    return int(str(list(f.values())).replace('[', '').replace(']', '').replace(', ', '') + str(
            list(s.values())[::-1]).replace('[', '').replace(']', '').replace(', ', ''))


def t14(string):
    """
    Преобразуйте математическое выражение (символьное) в буквенное выраэение

    Для операций используйте следующую таблицу
        { '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ' }
    Примеры:
        4 ** 9 -> Four To The Power Of Nine
        10 - 5 -> Ten Minus Five
        2 = 2  -> Two Equals Two
    """
    mydict = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
            '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten','+':   ' Plus ',  '-':   ' Minus ',
          '*':   ' Times ',
          '/':   ' Divided By ',
          '**':  ' To The Power Of ',
          '=':   ' Equals ', '!=':  ' Does Not Equal '}
    f = ''
    s = string.split(' ')
    for i in s:
        if i in mydict.keys():
            f += mydict.get(i)
    return f


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    rows_a = len(lst)
    cols_a = len(lst[0])

    t = 0
    k = 0
    s = [[0 for row in range(cols_a)] for col in range(rows_a)]
    for i in range(rows_a):
        s[i] = lst[i][::-1]
    if rows_a >= cols_a:
        for i in range(cols_a):
            t += lst[i][i]
            k += lst[i][i]
    else:
        for j in range(rows_a):
            t += lst[j][j]
            k += s[j][j]
    return t + k

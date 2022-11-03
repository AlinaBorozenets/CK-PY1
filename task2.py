def get_count_char(str_):
    str_dict = {}
    for t in str_:
        if t.isalpha():
            if t in str_dict:
                str_dict[t] += 1
            else:
                str_dict[t] = 1
    return str_dict


def procent(x):
    sum_x = 0
    for a in x:
        sum_x += x[a]
    for a in x:
        x[a] = round(x[a] / sum_x * 100, 1)
    return x


    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = main_str.lower()


print(get_count_char(main_str))
print(procent(get_count_char(main_str)))

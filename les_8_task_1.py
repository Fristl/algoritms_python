"""Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции: func("papa") : 6; func("sova") : 9
"""

import hashlib


def scs(text):
    text_h = hashlib.sha1(text.encode('utf-8')).hexdigest()
    h_none_str = hashlib.sha1(''.encode('utf-8')).hexdigest()
    list_hash = []

    for j in range(len(text)):
        for i in range(len(text) + 1):
            a = hashlib.sha1(text[j:i].encode('utf-8')).hexdigest()
            if a == text_h or a == h_none_str:
                continue
            if a not in list_hash:
                list_hash.append(a)
    return len(list_hash)


test_1 = 'papa'
test_2 = 'paPa'
test_3 = 'sova'
war_and_peace = 'Good news everyone!  today is very good day!'

print(test_1, scs(test_1))
print(test_2, scs(test_2))
print(test_3, scs(test_3))
print(scs(war_and_peace))

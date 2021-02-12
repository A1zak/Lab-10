#!/usr/bin/env python3
# -*- config: utf-8 -*-

#   Решить следующую задачу: основная ветка программы, не считая заголовков функций,
#   состоит из двух строки кода. Это вызов функции test() и инструкции if __name__ ==
#   '__main__' . В ней запрашивается на ввод целое число. Если оно положительное, то
#   вызывается функция positive(), тело которой содержит команду вывода на экран слова
#   "Положительное". Если число отрицательное, то вызывается функция negative(), ее тело
#   содержит выражение вывода на экран слова "Отрицательное".
#   Понятно, что вызов test() должен следовать после определения функций. Однако имеет ли
#   значение порядок определения самих функций? То есть должны ли определения positive() и
#   negative() предшествовать test() или могут следовать после него? Проверьте вашу гипотезу,
#   поменяв объявления функций местами. Попробуйте объяснить результат.

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def test():
    a = int(input('Введите целое число: '))
    if a > 0:
        positive()
    elif a < 0:
        negative()

if __name__ == '__main__':
    test()

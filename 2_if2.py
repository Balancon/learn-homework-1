"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
#Здесь я буду писать свою функцию!
def comparison_function(string_1, string_2):
    if isinstance(string_1, str) and isinstance(string_2, str):
    #    return 0
    #else:
        if string_1 == string_2:
            return 1
        elif (not (string_1 == string_2) and len(string_1) > len(string_2)):
            return 2
        elif string_2 == 'learn':
            return 3
    else:
        return 0


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
#    a = comparison_function('stiiing1', 'stringgggg2')
#    print(a)
    print(comparison_function(1, 'stringgg2'))
    #print(a)
    print(comparison_function('stringgg2', 'stringgg2'))
    #print(a)
    print(comparison_function('stringgg2', 'learn'))
    #print(a)
    print(comparison_function(10, 5))
    #print(a)

if __name__ == "__main__":
    main()

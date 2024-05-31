# Домашка номер 3!
"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def number_of_goods(sold_products, row):
    number_of_sold = 0
    phones_sold_number = 0
    for number_of_sold in range(len(sold_products[row]['items_sold'])):
        phones_sold_number += sold_products[row]['items_sold'][number_of_sold]
    return phones_sold_number

def avg_number_of_goods(sold_products, row):
    number_of_sold = 0
    phones_sold_number = 0
    average_sold = 0
    total_sold = len(sold_products[row]['items_sold'])
    for number_of_sold in range(len(sold_products[row]['items_sold'])):
        phones_sold_number += sold_products[row]['items_sold'][number_of_sold]
    average_sold = int(phones_sold_number / total_sold)
    return average_sold

def avg_number_of_all_goods(sold_products):
    category = 0
    number_of_sold = 0
    phones_sold_number = 0
    average_sold = 0
    total_sold = len(sold_products['product']['items_sold'])
#    total_sold = len(sold_products)
#    total_sold = len(sold_products[],[])
#    print(total_sold)
    
#    iphone_12_dict = dict(sold_products[0][1][])
#    print(iphone_12_dict)

#    params = sold_products.get("items_sold")
    print(sold_products)

    for category in range(len(sold_products[category]['items_sold'])):
        print("category = ", category)
        print("Range of category:", range(len(sold_products[category]['items_sold'])))
        for number_of_sold in range(len(sold_products[category]['items_sold'])):
            print("number_of_sold = ", number_of_sold)
            phones_sold_number += sold_products[category]['items_sold'][number_of_sold]
            print(phones_sold_number)
        average_sold = int(phones_sold_number / total_sold)
    return average_sold

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sold_products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    print("Кол-во проданных iPhone12: ", number_of_goods(sold_products, 0))
    print("Кол-во проданных Xiaomi Mi11: ", number_of_goods(sold_products, 1))
    print("Кол-во проданных Samsung Galaxy 21: ", number_of_goods(sold_products, 2), "\n")

    print("Среднее кол-во проданных iPhone12: ", avg_number_of_goods(sold_products, 0))
    print("Среднее кол-во проданных Xiaomi Mi11: ", avg_number_of_goods(sold_products, 1))
    print("Среднее кол-во проданных Samsung Galaxy 21: ", avg_number_of_goods(sold_products, 2), "\n")

    print("Кол-во проданных Samsung Galaxy 21: ", number_of_goods(sold_products, 0) + number_of_goods(sold_products, 1) + number_of_goods(sold_products, 2), "\n")
    
#    print("Среднее кол-во всех проданных устройств: ", avg_number_of_all_goods(sold_products))

if __name__ == "__main__":
    main()

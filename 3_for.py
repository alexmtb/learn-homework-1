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


def main(sales_data):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    # variables for saving processed data
    output_data = []
    all_summ = 0
    all_count = 0
    for product in sales_data:
        sell_summ = sum(product['items_sold'])
        sell_mean = round(sell_summ / len(product['items_sold']), 1)
        all_summ += sell_summ
        all_count += len(product['items_sold'])
        output_data.append({
            product['product']: {'Всего продаж': sell_summ, 'Средние продажи': sell_mean}
        })

    output_data.append({'Всего товаров продано': all_summ})
    output_data.append({'В среднем товаров продано': round(all_summ / all_count, 1)})

    return output_data


sales_data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


if __name__ == "__main__":
    statistics = main(sales_data)
    [print(stat) for stat in statistics]

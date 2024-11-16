
def total_revenue(purchases):
    total_pro = 0
    for i in purchases:
        total_pro = total_pro + i['price']*i['quantity']

    return print(f'Общая выручка: {total_pro} ')


def items_by_category(purchases):
    prod_dict = {}
    for y in purchases:
        prod_dict[y['category']] = []
    for x in purchases:
        prod_dict[x['category']].append(x['item'])
    return print(f'Товары по категориям: {prod_dict}')


def expensive_purchases(purchases, min_price):
    min_lst = []
    for x in purchases:
        if x['price']*x['quantity'] > min_price:
            min_lst.append(x)

    return print(f'Покупки дороже {min_price}: {min_lst}')


def average_price_by_category(purchases):
    new_dict = {}
    for y in purchases:
        new_dict[y['item']] = (y['category'], y['price'])
    print(new_dict)
    dct = {}
    tmp = {}
    for name in new_dict:
        category, price = new_dict[name]
        if category in dct:
            dct[category] += price
            tmp[category] += 1
        else:
            dct[category] = price
            tmp[category] = 1

    for category in dct:
        dct[category] = dct[category] / tmp[category]
    return print(f'Средняя цена по категориям: {dct} ')


def most_frequent_category(purchases):
    max_prod = 0
    max_cat = 0
    for x in purchases:
        if x['quantity'] > max_prod:
            max_prod = x['quantity']
            max_cat = x['category']
    return print(f'Категория с наибольшим количеством проданных товаров: {max_cat}')




purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

min_price = 1.0

total_revenue(purchases)
items_by_category(purchases)
expensive_purchases(purchases, min_price)
average_price_by_category(purchases)
most_frequent_category(purchases)

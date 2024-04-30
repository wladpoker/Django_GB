from datetime import datetime, timedelta

# Предположим, что у нас есть следующие данные:
orders = [
    {'client': 'Alice', 'products': ['Product A', 'Product B'], 'date': datetime.now() - timedelta(days=2)},
    {'client': 'Alice', 'products': ['Product B', 'Product C'], 'date': datetime.now() - timedelta(days=10)},
    {'client': 'Bob', 'products': ['Product A', 'Product D'], 'date': datetime.now() - timedelta(days=20)},
    # Другие заказы...
]

# Функция для получения списка заказанных товаров за указанный период
def get_ordered_products(client, days):
    products_set = set()
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    for order in orders:
        if order['client'] == client and start_date <= order['date'] <= end_date:
            products_set.update(order['products'])
    
    return list(products_set)

# Вывод списка товаров за последние 7 дней
print("Заказанные товары за последние 7 дней:")
print(get_ordered_products('Alice', 7))

# Вывод списка товаров за последние 30 дней
print("Заказанные товары за последние 30 дней:")
print(get_ordered_products('Alice', 30))

# Вывод списка товаров за последние 365 дней
print("Заказанные товары за последние 365 дней:")
print(get_ordered_products('Alice', 365))
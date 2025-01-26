# Список покупок
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Функция для расчета общей выручки
def total_revenue(purchases):
    return sum(item['price'] * item['quantity'] for item in purchases)

# Функция для группировки товаров по категориям
def items_by_category(purchases):
    result = {}
    for item in purchases:
        category = item['category']
        if category not in result:
            result[category] = set()
        result[category].add(item['item'])
    return {k: list(v) for k, v in result.items()}

# Функция для выборки покупок дороже заданной цены
def expensive_purchases(purchases, min_price):
    return [item for item in purchases if item['price'] >= min_price]

# Функция для расчета средней цены по категориям
def average_price_by_category(purchases):
    category_totals = {}
    category_counts = {}
    for item in purchases:
        category = item['category']
        if category not in category_totals:
            category_totals[category] = 0
            category_counts[category] = 0
        category_totals[category] += item['price']
        category_counts[category] += 1
    return {category: category_totals[category] / category_counts[category] for category in category_totals}

# Функция для определения категории с наибольшим количеством проданных товаров
def most_frequent_category(purchases):
    category_quantities = {}
    for item in purchases:
        category = item['category']
        if category not in category_quantities:
            category_quantities[category] = 0
        category_quantities[category] += item['quantity']
    return max(category_quantities, key=category_quantities.get)

# Генерация отчета
def generate_report(purchases):
    print(f"Общая выручка: {total_revenue(purchases)}")
    print(f"Товары по категориям: {items_by_category(purchases)}")
    print(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}")
    print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
    print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")

# Вывод отчета
generate_report(purchases)

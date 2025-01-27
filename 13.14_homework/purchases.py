import ast
from collections import defaultdict

# Чтение данных из файла
def read_purchases_from_text(file_path):
    with open(file_path, mode="r") as file:
        content = file.read()
        # Извлекаем список данных с помощью ast.literal_eval
        purchases = ast.literal_eval(content.split('=')[1].strip())
    return purchases

# Функция для расчета общей выручки
def total_revenue(purchases):
    return sum(item['price'] * item['quantity'] for item in purchases)

# Функция для группировки товаров по категориям
def items_by_category(purchases):
    result = defaultdict(set)
    for item in purchases:
        result[item['category']].add(item['item'])
    return {k: list(v) for k, v in result.items()}

# Функция для выборки покупок дороже заданной цены
def expensive_purchases(purchases, min_price):
    return [item for item in purchases if item['price'] >= min_price]

# Функция для расчета средней цены по категориям
def average_price_by_category(purchases):
    category_totals = defaultdict(float)
    category_counts = defaultdict(int)
    for item in purchases:
        category = item['category']
        category_totals[category] += item['price']
        category_counts[category] += 1
    return {category: category_totals[category] / category_counts[category] for category in category_totals}

# Функция для определения категории с наибольшим количеством проданных товаров
def most_frequent_category(purchases):
    category_quantities = defaultdict(int)
    for item in purchases:
        category_quantities[item['category']] += item['quantity']
    return max(category_quantities, key=category_quantities.get)

# Генерация отчета
def generate_report(file_path):
    purchases = read_purchases_from_text(file_path)
    print(f"Общая выручка: {total_revenue(purchases)}")
    print(f"Товары по категориям: {items_by_category(purchases)}")
    print(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}")
    print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
    print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")


generate_report("purchases.txt")
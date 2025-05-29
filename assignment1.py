from collections import defaultdict

product_list = [
    ["Strawberry", "Fruit", 3.50, 40, 10],
    ["Broccoli", "Vegetable", 2.20, 25, 8],
    ["Cheddar", "Dairy", 5.00, 18, 4],
    ["Baguette", "Bakery", 2.80, 35, 2],
    ["Blueberry", "Fruit", 4.00, 22, 6],
    ["Spinach", "Vegetable", 1.80, 30, 12],
    ["Yogurt", "Dairy", 1.20, 50, 15],
    ["Croissant", "Bakery", 3.00, 28, 3],
]

tr = 0
low_stock_product_names = []
revenue_per_category = defaultdict(float)

for name, category, price, sold, stock_left in product_list:
    revenue = price * sold
    tr += revenue

    if stock_left < 5:
        low_stock_product_names.append(name)

    revenue_per_category[category] += revenue

print("Total Revenue:", tr)
print("Low Stock Items:", low_stock_product_names)

print("Category-wise Revenue:")
for category_name, category_total in revenue_per_category.items():
    print(f"{category_name}: {category_total}")

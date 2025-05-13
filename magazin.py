class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден.")


# Создание объектов класса Store
store1 = Store("Пятерочка", "Островитянова , дом 18")
store2 = Store("Магнит", "Профсоюзная , дом 169")
store3 = Store("Перекресток", "Антонова, дом 15")

# Добавление товаров в магазины
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)

store2.add_item("Хлеб", 1.0)
store2.add_item("Молоко", 1.5)

store3.add_item("Кофе", 2.0)
store3.add_item("Чай", 1.0)

# Протестируем методы для store1
print(f"Цены в магазине '{store1.name}': {store1.items}")

# Добавление товара
store1.add_item("Апельсины", 0.65)
print(f"После добавления апельсинов: {store1.items}")

# Обновление цены товара
store1.update_item_price("Бананы", 0.80)
print(f"После обновления цены бананов: {store1.items}")

# Удаление товара
store1.remove_item("Яблоки")
print(f"После удаления яблок: {store1.items}")

# Запрос цены на товар
price = store1.get_item_price("Бананы")
print(f"Цена бананов: {price}")
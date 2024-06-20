class Store:
    def __init__(self, name,address):
        self.name = name
        self.address = address
        self.items = {}
    def add_item(self, item_name, price):
        self.items[item_name] = price
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print("Нет продуктов с таким названием")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создаем объекты класса Store
store1 = Store("Магазин Фруктов", "ул. Первомайская, 10")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2 = Store("Овощной Рай", "пр. Ленина, 25")
store2.add_item("помидоры", 1.0)
store2.add_item("огурцы", 0.8)

store3 = Store("Домашний Магазин", "ул. Садовая, 5")
store3.add_item("молоко", 1.2)
store3.add_item("хлеб", 0.6)
class Store(object):
    def __init__(self, name,address):
        self.name = name
        self.address = address
        self.items = {}
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"товар {item_name} добавлен в магазин {self.name}")


    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"товар {item_name} удален из {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"цена на товар {item_name} обновлена в магазине {self.name}")
        else:
            print(f"товар {item_name} не найден в магазине {self.name}")


store1 = Store("Магазин Фруктов", "ул. Первомайская, 10")
store2 = Store("Овощной Рай", "пр. Ленина, 25")
store3 = Store("Домашний Магазин", "ул. Садовая, 5")

# Создаем объекты класса Stor

store1.add_item("яблоки", 60)
store1.add_item("бананы", 80)


store2.add_item("помидоры", 58)
store2.add_item("огурцы", 67)


store3.add_item("молоко", 49)
store3.add_item("хлеб", 54)

store1.remove_item("яблоки")

print(store1.get_price("бананы"))
store1.update_price("бананы", 70)



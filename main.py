class Basket:
    def __init__(self):
        self.data = []

    def add(self, product, price):
        self.data.append({'product': product, 'price': price})
        print(f"{product}-{price}-narxi savatga qo'shildi")

    def remove(self, product):
        for item in self.data:
            if item['product'] == product:
                self.data.remove(item)
                print(f"{product} savatdan olib tashlandi")
                return
        print(f"{product} savatda topilmadi.")

    def show(self):
        if not self.data:
            print("Savat bo'sh.")
        else:
            for item in self.data:
                print(f"{item['product']}: {item['price']}")

    def calculating(self):
        umumiy_narx = sum(item['price'] for item in self.data)
        print(f"Umumiy: {umumiy_narx}")


basket = Basket()
print(basket.add("Apple", 10000))
print(basket.show())
print(basket.remove("Olma"))

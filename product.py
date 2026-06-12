class Product:
    counter = 1000
    products = 0
    def __init__(self, name, price, stock):
        if price>0 and stock>=0:
            Product.products+=1
            self.name = name
            self.price = price
            self.stock = stock
            self.product_id = Product.counter
            Product.counter+=1
        else:
            raise ValueError("Invalid price or stock")

    @classmethod
    def get_total_products(cls):
        return cls.products

    def is_available(self, quantity):
        if quantity>0:
            return quantity<=self.stock
        else:
            raise ValueError("Invalid quantity")
    
    def reduce_stock(self, quantity):
        if self.is_available(quantity)==True:
            self.stock -= quantity
        else:
            raise ValueError("Invalid quantity")
            
    def restock(self, quantity):
        if quantity>0:
            self.stock += quantity
        else:
            raise ValueError("Invalid quantity")
        
    def update_price(self, new_price):
        if new_price>0:
            self.price = new_price
        else:
            raise ValueError("Invalid price")

    def __str__(self):
        return f"{self.name} for {self.price} Rs ({self.stock} left)"
    
    def get_details(self):
        return f"\nProduct Specifications:\nProduct Name: {self.name}\nProduct Price: {self.price} Rs\nProduct Stock: {self.stock} pieces left\nProduct ID: {self.product_id} "

p1 = Product("Hp Laptop", 32000, 15)
p2 = Product("Dell Laptop", 26000, 10)

p1.update_price(56000)
print(f"Updated Price of {p1.name}: {p1.price}")

print(p1.is_available(4))
p1.reduce_stock(4)
print(f"Stock of {p1.name}: {p1.stock}")

print("Total Products: ", Product.get_total_products())

print(p1.get_details())
print(p2.get_details())

print(p2)
class Product:
    counter = 1000
    products = 0
    def __init__(self, name, price, stock):
    
        Product.products+=1
        self.name = name
        self.price = price
        self.stock = stock
        self.product_id = Product.counter
        Product.counter+=1


    @classmethod
    def get_total_products(cls):
        return cls.products

    def is_available(self, quantity):
        if quantity <= self.stock:
            return True
            self.reduce_stock(quantity)
        else:
            return False
            
    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            return None
            
    def restock(self, quantity):
        if quantity>=0:
            self.stock += quantity
        else:
            return None
        
    def update_price(self, new_price):
        if new_price>0:
            self.price = new_price
        else:
            return None

    def __str__(self):
        return f"{self.name} for {self.price} Rs ({self.stock} left)"
    
    def get_details(self):
        return f"Product Name: {self.name}\nProduct Price: {self.price} Rs\nProduct Stock: {self.stock} pieces left\nProduct ID: {self.product_id} "

p1 = Product("Hp Laptop", 32000, 15)
p2 = Product("Dell Laptop", 26000, 10)

# p1.update_price(56000)
# print(p1.price)

# print(p1.is_available(4))
# p1.reduce_stock(4)
# print(p1.stock)

print("Total Products: ",Product.get_total_products())

print(p1.get_details())
print(p2.get_details())
from product import Product

class CartItem:
    cartitems = 0
    def __init__(self, product, quantity):
        self.product = product
        if quantity<=self.product.stock and quantity>0:
            self.quantity = quantity
            CartItem.cartitems+=1 
        else:
            raise ValueError("Invalid quantity, not available in stock")

    def get_total_price(self):
        return self.product.price * self.quantity
    
    def increase_quantity(self, quantity):
        if quantity>0 and (self.quantity+quantity)<=self.product.stock:
            self.quantity+= quantity
        else:
            raise ValueError("Invalid quantity")
        
    def decrease_quantity(self, quantity):
        dif = self.quantity - quantity
        
        if dif > 0 and quantity>0:
            self.quantity -= quantity
        elif dif ==0:
            self.quantity=0
            return 0
        else:
            raise ValueError("Invalid quantity")
        
    def get_details(self):
        return f"Cart Summary:\nProduct Name: {self.product.name}\nProduct Quantity: {self.quantity}\nTotal Price: {self.get_total_price()} Rs"

p1 = Product("Hp Laptop", 32000, 15)
i1 = CartItem(p1,2)

i1.increase_quantity(10)
i1.decrease_quantity(8)
print(i1.get_details())

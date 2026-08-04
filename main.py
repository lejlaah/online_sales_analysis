from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 1500, 3)
p2 = Product("Mouse", 25, 10)
p3 = Product("Keyboard", 60, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.display_products()

manager.total_inventory_value()

manager.remove_product("Mouse")
manager.display_products()

from cart import Cart
cart = Cart()

cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.display_cart()

print(cart.total_price())
from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product(" Gaming Laptop", 1500, 3)
p2 = Product("Mouse", 25, 10)
p3 = Product("Keyboard", 60, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.display_products()



manager.remove_product("Mouse")

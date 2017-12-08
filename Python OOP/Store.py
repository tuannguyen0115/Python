class Store(object):
    def __init__(self, product, location, owner):
        self.product = product
        self.location = location
        self.owner = owner
    
    def add_product(self, product):
        self.product.append(product)
        return self
    
    def remove_product(self, product):
        self.product.remove(product)
        return self

    def inventory(self):
        for item in self.product:
            print item
        return self

store = Store(["egg", "ham", "bacon"], "VA", "Tuan")

store.inventory()
print ""
store.add_product("bread")
store.inventory()
print ""
store.remove_product("egg")
store.inventory()
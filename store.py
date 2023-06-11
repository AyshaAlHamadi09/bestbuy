from bestbuy import products


#testing commented out line

class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        if product in self.list_of_products:
            self.list_of_products.remove(product)
        else:
            print("product does not exist in store")

    def get_total_quantity(self):
        count = 0
        for item in self.list_of_products:
            count += item.quantity
        return f"total number of items in store: {count} items"


    def get_all_products(self):
        active_products = []
        for item in self.list_of_products:
            if item.active == True:
                active_products.append(item)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        self.shopping_list = shopping_list
        for product, order_quantity in shopping_list:
            total_price += (product.price * order_quantity)
            remaining_quantity = product.quantity - order_quantity
            product.set_quantity(remaining_quantity)
        return f"total price is {total_price} dollars\nremaining quantity in store is {remaining_quantity}"


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    stock = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(stock[0], 1), (stock[1], 2)]))


if __name__ == '__main__':
    main()


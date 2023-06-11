import products
import store
import main


def test_normal_product():
    Hp_laptop = products.Product("Hp laptop", 300, 250)
    assert Hp_laptop.name == "Hp laptop"
    assert Hp_laptop.price == 300
    assert Hp_laptop.quantity == 250
    assert Hp_laptop.active == True

def test_product_with_empty_name():
    try:
        noname = products.Product(" ", 300, 250)
        assert noname.name != ""
    except ValueError as e:
        assert str(e) == "name cannot be empty"

def test_product_with_zero_quantity():
    finished = products.Product("finished", 300, 0)
    assert finished.quantity == 0
    assert finished.active == False

def test_product_with_negative_quantity():
    negative = products.Product("negative", 300, -50)
    assert negative.quantity == 0 #check if quantity resets to zero when input is negative
    assert negative.active == False


def test_product_with_negative_price():
    try:
        free = products.Product("free", -20, 250)
        assert free.price > 0
    except ValueError as e:
        assert str(e) == "price cannot be negative"


def test_normal_order():
    stock = [products.Product("item1", price=5, quantity=50),
             products.Product("item2", price=15, quantity=50),
             products.Product("item3", price=10, quantity=50)]

    shop = store.Store(stock)

    my_basket = [(products.Product("item1", price=5, quantity=50), 1),
                 (products.Product("item2", price=15, quantity=50), 1),
                 (products.Product("item3", price=10, quantity=50), 2)]

    assert shop.order(my_basket) == "total price is 40 dollars\ntotal number of remaining items in store: 146 items"


def test_order_more_than_available_stock():
    stock = [products.Product("item1", price=5, quantity=50),
             products.Product("item2", price=15, quantity=50),
             products.Product("item3", price=10, quantity=50)]

    shop = store.Store(stock)

    my_basket = [(products.Product("item1", price=5, quantity=50), 100),
                 (products.Product("item2", price=15, quantity=50), 1),
                 (products.Product("item3", price=10, quantity=50), 2)]
    try:
        shop.order(my_basket)
    except ValueError as e:
        assert str(e) == "not enough in stock"



    f"""def order(self, shopping_list):
        total_price = 0
        self.shopping_list = shopping_list
        for product, order_quantity in shopping_list:
            total_price += (product.price * order_quantity)
            remaining_quantity = product.quantity - order_quantity
            product.set_quantity(remaining_quantity)
        return f"total price is total_price dollars\nremaining quantity in store is remaining_quantity"""""





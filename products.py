from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price, quantity, promo= None):
        self.name = name
        if self.name.isspace() or len(self.name) == 0:
            raise ValueError("name cannot be empty")
        self.price = price
        if self.price < 0:
            raise ValueError("price cannot be negative")
        self.quantity = quantity
        self.promo = promo
        self.active = True
        if self.quantity <= 0:
            self.quantity = 0
            self.active = False


    def get_promo(self):
        return self.promo

    def set_promo(self, promotion):
        self.promo = promotion

    def get_quantity(self):
        return self.quantity
    
    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self.promo}")


    def buy(self, quantity, promo=None):
        try:
            if self.quantity < quantity or self.quantity < 1:
                raise ValueError(f"Available stock ({self.quantity}) is not enough for this purchase.")

            if promo is None:
                total_price = quantity * self.price
            else:
                total_price = promo.apply_promotion(self, quantity)

            self.quantity -= quantity
            return total_price

        except ValueError as e:
            print(e)


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, max_order):
        super().__init__(name, price, quantity)
        self.max_order = max_order



class Promotion(ABC):
    def __init__(self, promo_name):
        self.name = promo_name
    @abstractmethod
    def apply_promotion(self, product, order_quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, promo_name, percentage):
        super().__init__(promo_name)
        self.percentage = percentage

    def apply_promotion(self, product, order_quantity):
        discount = product.price * (self.percentage / 100)
        new_price = product.price - discount
        total = new_price * order_quantity
        return total

class SecondHalfPrice(Promotion):
    def __init__(self, promo_name):
        super().__init__(promo_name)

    def apply_promotion(self, product, order_quantity):
        if order_quantity > 2:
            discount_quantity = order_quantity // 2
            full_price_quantity = order_quantity - discount_quantity
            discounted_price = (product.price / 2) * discount_quantity
            full_price = product.price * full_price_quantity
            new_price = discounted_price + full_price
            return new_price

class BuyOneGetOneFree(Promotion):
    def __init__(self, promo_name):
        super().__init__(promo_name)

    def apply_promotion(self, product, order_quantity):
        if order_quantity > 2:
            free_quantity = order_quantity // 2
            full_price_quantity = order_quantity - free_quantity
            new_price = product.price * full_price_quantity
            return new_price

class ThirdOneFree(Promotion):
    def __init__(self, promo_name):
        super().__init__(promo_name)

    def apply_promotion(self, product, order_quantity):
        if order_quantity >= 3:
            free_quantity = order_quantity // 3
            full_price_quantity = order_quantity - free_quantity
            new_price = product.price * full_price_quantity
            return new_price






def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=56)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == '__main__':
    main()

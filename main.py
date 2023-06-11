import store
import products

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, max_order=1)
               ]

best_buy = store.Store(product_list)

# Create promotion catalog
second_half_price = products.SecondHalfPrice("Second Half price!")
third_one_free = products.ThirdOneFree("Third One Free!")
thirty_percent = products.PercentDiscount("30% off!", percentage=30)

# Add promotions to products
product_list[0].set_promo(second_half_price)
product_list[1].set_promo(third_one_free)
product_list[3].set_promo(thirty_percent)


def start(store_object):
    user_input = input("""1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit\n\n""")

    product_list = best_buy.get_all_products()

    if user_input == "1":
        for index, item in enumerate(product_list):
            if item.promo is None:
                print(f"{index + 1}. {item.name}, promotion: {item.promo} \n")
            else:
                print(f"{index + 1}. {item.name}, promotion: {item.promo.name} \n")



    if user_input == "2":
        print(best_buy.get_total_quantity())
        print("")

    if user_input == "3":
        while True:
            product_number = input("Which product # do you want? \n(type 'done' when you are ready to checkout)")
            if product_number != 'done':
                quantity = input("What amount do you want? \n")
                basket = []
                index = int(product_number) - 1
                basket.append((product_list[index], int(quantity)))
            elif product_number == 'done':
                print(best_buy.order(basket))
                print("")
                break


    if user_input == "4":
        exit()


def main():
    start(best_buy)


while __name__ == '__main__':
    main()

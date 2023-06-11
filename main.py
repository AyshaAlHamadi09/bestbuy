import store
import products

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(store_object):
    user_input = input("""1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit\n\n""")

    product_list = best_buy.get_all_products()

    if user_input == "1":
        for index, item in enumerate(product_list):
            print(f"{index + 1}. {item.name} \n")


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

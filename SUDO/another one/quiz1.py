from module_for_quiz import product

product_sell = [
    "Best price for Milk?\n (a) $70\n (b) $50\n (c) $78\n",
    "Best price for Beef?\n (a) $120\n (b) $130\n (c) $115\n",
    "Best price for Chicken?\n (a) $88\n (b) $86\n (c) $84\n",
    "Best price for Egg?\n (a) $20\n (b) $18\n (C) $21\n"
]

product_hub = [
    product(product_sell[0], "c"),
    product(product_sell[1], "b"),
    product(product_sell[2], "a"),
    product(product_sell[3], "c"),
]

def run_machine(product_hub):
    profit = 0
    for product in product_hub:
        sell = input(product.product)
        if sell == product.sell:
            profit += 1
            print("Gonna rich!\n")
        else:
            print("as usual!\n")
    print("You're in profitable sell in", profit , "/" + str(len(product_hub)) + " times")
run_machine(product_hub)
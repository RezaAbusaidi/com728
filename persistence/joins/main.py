import database

def menu():
    print("Please enter option")
    print("[1] Desiplay Stock levels")

    selection = int(input("your selection"))
    return selection

def run():
    selection = menu()
    if selection == 1:
        database.display_products_with_stock_levels()

run()

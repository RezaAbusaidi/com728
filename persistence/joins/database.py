import sqlite3



def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = (" SELECT name, description FROM product NATURAL JOIN stock ")
    cursor.execute(sql)
    records = cursor.fetchall()
    print(f'There are {len(records)} product records')

    for row in records:
        print(f"Product{records[0]}")
        print(f"Product{records[1]}")
        print(f"Product{records[2]}")
        print("")
    db.close()

display_products_with_stock_levels()
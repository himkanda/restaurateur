from database import cursor, db
import commonMethods


# Function to view the menu
def view_menu():
    query = "SELECT * FROM `menu`"
    cursor.execute(query)
    menu = cursor.fetchall()
    commonMethods.create_table("MENU", [["ID", "Name", "Price"]], menu)


# Function to get single menu item by id
def get_menu_item_by_id(menuId):
    query = "SELECT * FROM `menu` WHERE `id` = " + str(menuId)
    cursor.execute(query)
    menu_item = cursor.fetchall()
    return menu_item


# Function to get all menu item ids as a list
def get_menu_items_id():
    query = "SELECT `id` FROM `menu`"
    cursor.execute(query)
    menu_items_id = cursor.fetchall()
    return menu_items_id


# Function to get all order ids as a list
def get_orders_id():
    query = "SELECT `id` FROM `orders`"
    cursor.execute(query)
    orders_id = cursor.fetchall()
    return orders_id


# Function to add a new menu item
def add_menu_item(name, price):
    updatedName = commonMethods.pascal_case(name)
    query = "INSERT INTO `menu` (name, price) VALUES (%s, %s)"
    cursor.execute(query, (updatedName, price))
    db.commit()
    print("INFO -> Menu item added successfully!")


# Function to edit an existing menu item
def update_menu_item(menuId, name, price):
    updatedName = commonMethods.pascal_case(name)
    query = "UPDATE `menu` SET `name` = %s, `price` = %s WHERE (`id` = %s)"
    cursor.execute(query, (updatedName, price, menuId))
    db.commit()
    print("INFO -> Menu item updated successfully!")


# Function to delete a menu item
def delete_menu_item(menuId):
    query = "DELETE FROM `menu` WHERE (`id` = %s)"
    cursor.execute(query, (menuId,))  # needs a tuple (menuId,)
    db.commit()
    print("INFO -> Menu item deleted successfully!")


# Function to create a new order
def create_order(custName, phone, email, orderType, reference):
    updatedName = commonMethods.pascal_case(custName)
    query1 = "INSERT INTO `orders` (`customer_name`, `phone`, `email`, `order_type`, `reference`) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query1, (updatedName, phone, email, orderType, reference))
    db.commit()
    print("INFO -> The order ID is created successfully!")
    query2 = "SELECT id FROM `orders` ORDER BY id DESC LIMIT 1;"
    cursor.execute(query2)
    orderId = cursor.fetchall()
    # print(orderId[0][0])
    print("INFO -> Please note the Order ID ->" + str(orderId[0][0]))
    print(
        "INFO -> You can add items to this order by providing above mentioned Order ID."
    )


# Function to add items to an order
def add_items_to_order(orderId, items, quantities):
    for item, quantity in zip(items, quantities):
        query = "INSERT INTO `order_items` (`order_id`, `menu_id`, `quantity`) VALUES (%s, %s, %s);"
        cursor.execute(query, (orderId, item, quantity))
        db.commit()
    print("INFO -> Successfully added all items in order " + orderId)


# Function to fetch an order from order id
def fetch_order(orderId):
    cursor.execute("SELECT * FROM `orders` WHERE id = %s", (orderId,))
    order = cursor.fetchall()
    return order


# Function to get all items of an order
def fetch_items_from_order(orderId, showAmount):
    cursor.execute(
        "SELECT `menu_id`,`quantity` from `order_items` WHERE `order_id` = "
        + str(orderId)
    )
    order = cursor.fetchall()
    result = commonMethods.aggregate_orders(order)
    result2 = []
    for id, quantity in result:
        cursor.execute("SELECT `name`, `price` FROM `menu` WHERE id = %s", (id,))
        # Fetch the name from the result set
        menu_result = cursor.fetchone()
        name = menu_result[0]
        price = float(menu_result[1])
        amount = float(quantity) * price
        if showAmount == True:
            result2.append((name, price, quantity, amount))
        else:
            result2.append((name, price, quantity))

    return result2


def get_bill_by_id(orderId):
    cursor.execute("SELECT `id` from bill WHERE `order_id` = " + str(orderId))
    bill_id = cursor.fetchall()
    return bill_id


def add_bill(orderId, amount):
    bill_id = get_bill_by_id(orderId)
    if bill_id:
        print("bill already generated!")
    else:
        query = "INSERT INTO bill (`order_id`, `total_amount`) VALUES (%s, %s);"
        cursor.execute(query, (orderId, amount))
        db.commit()
        print("bill generated successfully!")


# Function to get all orders or get filtered orders
def fetch_orders_filtered(orderStatus, orderType, orderDate, print):
    query1 = "SELECT * FROM `orders`"
    match orderStatus:
        case "1":
            statusQuery = "(`id` IS NOT NULL)"  # get all
        case "2":
            statusQuery = "(`id` NOT IN (SELECT `order_id` FROM `bill`))"
        case "3":
            statusQuery = "(`id` IN (SELECT `order_id` FROM `bill`))"
        case _:
            print("enter correct")

    match orderType:
        case "1":
            typeQuery = "(`order_type` IS NOT NULL)"  # get all
        case "2":
            typeQuery = "(`order_type` = 'Dine In')"
        case "3":
            typeQuery = "(`order_type` = 'Take Away')"
        case _:
            print("enter correct")

    match orderDate:
        case "1":
            dateQuery = "(`order_date` IS NOT NULL)"  # get all
        case "2":
            dateQuery = "(DATE(`order_date`) = DATE(now()))"
        case "3":
            dateQuery = "(DATE(`order_date`) >= DATE_ADD(DATE(now()), INTERVAL -7 DAY))"
        case "4":
            dateQuery = (
                "(DATE(`order_date`) >= DATE_ADD(DATE(now()), INTERVAL -30 DAY))"
            )
        case _:
            print("enter correct")

    query2 = " WHERE " + statusQuery + " AND " + typeQuery + " AND " + dateQuery
    query = query1 + query2
    # print(query)
    cursor.execute(query)
    orders = cursor.fetchall()
    if print == "print":
        commonMethods.create_table(
            "ORDERS",
            [
                [
                    "ID",
                    "Customer Name",
                    "Phone",
                    "Email",
                    "Order Date",
                    "Order Type",
                    "Reference ID",
                ]
            ],
            orders,
        )
        return orders

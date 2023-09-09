import actions
import commonMethods as fn


def choice1():
    actions.view_menu()


def choice2():
    name = input("Enter the item name: ")
    fn.return_if_empty(name)
    price = float(input("Enter the item price: "))
    fn.return_if_empty(price)
    actions.add_menu_item(name, price)


def choice3():
    actions.view_menu()
    menuId = int(input("Enter the menu item ID to be updated: "))
    fn.return_if_incorrect_input(menuId, actions.get_menu_items_id())
    menu_item = actions.get_menu_item_by_id(menuId)
    fn.create_table("ITEM TO BE UPDATED", [["ID", "Name", "Price"]], menu_item)
    # get updated details of item
    name = input("Enter the new item name: ")
    fn.return_if_empty(name)
    price = float(input("Enter the new item price: "))
    fn.return_if_empty(price)
    # confirm to update
    consent = input(
        "If you update this item, it cannot be reverted back! Proceed? (y/n): "
    )
    if consent.lower() == "y":
        actions.update_menu_item(menuId, name, price)
    else:
        print("INFO -> Change is discarded, item was not updated!")


def choice4():
    actions.view_menu()
    menuId = int(input("Enter the menu item ID to be deleted: "))
    fn.return_if_incorrect_input(menuId, actions.get_menu_items_id())
    menu_item = actions.get_menu_item_by_id(menuId)
    fn.create_table("ITEM TO BE DELETED", [["ID", "Name", "Price"]], menu_item)
    # confirm to delete
    consent = input(
        "If you delete this item, it cannot be recovered again! Proceed? (y/n): "
    )
    if consent.lower() == "y":
        actions.delete_menu_item(menuId)
    else:
        print("INFO -> Change is discarded, item was not deleted!")


def choice5():
    custName = input("Please enter the customer name: ")
    fn.return_if_empty(custName)
    phone = input("Please enter customer phone (can skip): ")
    email = input("Please enter customer email (can skip): ")
    print(
        "Following types of order are available: \n1. Dine In \n2. Take Away \n3. Online"
    )
    choiceOfOrder = int(input("Enter the type of order from above: "))
    fn.return_if_incorrect_input(choiceOfOrder, (1, 2, 3))
    typeOfOrder = (
        "Dine In"
        if choiceOfOrder == 1
        else "Take Away"
        if choiceOfOrder == 2
        else "Online"
    )
    actions.create_order(custName, phone, email, typeOfOrder, fn.random_string(16))


def choice6():
    orderNumber = input("Enter the Order ID for the item(s): ")
    if str(orderNumber) not in str(actions.get_orders_id()):
        print("***ERROR*** -> Incorrect order ID!")
        return
    if len(actions.get_bill_by_id(orderNumber)) > 0:
        print(
            "***ERROR*** -> Cannot add items to an order whose Bill is already generated!"
            + "If this is intended, please create fresh order."
        )
        return
    print("Here is a list of all items in the menu: ")
    actions.view_menu()
    items = []
    quantities = []
    while True:
        item = int(
            input(
                "Enter the menu item number to order from above menu, for Order ID "
                + orderNumber
                + " : "
            )
        )
        fn.return_if_incorrect_input(item, actions.get_menu_items_id())
        quantity = int(input("Enter the quantity of this item to order (max. 5): "))
        fn.return_if_incorrect_input(quantity, (1, 2, 3, 4, 5))
        # add input data to list
        items.append(item)
        quantities.append(quantity)
        print("1. Add another item to order")
        print("2. No more items to add")
        print("3. Exit program")
        orderChoice = int(input("Enter your choice: "))
        if orderChoice == 1:
            continue
        elif orderChoice == 2:
            break
        else:
            exit()
    if items and quantities:
        actions.add_items_to_order(orderNumber, items, quantities)


def choice7():
    print("\n")
    print(
        "1. All Status Orders \n"
        + "2. Open Orders (bill not generated yet) \n"
        + "3. Closed Orders (bill is generated) "
    )
    orderStatus = str(input("Please filter by order status as described above: "))
    fn.return_if_incorrect_input(orderStatus, ("1", "2", "3"))
    print("\n")
    print("1. All Type Orders \n" + "2. Dine In Orders \n" + "3. Take Away Orders")
    orderType = str(input("Please filter by order type as described above: "))
    fn.return_if_incorrect_input(orderType, ("1", "2", "3"))
    print("\n")
    print(
        "1. All Date Orders \n"
        + "2. Today's Orders \n"
        + "3. Last 7 days Orders \n"
        + "4. Last 30 days Orders"
    )
    orderDate = str(input("Please filter by order date as described above: "))
    fn.return_if_incorrect_input(orderDate, ("1", "2", "3", "4"))

    actions.fetch_orders_filtered(orderStatus, orderType, orderDate, "print")


def choice8():
    orderId = input("Enter the order ID:")
    if str(orderId) not in str(actions.get_orders_id()):
        print("***ERROR*** -> Incorrect order ID!")
        return
    # return "Menu Item","Price","Quantity"
    orders = actions.fetch_items_from_order(orderId, showAmount=False)
    fn.create_table("Order Items", [["Menu Item", "Price", "Quantity"]], orders)


def choice9():
    orderId = input("Enter the order ID:")
    if str(orderId) not in str(actions.get_orders_id()):
        print("***ERROR*** -> Incorrect order ID!")
        return
    order_data_header = [
        "ID",
        "Name",
        "Phone",
        "Email",
        "Order Date & Time",
        "Order Type",
        "Reference ID",
    ]
    # returns "ID","Customer Name","Phone","Email","Order Date","Order Type","Reference ID"
    order_data = actions.fetch_order(orderId)
    # Create the final_list by pairing elements from a and b
    order_data_final = [
        [b_item, "-" if a_item == "" else a_item]
        for a_item, b_item in zip(order_data[0], order_data_header)
    ]
    # return "Menu Item","Price","Quantity","Amount"
    order_items_data = actions.fetch_items_from_order(orderId, showAmount=True)
    order_items_data_final = [list(t) for t in order_items_data]
    # calculates total
    subtotal = fn.calculate_final_bill(order_items_data)
    tax = subtotal * 0.08  # 8% tax is added
    total = subtotal + tax
    order_items_data_final.append(
        [
            "Subtotal",
            "",
            "",
            subtotal,
        ]
    )
    order_items_data_final.append(
        [
            "Tax (8%)",
            "",
            "",
            tax,
        ]
    )
    total_row_list = [
        [
            "Total :",
            "$" + str(total),
        ]
    ]
    fn.print_bill(order_data_final, order_items_data_final, total_row_list)
    actions.add_bill(orderId, total)

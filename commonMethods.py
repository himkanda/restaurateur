from tabulate import tabulate
import string
import random


def pascal_case(sentence):
    # Trim spaces at the start and end of the sentence
    sentence = sentence.strip()
    # Split the sentence into words
    words = sentence.split()
    # Capitalize the first letter of each word and convert the rest to lowercase
    words = [word.capitalize() for word in words]
    # Join the words with a single space
    pascal_case = " ".join(words)
    return pascal_case


def random_string(length):
    # initializing size of string
    N = length
    # using random.choices(),generating random strings
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k=N))
    # print result
    return str(res)


def main_menu():
    input("\nPress enter to continue to main menu ... ")
    print("\n# ............ # ............ # ............ # ............ #")


def create_table(tableName: str, header, data):
    # Create table_data from query result
    table_data = header  # Header row
    for row in data:
        table_data.append(row)
    # Print the table
    table = tabulate(table_data, headers="firstrow", tablefmt="grid")
    print("\n ~~~~~~~~~ %s ~~~~~~~~~" % (tableName.upper()))
    print(table)


def return_if_incorrect_input(input, validity):
    # for list of tuple of elements
    if (type(validity) == list) and (type(validity[0]) == tuple):
        print("cndition 1")
        num_found = False
        # Iterate through the list of tuples
        for tup in validity:
            if input in tup:
                num_found = True
                break  # No need to continue searching if num is found
        # Check if num was found or not
        if num_found == False:
            print("***ERROR*** -> Incorrect input!")
            exit()
    # for list or tuple of int or str elements
    elif (isinstance(validity, (list, tuple))) and (
        isinstance(validity[0], (int, str))
    ):
        if input not in validity:
            print("***ERROR*** -> Incorrect input!")
            exit()
    else:
        print("***ERROR*** -> Unidentified validity!")
        exit()


def return_if_empty(input):
    # for float, validate its more than 0.0
    if type(input) == float:
        if input <= 0.0:
            print("***ERROR*** -> Input cannot be equal to or less than zero!")
            exit()
    # for strings, validate its not empty
    if type(input) == str:
        if not input:
            print("***ERROR*** -> Please enter a non-blank input!")
            exit()


def aggregate_orders(input_list):
    # Create a dictionary to store the sums of second elements for each unique first element
    sums_dict = {}

    # Iterate through the input list and accumulate sums
    for first, second in input_list:
        if first in sums_dict:
            sums_dict[first] += second
        else:
            sums_dict[first] = second

    # Create the resulting list of tuples from the dictionary
    result_list = [(key, value) for key, value in sums_dict.items()]
    return result_list


def calculate_final_bill(inp):
    # inp contains "Menu Item","Price","Quantity"
    total = 0.0
    for data in inp:
        total += float(data[3])  # 4th value in tuple is the amount
    return total


def print_bill(
    order_data: list[list], order_items_data: list[list], total_data: [list[list]]
):
    # Create a single table with nested formatting for headers
    restaurant_table = tabulate(
        [
            [
                tabulate(
                    order_data,
                    tablefmt="plain",
                    disable_numparse=True,
                )
            ],
            [
                tabulate(
                    order_items_data,
                    headers=["Item", "Price", "Quantity", "Amount"],
                    tablefmt="github",
                    stralign="center",
                    disable_numparse=True,
                )
            ],
            [
                tabulate(
                    total_data,
                    tablefmt="plain",
                    stralign="right",
                    disable_numparse=True,
                )
            ],
        ],
        tablefmt="rounded_grid",
        headers=["RESTAURATEUR DINING INVOICE..."],
        stralign="left",
    )

    # Print the formatted bill with the restaurant name, customer info, and order details
    print(restaurant_table)

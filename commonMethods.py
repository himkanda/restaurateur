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
    if type(validity) == list:
        if input not in validity:
            print("***ERROR*** -> Incorrect input!")
            return


def return_if_empty(input):
    # for float, validate its more than 0.0
    if type(input) == float:
        if input <= 0.0:
            print("***ERROR*** -> Input cannot be equal to or less than zero!")
            return
    # for strings, validate its not empty
    if type(input) == str:
        if not input:
            print("***ERROR*** -> Please enter a non-blank input!")
            return

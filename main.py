"""
warehouse

"""
import sys
import csv
import logging

logging.basicConfig(level=logging.DEBUG)
"""
items = [
    {
        "name": "Milk", "quantity": 2, "unit": "l", "unit_price": 3.5
    },
{
        "name": "Coffee", "quantity": 25, "unit": "kg", "unit_price": 40
    },
{
        "name": "Sugar", "quantity": 1000, "unit": "kg", "unit_price": 3
    },
{
        "name": "Flour", "quantity": 2500, "unit": "kg", "unit_price": 2.5
    },
]
"""

items = []
sold_items = []

width = 56


def get_items():
    print("_" * width)
    print("|{:<10} | {:<10} | {:<8} | {:<15} |".format("Name", "Quantity", "Unit", "Unit Price (PLN)"))
    print("*" * width)
    for item in items:
        print("|{:<10} | {:<10} | {:<8} | {:>16} |".format(item["name"], item["quantity"], item["unit"], item["unit_price"]))

    return "_" * width


def add_item(name, quantity, unit_name, unit_price):
    items.append({"name": name, "quantity": quantity, "unit": unit_name, "unit_price": unit_price})

    return "Successfully added to warehouse. Current status: "


def sell_item(name, quantity):
    for item in items:
        if item["name"] == name:
            if item["quantity"] >= quantity:
                item["quantity"] -= quantity
                sold_items.append({"name": name, "quantity": quantity, "unit": item["unit"], "unit_price": item["unit_price"]})
                print("Successfully sold {} {} of {}".format(quantity, item["unit"], name))
            elif item["quantity"] < quantity:
                print("Not enough item, out of range choose less!")
            else:
                print("No item!")
    return "Current status: "


def get_income():
    get_income = sum([item["quantity"] * item["unit_price"] for item in sold_items])
    return get_income


def get_costs():
    get_costs = sum([item["quantity"] * item["unit_price"] for item in items])
    return get_costs


def show_revenue(income, costs):
    print("Revenue breakdown (PLN): ")
    print("Income: {:0.2f}".format(income))
    print("Costs: {:0.2f}".format(costs))
    revenue = income - costs
    return "Revenue: {} (PLN)".format(revenue)


def export_items_to_csv():
    with open(sys.argv[1], 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["name", "quantity", "unit", "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")

        writer.writeheader()
        for item in items:
            writer.writerow(item)
    return "Successfully exported data to warehouse.csv"


def export_sales_to_csv():
    with open('sales.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["name", "quantity", "unit", "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")

        writer.writeheader()
        for item in sold_items:
            writer.writerow(item)
    return "Successfully exported sale data to sales.csv"


def load_items_from_csv():
    items.clear()
    with open(sys.argv[1], encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'], row['quantity'], row['unit'], row['unit_price'])
            items.append(row)


if __name__ == "__main__":
    load_items_from_csv()
    while True:
        choice = input("What would you do? ")
        if choice == "exit":
            export_items_to_csv()
            export_sales_to_csv()
            print("Exiting Bye!")
            break
        elif choice == "show":
            print(get_items())
        elif choice == "add":
            print("Adding to warehouse... ")
            name = input("Item name: ")
            quantity = int(input("Item quantity: "))
            unit_name = input("Item unit of measure (l, kg, pcs): ")
            unit_price = float(input("Item price in PLN: "))
            print(add_item(name, quantity, unit_name, unit_price))
            print(get_items())
        elif choice == "sell":
            name = input("Item name: ")
            quantity = int(input("Item quantity to sell: "))
            print(sell_item(name, quantity))
            print(get_items())
        elif choice == "show_revenue":
            print(show_revenue(get_income(), get_costs()))
        elif choice == "save":
            print("Exporting data...")
            print(export_items_to_csv())
            print(export_sales_to_csv())
        elif choice == "load":
            print("This will overwrite all Your data! Are You sure?")
            if input("Y/N: ").lower() == "y":
                print(load_items_from_csv())
            else:
                print("Import cancelled.")
        else:
            print("Error!")





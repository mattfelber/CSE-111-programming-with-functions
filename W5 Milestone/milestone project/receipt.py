import csv
from datetime import datetime


def main():
    
    print("\nGROCERY STORE\n")
    key_column_index = 0
    try:

        dictionary_products = read_dictionary("products.csv", key_column_index)
        #print(dictionary_products)
        print()
        print("YOUR CART:")
        print('-' * 30)

        with open("request.csv", "rt") as request_csv:
            next(request_csv)
            request = csv.reader(request_csv)

            sum_quantity = 0
            sum_subtotal = 0
            sales_tax = 0
            total = 0
        
            for line in request:
                product = line[0]
                quantity = int(line[1])

                if product in dictionary_products:
                    
                    product_info = dictionary_products[product]

                    product_code = product_info[0]
                    product_name = product_info[1]
                    product_cost = float(product_info[2])
                                   
                    print(f"{product_name}: {quantity} @ ${product_cost}.")
                    sum_quantity += quantity
                    sum_subtotal += (quantity*product_cost)

                else:
                    print(f"Product with key '{product}' not found in dictionary.")

        sales_tax += (sum_subtotal*0.06)
        total += (sum_subtotal + sales_tax)

        print('-' * 30)
        print(f"Number of items in your cart: {sum_quantity:.2f}")
        print()
        print(f"Subtotal: ${sum_subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        print()
        print("Thank you!")
        dt = datetime.now()
        print(f"{dt:%A %I:%M %p}")
      
    except FileNotFoundError:
        print("File 'products.csv' not found.")
    except PermissionError:
        print("You don't have permission to access 'products.csv'.")
    except KeyError:
        print("Please check your values.")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary_products = {}

    with open(filename, "rt") as csv_file:
        next(csv_file)
        file = csv.reader(csv_file)

        for line in file:
            key = line[key_column_index]
            dictionary_products[key] = line


    return dictionary_products
            

# Call main to start this program.
if __name__ == "__main__":
    main()
import csv


def main():

    key_column_index = 0
    dictionary_products = read_dictionary("products.csv", key_column_index)
    print(dictionary_products)

    with open("request.csv", "rt") as request_csv:
        next(request_csv)
        request = csv.reader(request_csv)
        for line in request:
            product = line[0]
            quantity = line[1]

     
            # Check if the product exists in the dictionary before accessing its value
            if product in dictionary_products:
                # Access the product name and quantity from the dictionary
                
                product_info = dictionary_products[product]

                product_code = product_info[0]
                product_name = product_info[1]
                product_cost = product_info[2]
                
                print(f"{product_name}: {quantity} @ ${product_cost}.")

            else:
                print(f"Product with key '{product}' not found in dictionary.")

    



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
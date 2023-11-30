import csv

           
low_limit = 100000000
upper_limit = 999999999
key_column_index = 0
pair_column_index = 1

def main():
    name_column_index = 1
    student_dictionary = read_dictionary("students.csv", key_column_index)
    print(student_dictionary)
    key = get_key("Enter student's ID: ", low_limit, upper_limit)

    pair = student_dictionary[key]
    name = pair[name_column_index]
    print(name)
   
   


def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, "rt") as file:

        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if len(line) != 0:

                key = line[key_column_index]
                dictionary[key] = line

    return dictionary


def get_key(prompt, low_limit, upper_limit):

    while True:

        try:
            id = input(prompt)
            id = int(id)

            if id <= low_limit:
                print(f"Invalid Number: {id} is too small.")

            elif id >= upper_limit:
                print(f"Invalid Number: {id} is too large.")
                

            else:
                break

        except ValueError:
            print(f"Invalid command! {id} is not a number")

    key = str(id)
    
    return key




if __name__ == "__main__":
    main()

 

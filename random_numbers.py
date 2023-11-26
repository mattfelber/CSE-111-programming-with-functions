import random


def main():
    numbers_list = []
    append_random_numbers(numbers_list)
    append_random_numbers(numbers_list, 2)


def append_random_numbers(numbers_list, quantity=1):
    
    if quantity == 1:
        value = random.random()
        numbers_list.append(value)
        print(numbers_list)
    
    else:
        value = random.random()
        numbers_list.append(value)

        value = random.random()
        numbers_list.append(value)

        value = random.random()
        numbers_list.append(value)
        print(numbers_list)

main()




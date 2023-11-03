#You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
#which are the store’s slowest sales days. On Tuesday and Wednesday, 
#if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.

#If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the 
#subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. 
#Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

from datetime import datetime

subtotal = int(input("What is the subtotal?"))

today = datetime.isoweekday

#monday 0 tuesday 1 wednesday 2 thursday 3 friday 4 saturday 5 sunday 6


if subtotal > 50 and today == 1 or 2:
    discount = subtotal * 0.1
    tax = subtotal * 0.06

    discounted = subtotal - discount
    net_total = discounted + tax

    print(f"Discount = ${discount} \nTax: ${tax} \nNet Total: {net_total}")




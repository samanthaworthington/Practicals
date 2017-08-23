

total_price = 0

number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Enter number of items: "))
for i in range(0, number_of_items, 1):
    price_of_item= float(input("Enter the price of the item: "))
    total_price = price_of_item + total_price

if total_price > 100:
    total_price = total_price *0.9
print("Total Price: $ {:.2f}". format(total_price))

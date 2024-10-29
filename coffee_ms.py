from tabulate import tabulate
import math
menu = {
    "Toast":50,
    "Bread": 50,
    "Sandwich": 80,
    "Coffee": 30,
    "Tea": 20,
    "Juice":50
}
items = []
rates = []
quantities = []
print("Welcome to the Order System!")
print("Available items:")
print(tabulate(menu.items(), headers=["Item", "Rate"], tablefmt="grid"))
while True:
    ask = input("What do you want to order? (Type 'No' to finish) ").capitalize()
    if ask == 'No':
        break
    if ask in menu:
        rate = menu[ask]
        quantity = int(input(f"Enter quantity for :-  "))
        items.append(ask)
        rates.append(rate)
        quantities.append(quantity)
    else:
        print("Item not found in the menu. Please select a valid item.")
prlst = []
gst =0
total_amount = 0
for i in range(len(items)):
    amount = rates[i] * quantities[i]
    gst = amount + amount*0.12
    prlst.append((items[i], rates[i], quantities[i], amount,gst))
    total_amount += gst
main_amt=math.ceil(total_amount)
prlst.append(("Total_Payment", "", "","",main_amt))
print("\nYour Order Summary:")
print(tabulate(prlst, headers=["Item", "Rate", "Quantity", "Amount","Taxable"], tablefmt="grid", stralign="center", numalign="center"))
# cis129_lab03_coffeeShop.py
"""a short program in Python that asks the user for the number of coffee and muffins 
they are purchasing. The price of a cup of coffee is $5 and the price of a muffin is 
$4. Calculates 6% tax on the subtotal."""

numCoffees = int(input("Enter the number of coffees you want to order:"))
numMuffins = int(input("Enter the number of muffins you want to order:"))
numLattes = int(input("Enter the number of lattes you want to order:"))
numDanishes = int(input("Enter the number of danishes you want to order:"))

print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(numCoffees)
print("Number of muffins bought?")
print(numMuffins)
print("Number of lattes bought?")
print(numLattes)
print("Number of danishes bought?")
print(numDanishes)
print("***************************************\n\n")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(str(numCoffees) + " Coffee at $5 each: $ " + str(numCoffees * 5.0))
print(str(numMuffins) + " Muffin at $4 each: $ " + str(numMuffins * 4.0))
print(str(numLattes) + " Latte at $6 each: $ " + str(numLattes * 6.0))
print(str(numDanishes) + " Danish at $3 each: $ " + str(numDanishes * 3.0))
sum = float(numCoffees * 5.0) + float(numMuffins * 4.0) +  float(numLattes * 6.0) \
    +  float(numDanishes * 3.0)
print (sum)
print("6% tax: $ " + str(sum * 0.06))
total = str(sum + (sum * 0.06))
print("---------")
print("Total: $ " + str(total))
print("***************************************\n\n")
print("Thank you for shopping at the coffee-muffin-latte-danish shop, please come again!")

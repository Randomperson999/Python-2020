#Caleb Keller
#9/17/2020
#Cash Register Activity
numItems = 4
costPerItem = 10.00
taxRate = 0.08
subTotal = numItems*costPerItem
taxAmount = subTotal*taxRate
totalPrice = subTotal+taxAmount
#Initializes the variables and does basic calculations for cost and tax.
print("|-----Sales Reciept-----|")
print("|Number of items : "+str(numItems)+"    |")
print("|Cost per item   : "+str(costPerItem)+" |")
print("|Tax rate        : "+str(taxRate)+" |")
print("|Tax amount      : "+str(taxAmount)+"  |")
print("|TOTAL SALE PRICE: "+str(totalPrice)+" |")
print("|-----------------------|")
#Prints the valuses to the sceen with context.

"""A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
-Ask user for quantity.
-Suppose, one unit will cost 100.
-Judge and print total cost for user."""

tenPercentDiscount = 0.1
purchasedQuantatiy = int(input("How may items did you purchased? - "))
totalBillOnpurchasedQuantatiy = 100 * purchasedQuantatiy
if totalBillOnpurchasedQuantatiy >= 1000:
    billWithDiscound = totalBillOnpurchasedQuantatiy * tenPercentDiscount
    print("Total bills with 10% discounf:",billWithDiscound+totalBillOnpurchasedQuantatiy)
else:
    print("Totla bills:",totalBillOnpurchasedQuantatiy)
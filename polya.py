# If you have 5 types of coins (half dollar, quarter, dime, nickel, and penny), worth 50, 25, 10, 5 and 1 cents respectively, how many ways are there of making change for $1.25?
amt = 125
penny, nickel, dime, quarter, halfdollar = 1, 5, 10, 25, 50
ways = set()
for pennies in range(amt//penny + 1):
    for nickels in range(amt//nickel + 1):
        for dimes in range(amt//dime + 1):
            for quarters in range(amt//quarter + 1):
                for halfdollars in range(amt//halfdollar + 1):
                    total = penny*pennies + nickel*nickels + dime*dimes + quarter*quarters + halfdollar*halfdollars
                    if total == amt:
                        s = "P"*pennies + "N"*nickels + "D"*dimes + "Q"*quarters + "H"*halfdollars
                        ways.add(s)
print(len(ways))

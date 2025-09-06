# find the first non-repeated char 


name = "Karan"
for char in name: 
    if name.count(char) == 1:
        print("Non-repeated Char:", char)
        break

        

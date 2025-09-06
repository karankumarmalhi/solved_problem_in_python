# Find the duplicate Item and print it 

items = ["mango", "apple","apple", "orange", "banana"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Dulplicate Item:", item)
        break
    unique_item.add(item) 
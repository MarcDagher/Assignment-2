available_items = {
    12345:{"Name":"Potato", "Price":0.5}, 
    56789:{"Name":"Tomato", "Price":0.5}, 
    13579:{"Name":"Chips", "Price":1}, 
    20347:{"Name":"Soap", "Price":9}, 
    10393:{"Name":"Persil", "Price":3}, 
    47263:{"Name":"Bread", "Price":2}, 
    53928:{"Name":"Carrots", "Price":2.5}, 
    92638:{"Name":"Chocolate", "Price":1.3}, 
    70192:{"Name":"Garlic", "Price":9},
    44483:{"Name":"Toothpaste", "Price":6}
    }
def add_items(available_items):
    item_barcode = input("Insert item barcode: ")
    while item_barcode.isdigit() == False or int(item_barcode) not in available_items.keys(): # make sure item_barcode is valid
        if item_barcode.isdigit() == False:
            print()
            print("Please insert a number.")
            item_barcode = input("Insert item barcode: ")
        elif int(item_barcode) not in available_items.keys():
            print()
            print("Item not found. Choose another item.")
            item_barcode = input("Insert item barcode: ")
    item_quantity = input("Insert item quantity: ") 

    while item_quantity.isdigit() == False or int(item_quantity) <= 0 or int(item_quantity) > 49:
        if item_quantity.isdigit() == False:
            print()
            print("Please insert a number.")
            print()
            item_quantity = input("Insert item quantity: ")
        elif int(item_quantity) <= 0:
            print()
            print("Quantity can't be zero or below.")
            print()
            item_quantity = input("Insert item quantity: ")
            print()
        elif int(item_quantity) > 49:
            print()
            print("Quantity too high. Quantity must be below 50.")
            print()
            item_quantity = input("Insert item quantity: ")
            print()

    return [item_barcode, item_quantity] 

def add_extra_items(add_more, list_of_barcodes):

    while add_more == "Yes" or add_more == "yes":
        print()
        print("Choose from the avaiable items.")
        print()
        for i in available_items:
            print("Item Name:",i, "-- Price:", available_items[i]["Price"])
        print()
        barcode_quantity = add_items(available_items)
        list_of_barcodes.append(barcode_quantity) #storing the list of answers inside the list of barcodes
        print()
        add_more = input("Would you like to add more items? [Answer yes or no] ")
        print()
    
    if add_more == "No" or add_more == "no":
        return display_receipt(list_of_barcodes, available_items)
    
    elif add_more != "No" and add_more != "no" and add_more != "Yes" and add_more != "yes":
        print()
        print("Invalid entry, please choose yes or no!")
        add_more = input("Would you like to add more items? [Answer yes or no] ")
        print()
        return add_extra_items(add_more, list_of_barcodes)

def display_receipt(list_of_barcodes, available_items):
    #name - quantity - total
    print("Your basket contains:")
    print()
    total_items = 0
    total_price = 0 
    for i in list_of_barcodes:
        item_barcode = int(i[0])
        item_quantity = int(i[1])

        total_items += item_quantity
        total_price += item_quantity * available_items[item_barcode]["Price"]
        print(available_items[int(item_barcode)]["Name"], "Quantity: ", item_quantity, "Price: ", item_quantity * available_items[item_barcode]["Price"], "$")
    print()
    print("Total Items: ", total_items)
    print("Total Price: ", total_price, "$")
    print()

def Open_Receipt(available_items):
    list_of_barcodes = []
    new_receipt = input("Open New Receipt? [Answer yes or no] ")
    while new_receipt == "Yes" or new_receipt == "yes":
        print()
        print("Choose from the avaiable items.")
        print()
        for i in available_items:
            print("Item Name:",i, "-- Price:", available_items[i]["Price"]) #List of options
        print()
        barcode_quantity = add_items(available_items) #returns a list [barcode, quantity]
        list_of_barcodes.append(barcode_quantity) # store barcodes with quantities in the list
    
        add_more = input("Would you like to add more items? [Answer yes or no] ") # Ask add more?

        print(add_extra_items(add_more, list_of_barcodes)) ## Extra items function returns displayed receipt 
        new_receipt = input("Open New Receipt? [Answer yes or no] ")

    if new_receipt == "No" or new_receipt == "no":
        return "Have a nice day :)"
    else:
        print("Wrong Entry. Please type correctly.")
        return Open_Receipt(available_items)

print(Open_Receipt(available_items))
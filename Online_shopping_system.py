# Online Shopping Management System
print("Welcome to online shopping system")

print("Choose a category to shop from:")
print("1. Fashion")
print("2. Footwear")
print("3. Gadgets")
print("4. Exit")

choice = input("Enter number of the chosen category: ")

if choice == "1":
    print("1. Men")
    print("2. Women")
    print("3. Kids")

    c = input("Choose a category: ")

    if c == "1":
        print("Men's Collection")
        print("1. T-Shirt - Rs.800")
        print("2. Shirt - Rs.1200")
        print("3. Jeans - Rs.1800")

        item = input("Choose an item: ")

        if item == "1":
            product = "T-Shirt"
            price = 800
        elif item == "2":
            product = "Shirt"
            price = 1200
        elif item == "3":
            product = "Jeans"
            price = 1800
        else:
            print("Invalid Item")

    elif c == "2":
        print("Women's Collection")
        print("1. Kurti - Rs.1000")
        print("2. Saree - Rs.2500")
        print("3. Top - Rs.900")

        item = input("Choose an item: ")

        if item == "1":
            product = "Kurti"
            price = 1000
        elif item == "2":
            product = "Saree"
            price = 2500
        elif item == "3":
            product = "Top"
            price = 900
        else:
            print("Invalid Item")

    elif c == "3":
        print("Kids Collection")
        print("1. Frock - Rs.700")
        print("2. Kids T-Shirt - Rs.500")
        print("3. Shorts - Rs.600")

        item = input("Choose an item: ")

        if item == "1":
            product = "Frock"
            price = 700
        elif item == "2":
            product = "Kids T-Shirt"
            price = 500
        elif item == "3":
            product = "Shorts"
            price = 600
        else:
            print("Invalid Item")

    else:
        print("Invalid Fashion Category")

elif choice == "2":
    print("Footwear Collection")
    print("1. Sports Shoes - Rs.2500")
    print("2. Sandals - Rs.1200")
    print("3. Slippers - Rs.600")

    item = input("Choose an item: ")

    if item == "1":
        product = "Sports Shoes"
        price = 2500
    elif item == "2":
        product = "Sandals"
        price = 1200
    elif item == "3":
        product = "Slippers"
        price = 600
    else:
        print("Invalid Item")

elif choice == "3":
    print("Gadgets Collection")
    print("1. Mobile - Rs.20000")
    print("2. Laptop - Rs.55000")
    print("3. Smart Watch - Rs.4500")
    print("4. Earbuds - Rs.3000")

    item = input("Choose an item: ")

    if item == "1":
        product = "Mobile"
        price = 20000
    elif item == "2":
        product = "Laptop"
        price = 55000
    elif item == "3":
        product = "Smart Watch"
        price = 4500
    elif item == "4":
        product = "Earbuds"
        price = 3000
    else:
        print("Invalid Item")

elif choice == "4":
    print("Thank You for Visiting")

else:
    print("Invalid Choice")

if choice == "1" or choice == "2" or choice == "3":
    qty = int(input("Enter Quantity: "))
    total = price * qty
    print("BILL")
    print(f"Product  : {product}")
    print(f"Price    : Rs. {price}")
    print(f"Quantity : {qty}")
    print(f"Subtotal : Rs. {total}")

    if total >= 1000:
        print("Delivery : FREE")
    else:
        total = total + 150
        print("Delivery Charge : Rs.150")

    print(f"Final Amount : Rs. {total}")

    print("Payment Method")
    print("\n1.Cash \n2.Card \n3.UPI")
    payment = input("Payment Method (Cash/Card/UPI): ")

    if payment == "1":
        print("Cash Payment Selected")
    elif payment == "2":
        print("Card Payment Successful")
    elif payment == "3":
        print("UPI Payment Successful")
    else:
        print("Invalid Payment Method")

    print("Thank You for Shopping at OnShop!")
    print("Visit Again!")
print("FLIGHT TICKET RESERVATION SYSTEM")

print("1. Domestic Flights")
print("2. International Flights")
print("3. Exit")

choice = input("Enter your choice: ")
if choice == "1" or choice == "2":
    if choice == "1":
        flight_type = "Domestic"
        print("\nAvailable Flights")
        print("1. Bangalore -> Delhi")
        print("2. Bangalore -> Mumbai")
        print("3. Bangalore -> Mangalore")
        route = input("Choose your destination: ")
        if route == "1":
            flight = "Bangalore -> Delhi"
            print("\nTravel Class")
            print("1. Economy - Rs.6000")
            print("2. Business - Rs.10000")
            print("3. First Class - Rs.15000")
            cls = input("Choose Class: ")
            if cls == "1":
                travel_class = "Economy"
                fare = 6000
            elif cls == "2":
                travel_class = "Business"
                fare = 10000
            elif cls == "3":
                travel_class = "First Class"
                fare = 15000
            else:
                print("Invalid Choice")

        elif route == "2":
            flight = "Bangalore -> Mumbai"
            print("\nTravel Class")
            print("1. Economy - Rs.4500")
            print("2. Business - Rs.8000")
            print("3. First Class - Rs.12000")
            cls = input("Choose Class: ")
            if cls == "1":
                travel_class = "Economy"
                fare = 4500
            elif cls == "2":
                travel_class = "Business"
                fare = 8000
            elif cls == "3":
                travel_class = "First Class"
                fare = 12000
            else:
                print("Invalid Choice")

        elif route == "3":
            flight = "Bangalore -> Mangalore"
            print("\nTravel Class")
            print("1. Economy - Rs.2000")
            print("2. Business - Rs.4000")
            print("3. First Class - Rs.6000")
            cls = input("Choose Class: ")
            if cls == "1":
                travel_class = "Economy"
                fare = 2000
            elif cls == "2":
                travel_class = "Business"
                fare = 4000
            elif cls == "3":
                travel_class = "First Class"
                fare = 6000
            else:
                print("Invalid Choice")

        else:
            print("Invalid Flight")

    elif choice == "2":
        flight_type = "International"
        print("\nAvailable Flights")
        print("1. Bangalore -> Dubai")
        print("2. Bangalore -> Singapore")
        print("3. Bangalore -> New York")
        route = input("Choose your destination: ")
        if route == "1":
            flight = "Bangalore -> Dubai"
            print("\nTravel Class")
            print("1. Economy - Rs.20000")
            print("2. Business - Rs.35000")
            print("3. First Class - Rs.50000")

            cls = input("Choose Class: ")
            if cls == "1":
                travel_class = "Economy"
                fare = 20000
            elif cls == "2":
                travel_class = "Business"
                fare = 35000
            elif cls == "3":
                travel_class = "First Class"
                fare = 50000
            else:
                print("Invalid Choice")

        elif route == "2":
            flight = "Bangalore -> Singapore"
            print("\nTravel Class")
            print("1. Economy - Rs.25000")
            print("2. Business - Rs.45000")
            print("3. First Class - Rs.65000")

            cls = input("Choose Class: ")
            if cls == "1":
                travel_class = "Economy"
                fare = 25000
            elif cls == "2":
                travel_class = "Business"
                fare = 45000
            elif cls == "3":
                travel_class = "First Class"
                fare = 65000
            else:
                print("Invalid Choice")
            
        elif route == "3":
            flight = "Bangalore -> New York"
            print("\nTravel Class")
            print("1. Economy - Rs.70000")
            print("2. Business - Rs.120000")
            print("3. First Class - Rs.180000")

            cls = input("Choose Class: ")
            if cls == "1":
                travel_class = "Economy"
                fare = 70000
            elif cls == "2":
                travel_class = "Business"
                fare = 120000
            elif cls == "3":
                travel_class = "First Class"
                fare = 180000
            else:
                print("Invalid Choice")

        else:
            print("Invalid Flight")

    print("Enter Passenger Details")
    name = input("Passenger Name: ")
    age = input("Age: ")
    gender = input("Gender: ")

    if flight_type == "Domestic":
        aadhaar = input("Enter Aadhaar Number: ")

    elif flight_type == "International":
        passport = input("Enter Passport Number: ")
        visa = input("Visa Available (Yes/No): ")

        if visa == "Yes" or visa == "yes":
            print("Visa Verified")
        else:
            print("Booking Cancelled! Visa is Required.")
    
    print("\nSeat Preference")
    print("1. Window")
    print("2. Middle")
    print("3. Aisle")

    seat = input("Choose Seat: ")
    if seat == "1":
        seat_type = "Window"
    elif seat == "2":
        seat_type = "Middle"
    elif seat == "3":
        seat_type = "Aisle"
    else:
        print("Invalid Seat")
        
    print("\nPayment Method")
    print("1. UPI")
    print("2. Card")
    print("3. Cash")

    pay = input("Choose Payment Method: ")

    if pay == "1":
        payment = "UPI"
    elif pay == "2":
        payment = "Card"
    elif pay == "3":
        payment = "Cash"
    else:
        print("Invalid Payment Method")

    print("FLIGHT TICKET")

    print("Passenger Name :", name)
    print("Age            :", age)
    print("Gender         :", gender)
    print("Flight Type    :", flight_type)
    print("Destination    :", flight)
    print("Travel Class   :", travel_class)
    print("Seat           :", seat_type)
    print("Ticket Fare    : Rs.", fare)
    print("Payment Method :", payment)
    print("Booking Status : CONFIRMED")

    print("Thank You for Booking with Us!")
    print("Have a Safe Journey!")

elif choice == "3":
    print("Thank You for Visiting!")

else:
    print("Invalid Choice")


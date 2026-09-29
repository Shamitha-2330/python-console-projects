# Python Console Projects

A collection of beginner-level Python programs built while learning core Python (conditionals, input/output, string formatting and program flow). Each program is menu-driven and runs entirely in the terminal.

## Projects

| Project | Description | File |
|---|---|---|
| Flight Ticket Reservation System | Book domestic or international flights, choose travel class and seat, enter passenger details, pay, and get a ticket | [`flight-reservation/flight_reservation.py`](flight-reservation/flight_reservation.py) |
| Online Shopping Management System | Browse Fashion, Footwear and Gadgets, pick a product and quantity, get a bill with delivery charges, and choose a payment method | [`online-shopping/online_shopping.py`](online-shopping/online_shopping.py) |

## 1. Flight Ticket Reservation System

**Features**
- Domestic and international routes from Bangalore (Delhi, Mumbai, Mangalore, Dubai, Singapore, New York)
- Three travel classes per route (Economy, Business, First Class) with route-specific fares
- Passenger details, with Aadhaar for domestic and passport plus visa check for international bookings
- Seat preference (Window, Middle, Aisle)
- Payment via UPI, Card or Cash
- Formatted ticket printed at the end

## 2. Online Shopping Management System

**Features**
- Category menu: Fashion (Men, Women, Kids), Footwear, Gadgets
- Product selection with prices
- Quantity input and subtotal calculation
- Free delivery on orders of Rs.1000 or more, Rs.150 delivery charge otherwise
- Itemised bill and payment method selection (Cash, Card, UPI)

## Concepts Practised

- `if / elif / else` and nested conditionals
- User input with `input()`
- Type conversion and arithmetic
- f-strings and formatted output
- Menu-driven program design

## How to Run

Requires Python 3.8 or later.

```bash
git clone https://github.com/Shamitha-2330/python-console-projects.git
cd python-console-projects

python flight-reservation/flight_reservation.py
python online-shopping/online_shopping.py
```

On some systems the command is `python3` instead of `python`.

## Author

**Shamitha**

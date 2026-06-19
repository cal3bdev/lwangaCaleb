"""
E-commerce Price Calculator
Assignment 2

A small e-commerce checkout that authenticates a user, then takes a
subtotal, a coupon code, and a location, and prints a receipt with the
coupon discount, location-based tax, and grand total.

Uses nested conditions (match/case) to handle valid/invalid coupon codes
and different tax rates per location.
"""


def check_location(location):
    """Return the tax rate for a supported country, or 0 if unsupported."""
    match location:
        case "Uganda":
            return 0.18
        case "Kenya":
            return 0.16
        case "Tanzania":
            return 0.18
        case "Rwanda":
            return 0.18
        case _:
            print("Country not supported. No location tax applied.")
            return 0.0


def check_coupon_code(coupon_code):
    """Return the discount rate for a valid coupon, or 0 if invalid."""
    match coupon_code:
        case "CU435x":
            return 0.1
        case "Yu234C":
            return 0.4
        case "TY3345x":
            return 0.7
        case _:
            print("Invalid coupon code. No coupon discount applied.")
            return 0.0


def compute_grand_total(subtotal, location, coupon_code):
    """Calculate and print a receipt from subtotal, coupon, and location."""
    coupon_discount = check_coupon_code(coupon_code) * subtotal
    discounted_subtotal = subtotal - coupon_discount

    tax_rate = check_location(location)
    tax_amount = discounted_subtotal * tax_rate

    grand_total = discounted_subtotal + tax_amount

    receipt = f"""
==================================================
Subtotal:        {subtotal:>12.2f}/=
Coupon Discount: {coupon_discount:>12.2f}/=
Tax:             {tax_amount:>12.2f}/=
--------------------------------------------------
GRAND TOTAL:     {grand_total:>12.2f}/=
==================================================
"""
    print(receipt)


def login_system():
    """Authenticate the user, then run one checkout on success."""
    print("Welcome to the E-commerce price calculator. Authenticate to continue.")

    users = {
        "Cashier": "password",
    }

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Correct username AND matching password -> log in and check out.
        if username in users and users[username] == password:
            print(f"\nWelcome, {username}\n")

            subtotal = float(input("Enter subtotal: "))
            coupon_code = input("Enter coupon code: ")
            location = input("Enter your country: ").capitalize()
            compute_grand_total(subtotal, location, coupon_code)
            return

        # Otherwise it is a failed attempt.
        attempts += 1
        print(f"Invalid username or password. Attempt {attempts} of {max_attempts}.\n")

    print("Maximum login attempts reached. Access denied.")


login_system()

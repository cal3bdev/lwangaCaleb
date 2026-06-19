"""
Bill Split Calculator
Assignment 1

Asks for a total bill, number of people, and tip percentage, then
calculates the tip, grand total, and each person's share, and prints
a formatted receipt. After each run you can rerun or exit.
"""


def get_positive_float(prompt):
    """Keep asking until the user enters a number greater than 0."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("  Please enter a valid number (e.g. 54.20).")
            continue
        if value <= 0:
            print("  Please enter an amount greater than 0.")
            continue
        return value


def get_positive_int(prompt):
    """Keep asking until the user enters a whole number greater than 0."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number (e.g. 4).")
            continue
        if value <= 0:
            print("  Please enter a number of people greater than 0.")
            continue
        return value


def get_tip_percentage():
    """Let the user choose a preset tip or enter a custom one."""
    print("\nChoose a tip percentage:")
    print("  1) 10%")
    print("  2) 15%")
    print("  3) 20%")
    print("  4) Custom")

    options = {"1": 10.0, "2": 15.0, "3": 20.0}

    while True:
        choice = input("Enter 1, 2, 3, or 4: ").strip()

        if choice in options:
            return options[choice]

        if choice == "4":
            while True:
                try:
                    custom = float(input("Enter your custom tip percentage: "))
                except ValueError:
                    print("  Please enter a valid number (e.g. 18).")
                    continue
                if custom < 0:
                    print("  Tip percentage cannot be negative.")
                    continue
                return custom

        print("  Invalid choice. Please enter 1, 2, 3, or 4.")


def run_calculator():
    """Run one full bill split calculation."""
    print("=" * 40)
    print("       BILL SPLIT CALCULATOR")
    print("=" * 40)

    # 1. Get inputs (all validated)
    bill = get_positive_float("\nEnter the total bill amount: $")
    people = get_positive_int("Enter the number of people: ")
    tip_percent = get_tip_percentage()

    # 2. Calculations
    tip_amount = bill * (tip_percent / 100)
    grand_total = bill + tip_amount
    per_person = grand_total / people

    # 3. Formatted receipt (f-strings)
    print("\n" + "=" * 40)
    print("               RECEIPT")
    print("=" * 40)
    print(f"Bill amount:        ${bill:>10.2f}")
    print(f"Tip ({tip_percent:.0f}%):           ${tip_amount:>10.2f}")
    print("-" * 40)
    print(f"Total (bill + tip): ${grand_total:>10.2f}")
    print(f"Number of people:   {people:>11}")
    print("-" * 40)
    print(f"Each person pays:   ${per_person:>10.2f}")
    print("=" * 40)


def main():
    while True:
        run_calculator()
        again = input("\nRun again? (y to rerun, anything else to exit): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()

"""
Contact Manager
Assignment 5

A menu-driven contact book. Each contact is stored as a tuple
(name, phone, email) inside a list. Supports add, view, update, delete,
search (by name, phone, or email), and listing all contacts. Phone and
email are validated before a contact is saved.
"""

# Each contact is a tuple: (name, phone, email)
contacts = []


def validate_phone(phone):
    """A phone is valid if it is non-empty and only digits, '-', or '+'."""
    if not phone:
        return False
    for char in phone:
        if not (char.isdigit() or char == "-" or char == "+"):
            return False
    return True


def validate_email(email):
    """A simple email check: must contain both '@' and '.'."""
    if not email:
        return False
    return "@" in email and "." in email


def format_contact_display(contact):
    """Return a single, aligned line describing one contact."""
    name, phone, email = contact
    return f"  Name: {name:20} | Phone: {phone:15} | Email: {email}"


def add_contact(name, phone, email):
    """Add a contact after checking for duplicates and validating fields."""
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"\nError: Contact '{name}' already exists.")
            return

    if not validate_phone(phone):
        print(f"\nError: Invalid phone number '{phone}'.")
        print("   Phone must contain only digits, hyphens, and plus signs (e.g. '+256-701').")
        return

    if not validate_email(email):
        print(f"\nError: Invalid email '{email}'.")
        print("   Email must contain '@' and '.' (e.g. 'user@example.com').")
        return

    contacts.append((name, phone, email))
    print(f"\nContact '{name}' added successfully.")


def view_contact(name):
    """Print one contact matched by name, or a not-found message."""
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("\n--- Contact Found ---")
            print(format_contact_display(contact))
            return
    print(f"\nContact '{name}' not found.")


def update_contact(name, phone, email):
    """Replace a contact's phone and email after validating the new values."""
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name.lower():
            if not validate_phone(phone):
                print(f"\nError: Invalid phone number '{phone}'.")
                print("   Phone must contain only digits, hyphens, and plus signs.")
                return

            if not validate_email(email):
                print(f"\nError: Invalid email '{email}'.")
                print("   Email must contain '@' and '.'.")
                return

            contacts[i] = (name, phone, email)
            print(f"\nContact '{name}' updated successfully.")
            return

    print(f"\nContact '{name}' not found.")


def delete_contact(name):
    """Remove a contact matched by name."""
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name.lower():
            contacts.pop(i)
            print(f"\nContact '{name}' deleted successfully.")
            return
    print(f"\nContact '{name}' not found.")


def list_all_contacts():
    """Print every saved contact, or a message if there are none."""
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n" + "=" * 70)
    print("ALL CONTACTS")
    print("=" * 70)
    for contact in contacts:
        print(format_contact_display(contact))
    print("=" * 70)
    print(f"Total: {len(contacts)} contact(s)\n")


def search_contacts(query, search_by="name"):
    """Return contacts whose chosen field contains the query (case-insensitive)."""
    query = query.lower()

    if search_by == "name":
        return [c for c in contacts if query in c[0].lower()]
    if search_by == "phone":
        return [c for c in contacts if query in c[1].lower()]
    if search_by == "email":
        return [c for c in contacts if query in c[2].lower()]
    return []


def display_search_results(results, query, search_by="name"):
    """Print search results, or a not-found message if the list is empty."""
    if not results:
        print(f"\nNo contacts found matching '{query}' in {search_by}.")
        return

    print("\n" + "=" * 70)
    print(f"SEARCH RESULTS ({len(results)} found)")
    print(f"Searching by: {search_by.upper()} for '{query}'")
    print("=" * 70)
    for contact in results:
        print(format_contact_display(contact))
    print("=" * 70 + "\n")


def get_valid_input(prompt, input_type="string"):
    """Keep asking until the user gives non-empty input of the right type."""
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        if input_type == "int":
            try:
                return int(user_input)
            except ValueError:
                print("Please enter a valid number.")
                continue

        return user_input


def main():
    print("\n" + "=" * 50)
    print("Welcome to Contact Manager!")
    print("=" * 50)

    while True:
        print("\n" + "=" * 50)
        print("=== CONTACT MANAGER MENU ===")
        print("=" * 50)
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        print("=" * 50)

        choice = get_valid_input("Choose an option (1-7): ", input_type="int")

        if choice == 1:
            print("\n--- Add New Contact ---")
            name = get_valid_input("Enter name: ")
            phone = get_valid_input("Enter phone (digits, hyphens, +): ")
            email = get_valid_input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == 2:
            print("\n--- View Contact ---")
            name = get_valid_input("Enter name to view: ")
            view_contact(name)

        elif choice == 3:
            print("\n--- Update Contact ---")
            name = get_valid_input("Enter name to update: ")
            phone = get_valid_input("Enter new phone (digits, hyphens, +): ")
            email = get_valid_input("Enter new email: ")
            update_contact(name, phone, email)

        elif choice == 4:
            print("\n--- Delete Contact ---")
            name = get_valid_input("Enter name to delete: ")
            delete_contact(name)

        elif choice == 5:
            print("\n--- Search Contacts ---")
            print("Search by: (1) Name, (2) Phone, (3) Email")
            search_choice = get_valid_input("Select search type (1-3): ", input_type="int")

            if search_choice == 1:
                query = get_valid_input("Enter name to search: ")
                display_search_results(search_contacts(query, "name"), query, "name")
            elif search_choice == 2:
                query = get_valid_input("Enter phone to search: ")
                display_search_results(search_contacts(query, "phone"), query, "phone")
            elif search_choice == 3:
                query = get_valid_input("Enter email to search: ")
                display_search_results(search_contacts(query, "email"), query, "email")
            else:
                print("Invalid search type. Please choose 1, 2, or 3.")

        elif choice == 6:
            list_all_contacts()

        elif choice == 7:
            print("\n" + "=" * 50)
            print("Thank you for using Contact Manager!")
            print("=" * 50 + "\n")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    main()

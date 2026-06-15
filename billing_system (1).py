"""
SmartBuy Supermarket Billing System
------------------------------------
A simple Python program that allows a cashier to:
- Enter multiple products purchased by a customer
- Calculate total price for each product and the overall bill
- Apply a 10% discount if the total exceeds Le 500
- Display a well-formatted receipt
- Process multiple customers continuously until the cashier exits
"""

DISCOUNT_THRESHOLD = 500   # Discount applies if total exceeds this amount
DISCOUNT_RATE = 0.10       # 10% discount


def get_products():
    """
    Collect product details (name, quantity, price) from the cashier
    and store them in a list. Returns the list of products.
    """
    products = []  # List (array) to store all products for this customer

    while True:
        print("\n--- Enter Product Details ---")
        name = input("Enter product name: ")

        # Validate quantity input
        while True:
            try:
                quantity = int(input("Enter quantity purchased: "))
                if quantity <= 0:
                    print("Quantity must be a positive number. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")

        # Validate price input
        while True:
            try:
                price = float(input("Enter price per unit (Le): "))
                if price <= 0:
                    print("Price must be a positive number. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for price.")

        # Calculate total price for this product
        total_price = quantity * price

        # Store product details as a dictionary inside the list
        products.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": total_price
        })

        # Ask if cashier wants to add another product
        more = input("Add another product? (y/n): ").strip().lower()
        if more != 'y':
            break

    return products


def calculate_bill(products):
    """
    Calculate the subtotal, discount (if any), and final amount.
    Returns a tuple: (subtotal, discount_amount, final_amount)
    """
    subtotal = 0

    # Add up the total price of each product to get the subtotal
    for product in products:
        subtotal += product["total"]

    # Apply discount if subtotal exceeds the threshold
    if subtotal > DISCOUNT_THRESHOLD:
        discount_amount = subtotal * DISCOUNT_RATE
    else:
        discount_amount = 0

    final_amount = subtotal - discount_amount

    return subtotal, discount_amount, final_amount


def print_receipt(products, subtotal, discount_amount, final_amount):
    """python billing_system
    Display a well-formatted receipt for the customer.
    """
    print("\n" + "=" * 40)
    print("        SMARTBUY SUPERMARKET")
    print("              RECEIPT")
    print("=" * 40)
    print(f"{'Product':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
    print("-" * 40)

    for product in products:
        print(f"{product['name']:<15}{product['quantity']:<5}"
              f"{product['price']:<10.2f}{product['total']:<10.2f}")

    print("-" * 40)
    print(f"{'Subtotal:':<30}Le {subtotal:.2f}")

    if discount_amount > 0:
        print(f"{'Discount (10%):':<30}Le {discount_amount:.2f}")
    else:
        print(f"{'Discount:':<30}None")

    print(f"{'Total to Pay:':<30}Le {final_amount:.2f}")
    print("=" * 40)
    print("     THANK YOU FOR SHOPPING WITH US!")
    print("=" * 40 + "\n")


def main():
    """
    Main program loop. Allows the cashier to process multiple
    customers continuously until they choose to exit.
    """
    print("Welcome to the SmartBuy Supermarket Billing System")

    while True:
        print("\n############################")
        print("     NEW CUSTOMER")
        print("############################")

        # Step 1: Get list of products for this customer
        products = get_products()

        # Step 2: Calculate the bill
        subtotal, discount_amount, final_amount = calculate_bill(products)

        # Step 3: Display the receipt
        print_receipt(products, subtotal, discount_amount, final_amount)

        # Step 4: Ask if cashier wants to serve another customer
        choice = input("Process another customer? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nThank you for using SmartBuy Billing System. Goodbye!")
            break


# Run the program
if __name__ == "__main__":
    main()

# Supermarket billing system
Project Description
The Supermarket Billing System is a Python-based command-line application 
developed for SmartBuy Supermarket to automate the billing process. It 
replaces the manual, error-prone process of calculating customer bills 
using calculators and handwritten receipts. The system allows cashiers to 
enter product details, automatically calculates totals, applies discounts 
where applicable, and generates a clear, well-formatted receipt for each 
customer.

## How the Program Works
1. The cashier enters the details of each product purchased by a customer:
   - Product name
   - Quantity purchased
   - Price per unit
2. The program calculates the total price for each product (quantity × price).
3. All products are stored in a list, and the program calculates the overall 
   subtotal by summing the totals of all products.
4. If the subtotal exceeds Le 500, a 10% discount is automatically applied.
5. The program displays a formatted receipt showing:
   - List of products with quantity and price
   - Subtotal
   - Discount applied (if any)
   - Final amount to be paid
6. After completing one customer's bill, the cashier is asked whether they 
   want to process another customer. The program continues looping until 
   the cashier chooses to stop.

## How to Run the Program
1. Ensure Python 3 is installed on your computer (download from python.org 
   if needed).
2. Download or clone this repository.
3. Open the project folder in VS Code (or any code editor/terminal).
4. Open a terminal in the project folder.
5. Run the program using the command:
   ```
   python billing_system.py
   ```
   (use `python3` on Mac/Linux if required)
6. Follow the on-screen prompts to enter product details and generate 
   receipts.

## Author
[Mohamed Jalloh]
IPG101 – Introduction to Programming
Limkokwing University of Creative Technology, Sierra Leone


def fetch_sales():
    return [
        {"item": "Masala Chai", "price": 30, "quantity": 10, "valid": True},
        {"item": "Ginger Chai", "price": 35, "quantity": 5, "valid": False},
        {"item": "Elaichi Chai", "price": 40, "quantity": 7, "valid": True},
        {"item": "Green Tea", "price": 50, "quantity": 3, "valid": True},
    ]
# Simulates fetching raw sales data from a database or API.


def filter_valid_orders(sales):
    return [order for order in sales if order["valid"]]
#Filters out invalid orders.

def summarize_data(valid_sales):
    total_revenue = 0
    for order in valid_sales:
        total_revenue += order["price"] * order["quantity"]
    return total_revenue
# Summarizes total revenue from valid sales.


def generate_report():
    sales = fetch_sales()
    valid_sales = filter_valid_orders(sales)
    revenue = summarize_data(valid_sales)
    # Generate and print the monthly sales report

    print("Monthly Sales Report")
    print("----------------------")
    print(f"Total Orders: {len(valid_sales)}")
    print(f"Total Revenue: ₹{revenue}")

generate_report()
# Main function to generate the monthly sales report.

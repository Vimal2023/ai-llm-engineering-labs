def add_vat(price, vat_rate):
    vat_amount = price * vat_rate
    final_price = price + vat_amount
    return final_price
# Adds VAT to the given price.

VAT_RATE = 0.10
# Example usage

order_1 = add_vat(100, VAT_RATE)
# Calculating final price for an order of ₹100 with 10% VAT.

print("Final Prices (Including VAT)")
print(f"Order 1: ₹{order_1}")
# Print the final price for the first order.

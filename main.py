# Task 1

class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount


    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate

    def display_order(self):
        print(f"ID: {self.order_id} | Name: {self.customer_name} | Total: Rp{self.total_amount}")

# Task 2
class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        total = 0
        for index in self.orders:
            total = total + index.total_amount
        return total
            
    def calculate_total_tax(self, tax_rate):
        total_tax = 0
        for index in self.orders:
            total_tax = total_tax + index.calculate_tax(tax_rate)
        return total_tax
            
# Task 3
invoice1 = Order ("001", "Budi", "2024-01-01", 100000)
invoice2 = Order ("002", "Andi", "2024-04-01", 100000)
invoice3 = Order ("003", "Wawan", "2024-01-03", 100000)

processor = OrderProcessor()

processor.add_order(invoice1)

processor.add_order(invoice2)

processor.add_order(invoice3)

invoice1.display_order()

invoice2.display_order()

invoice3.display_order()

print(f"Total Revenue: Rp{processor.calculate_total_revenue()}")

print(f"Total Tax: Rp{processor.calculate_total_tax(0.1)}")
    
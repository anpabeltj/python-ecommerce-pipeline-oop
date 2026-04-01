# python-ecommerce-pipeline-oop

A simple Order Management System built with Python using Object-Oriented Programming (OOP) principles.

## Features

- Create and manage customer orders
- Display order details
- Calculate total revenue from all orders
- Calculate total tax automatically

## OOP Concepts Used

### Encapsulation

This project uses **Encapsulation** by wrapping data and methods inside a class, keeping the data protected and organized.

- `Order` class stores order data (`order_id`, `customer_name`, `order_date`, `total_amount`) and provides methods to calculate tax and display order details.
- `OrderProcessor` class manages a list of orders and provides methods to calculate total revenue and total tax.

## How to Run

```bash
python main.py
```

## Testing

Manual test was performed by inputting 3 order data with a total price of Rp 300,000. The program successfully calculated a 10% tax of **Rp 30,000** automatically.

### Expected Output

```
ID: 001 | Name: Budi | Total: Rp100000
ID: 002 | Name: Andi | Total: Rp100000
ID: 003 | Name: Wawan | Total: Rp100000
Total Revenue: Rp300000
Total Tax: Rp30000.0
```

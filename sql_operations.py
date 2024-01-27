import psycopg2
from datetime import datetime, timedelta

# Database connection parameters
db_params = {
    'database': 'postgres',
    'user': 'postgres',
    'password': 'xxxx',
    'host': 'xxxxp-southeast-2.rds.amazonaws.com',  # or your database host
    'port': '5432'  # default PostgreSQL port
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Function to insert data into the Customers table
def insert_customers():
    for i in range(1, 6):  # Insert 5 sample customers
        cursor.execute(
            "INSERT INTO Customers (Name, Email, Country) VALUES (%s, %s, %s)",
            (f'Customer{i}', f'customer{i}@example.com', f'Country{i}')
        )

# Function to insert data into the Products table
def insert_products():
    for i in range(1, 4):  # Insert 3 sample products
        cursor.execute(
            "INSERT INTO Products (Name, Price) VALUES (%s, %s)",
            (f'Product{i}', i * 100.00)  # Sample price
        )

# Function to insert data into the Orders table, linking to Customers
def insert_orders():
    for i in range(1, 11):  # Insert 10 sample orders
        order_date = datetime.now() - timedelta(days=i)
        cursor.execute(
            "INSERT INTO Orders (OrderDate, CustomerID, TotalAmount) VALUES (%s, %s, %s)",
            (order_date, i % 5 + 1, i * 200.00)  # Sample total amount
        )

# Function to insert data into the OrderDetails table, linking to Orders and Products
def insert_order_details():
    for i in range(1, 16):  # Insert 15 sample order details
        cursor.execute(
            "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)",
            (i % 10 + 1, i % 3 + 1, i % 4 + 1)  # Sample quantity
        )

# Insert data into all tables
insert_customers()
insert_products()
insert_orders()
insert_order_details()

# Commit the transactions and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted into all tables successfully.")
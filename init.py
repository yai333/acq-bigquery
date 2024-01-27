import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Database connection parameters
db_params = {
    'database': 'postgres',
    'user': 'postgres',
    'password': 'xxxx',
    'host': 'xxxx.rds.amazonaws.com',  # or your database host
    'port': '5432'  # default PostgreSQL port
}

# Connect to PostgreSQL server
conn = psycopg2.connect(**db_params)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor to perform database operations
cursor = conn.cursor()

# SQL commands to create tables (if they don't exist)
create_table_commands = [
    '''
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID SERIAL PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255),
        Country VARCHAR(255)
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID SERIAL PRIMARY KEY,
        OrderDate DATE NOT NULL,
        CustomerID INT,
        TotalAmount DECIMAL(10, 2),
        FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS Products (
        ProductID SERIAL PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Price DECIMAL(10, 2)
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS OrderDetails (
        OrderDetailID SERIAL PRIMARY KEY,
        OrderID INT,
        ProductID INT,
        Quantity INT,
        FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
    )
    '''
]

# Execute the SQL commands to create tables
for command in create_table_commands:
    cursor.execute(command)

# Insert auto-generated data into tables
# Example for inserting into Customers table
for i in range(1, 6):  # Assuming 5 customers
    cursor.execute(
        "INSERT INTO Customers (Name, Email, Country) VALUES (%s, %s, %s)",
        (f'Customer{i}', f'customer{i}@example.com', f'Country{i%3+1}')
    )

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Tables created and data inserted successfully.")
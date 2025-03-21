import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')  # Create or connect to the database
    cursor = conn.cursor()
    
    # Create the Products table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert sample data (only if the table is empty)
    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO Products (id, name, category, price)
            VALUES (?, ?, ?, ?)
        ''', [
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Smartphone', 'Electronics', 999.99)
        ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()

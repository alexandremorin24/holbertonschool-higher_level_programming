from flask import Flask, render_template, request, json
import sqlite3
import csv

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv():
    try:
        products = []
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except (FileNotFoundError, csv.Error):
        return []

def read_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id", type=int)

    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    elif source == "sql":
        products = read_sql()
    else:
        return render_template("product_display.html", error="Wrong source. Use ?source=json, ?source=csv, or ?source=sql")

    if product_id:
        filtered_products = [p for p in products if p["id"] == product_id]
        if not filtered_products:
            return render_template("product_display.html", error="Product not found")
        products = filtered_products

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

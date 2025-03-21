from flask import Flask, render_template, request, json
import csv

app = Flask(__name__)

# Function to read JSON data
def read_json():
    try:
        with open("products.json", "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to read CSV data
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/items')
def items():
    try:
        # Read data from JSON file
        with open("items.json", "r") as file:
            data = json.load(file)
            item_list = data.get("items", [])  # Get items or an empty list if missing

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}")
        item_list = []

    # Pass the list of items to the template
    return render_template('items.html', items=item_list)

# Route to display products
@app.route('/products')
def products():
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id", type=int)

    # Determine data source
    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    else:
        return render_template("product_display.html", error="Wrong source. Use ?source=json or ?source=csv")

    # If an ID is provided, filter the data
    if product_id:
        filtered_products = [p for p in products if p["id"] == product_id]
        if not filtered_products:
            return render_template("product_display.html", error="Product not found")
        products = filtered_products

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

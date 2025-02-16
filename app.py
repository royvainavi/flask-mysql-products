from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "csci3124-rds.cwl7xlflmwj2.us-east-1.rds.amazonaws.com",
    "user": "admin",
    "password": "NewSecurePassword123",
    "database": "product_db"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/store-products', methods=['POST'])
def store_products():
    try:
        data = request.json['products']
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Clear existing entries to avoid duplicates
        cursor.execute("DELETE FROM products")
        
        for product in data:
            cursor.execute(
                "INSERT INTO products (name, price, availability) VALUES (%s, %s, %s)",
                (product['name'], product['price'], product['availability'])
            )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Success."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list-products', methods=['GET'])
def list_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT name, price, availability FROM products")
        products = cursor.fetchall()
        
        # Convert TINYINT(1) to boolean
        for product in products:
            product['availability'] = bool(product['availability'])
        
        cursor.close()
        conn.close()
        return jsonify({"products": products}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

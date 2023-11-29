import requests

def insert_order(data):
    url = "https://api.example.com/orders"  # Replace with the actual API endpoint

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        order_id = response.json()["order_id"]
        print(f"New order with ID {order_id} has been successfully inserted!")
    except requests.exceptions.RequestException as e:
        print("Error inserting order:", e)

# Example usage
new_order_data = {
    "product": "Apple",
    "quantity": 10,
    "price": 1.99
}

insert_order(new_order_data)

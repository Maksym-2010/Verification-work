from models import User, Product
from fastapi import HTTPException
from typing import Optional


userslist: list[dict] = []



allowed_users = [
    {"name": "Maksym", "password": "SecretPASSWORD"},
    {"name": "John", "password": "JohN_12"},
]



products = [
    Product(id=1, name="Laptop", price=1200.50, in_stock=True),
    Product(id=2, name="Smartphone", price=699.99, in_stock=True),
    Product(id=3, name="Headphones", price=199.99, in_stock=False),
]

# Перше завдання(the first task):
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    return users




# Друге завдання(the second task):
def user_to_create(name: str, age: int, email: str):
    new_user = {
        "name": name,
        "age":  age,
        "email": email
    }
    userslist.append(new_user)
    return userslist
    
    

# Третє завдання(the third task):
def verify_user(name: Optional[str], password: Optional[str]) -> bool:
    if name and password:
        return any(user for user in allowed_users if user["name"] == name and user["password"] == password)
    return False



# Четверте завдання(the fourth task):
def get_product_with_id(product_id: int) -> Product:
    product = next((prod for prod in products if prod.id == product_id), None)
    return product
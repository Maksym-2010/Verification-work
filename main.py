from fastapi import FastAPI, HTTPException, Header
from utils import get_users, user_to_create,  get_product_with_id, verify_user
from models import User, Product
from fastapi.responses import JSONResponse



app = FastAPI()



# Перше завдання(the first task):
@app.get("/users/")
async def find_users():
    return get_users()



# Друге завдання(the second task):
@app.post("/users/")
async def create_user(user_data: User):
    return user_to_create(name=user_data.name, age=user_data.age, email=user_data.email)



# Третє завдання(the third task):
@app.get("/admin")
async def admin_route(name: str = Header(None), password: str = Header(None)):
    if verify_user(name, password):
        return JSONResponse(content={"message": "Welcome! You have access to admin functions "})
    else:
        raise HTTPException(status_code=403, detail="Invalid name or password.")



# Четверте завдання(the fourth task):
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = get_product_with_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
from pydantic import BaseModel, EmailStr, validator




class User(BaseModel):
    name: str
    age: int
    email: EmailStr
   
    @validator("name")
    def name_must_be_longer_than_3(cls, value):
        if len(value) <= 3:
            raise ValueError("Вказана довжина імені має бути більше ніж 3")
        return value
    
    @validator("age")
    def age_must_be_bigger_than_18(cls, value):
        if value <= 18:
            raise ValueError("Вам не достатньо років. Для продовження вік має бути більше 18-ти років!")
        return value




class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool
from pydantic import BaseModel
class User(BaseModel):
    email: str
    password: str

class Product(BaseModel):
    product_name: str
    product_ID: int
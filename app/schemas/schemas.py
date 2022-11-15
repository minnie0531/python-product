from pydantic import BaseModel

class ProductBase(BaseModel):
    product_id: int
    product_name: str
    product_price: str
    product_quantity: int
    
    class Config:
        orm_mode = True
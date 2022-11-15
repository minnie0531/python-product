from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas import schemas


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductBase):
    db_product = Product(product_id=product.product_id,
    product_name=product.product_name,
    product_price=product.product_price,
    product_quantity=product.product_quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

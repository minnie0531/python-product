from sqlalchemy.orm import Session

from app.models import product
from app.schemas import schemas


def get_product(db: Session, product_id: int):
    return db.query(product.Product).filter(product.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(product.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductBase):
    db_product = product.Product(product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

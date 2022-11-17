from fastapi import APIRouter, Depends
from app.repository import product_curd
from app.schemas import schemas
from app.repository.sql_session import SessionLocal, engine, Base
from sqlalchemy.orm import Session

"""
This Module is for query endpoints.
Client can access this application through GET/POST/PUT/DELETE /queries
"""

router = APIRouter()
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products", tags=["products"], description="product")
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return product_curd.get_products(db,skip=skip, limit=limit)

@router.post("/products", tags=["products"], description="product")
def create_user(product_schema: schemas.ProductBase, db: Session = Depends(get_db)):
    return product_curd.create_product(db=db, product=product_schema)
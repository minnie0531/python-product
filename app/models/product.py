from sqlalchemy import Column, Integer, String

from app.repository.sql_session import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    product_price = Column(String)
    product_quantity= Column(Integer)

  
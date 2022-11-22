from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

username = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PW']

engine = create_engine("mysql+pymysql://${username}:${password}@product-mysql/product")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

username = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PW']

connectionString = 'mysql+pymysql://' + username + ":" + password + "@product-mysql:3306/product"

engine = create_engine(connectionString)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

# Define your models here (assuming they are in models.py)
from models import Workday_Company_Data, Greenhouse_Company_Data, Jobs

def get_database_engine():
    # Fetch DB credentials from environment variables
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    # Create the database engine
    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
    return engine

def create_database(engine):
    # Create tables only if they don't exist
    Base.metadata.create_all(engine)
    print("Tables created successfully (if they didn't exist).")

def main():
    engine = get_database_engine()
    
    # Create tables only if they don't exist
    create_database(engine)
    
    # Use session to interact with DB
    Session = sessionmaker(bind=engine)
    session = Session()

if __name__ == "__main__":
    main()

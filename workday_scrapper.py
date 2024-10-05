# Importing the necessary Libraries
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from sqlalchemy.orm import sessionmaker
from db_setup import get_database_engine
from dotenv import load_dotenv
import os
import time

# Import your models
from models import Workday_Company_Data  

# Load environment variables
load_dotenv()

# Establish a connection to your PostgreSQL database
engine = get_database_engine()
Session = sessionmaker(bind=engine)
session = Session()

# Fetching the company_info data from the database
company_data = session.query(Workday_Company_Data).all()

# Converting the fetched data into a DataFrame
company_df = pd.DataFrame([(c.Company_ID, c.Company_Name, c.Company_URL) for c in company_data],
                          columns=['company_id', 'company_name', 'company_url'])


job_data = []

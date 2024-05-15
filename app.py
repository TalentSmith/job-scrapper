import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime, timedelta
import mysql.connector

import time
time.sleep(5)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port = 3306,
    user='root',
    password='nitsnidhi123',
    database='scrapper'
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the URL of the Workday career page
url = 'https://pru.wd5.myworkdayjobs.com/en-US/Careers/'

driver = webdriver.Chrome()
driver.get(url)

base_url = url[:-1]


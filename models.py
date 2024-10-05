from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey  # Add ForeignKey here
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Workday_Company_Data(Base):
    __tablename__ = 'workday_company_data'
    Company_ID = Column(Integer, primary_key=True)
    Company_Name = Column(String)
    Company_URL = Column(String)

class Greenhouse_Company_Data(Base):
    __tablename__ = 'greenhouse_company_data'
    Company_ID = Column(Integer, primary_key=True)
    Company_Name = Column(String)
    Company_URL = Column(String)

class Jobs(Base):
    __tablename__ = 'jobs'
    Job_Id = Column(Integer, primary_key=True)
    Job_Url = Column(String)
    Company_ID = Column(Integer, ForeignKey('workday_company_data.Company_ID'))  # Use ForeignKey here
    Posting_Date = Column(Date)
    Job_Title = Column(String)
    Location = Column(String)
    Job_Req_Id = Column(String)

# Other functions (get_database_engine, etc.) remain the same.

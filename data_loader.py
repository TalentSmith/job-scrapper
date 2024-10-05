import pandas as pd
from sqlalchemy.orm import sessionmaker
from models import Workday_Company_Data
from db_setup import get_database_engine  # Adjust the import according to your structure

def load_workday_data_from_csv(csv_file_path):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Create a new session
    engine = get_database_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    new_companies_count = 0  # To count the number of new companies added

    # Iterate through the DataFrame and add records to the database
    for index, row in df.iterrows():
        # Check if the company already exists
        existing_company = session.query(Workday_Company_Data).filter_by(Company_ID=row['Company_ID']).first()
        if existing_company is None:  # Company does not exist, so add it
            company_data = Workday_Company_Data(
                Company_ID=row['Company_ID'],
                Company_Name=row['Company_Name'],
                Company_URL=row['Company_URL']
            )
            session.add(company_data)
            new_companies_count += 1

    # Commit the transaction
    session.commit()
    session.close()
    
    print(f"Data loaded successfully into Workday_Company_Data. {new_companies_count} new companies added.")

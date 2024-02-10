from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import streamlit as st

# Database connection
engine = create_engine('sqlite:///example.db')
metadata = MetaData()

# Define the table structure
table_name = Table('table_name', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String),
                   Column('age', Integer),
                   Column('city', String))

# Create the table if it doesn't exist
metadata.create_all(engine)

# Insert initial seed data
def insert_initial_data(engine, table_name):
    # Check if the table already has data
    with engine.connect() as conn:
        existing_data = conn.execute(table_name.select()).fetchall()
        if not existing_data:  # Only insert if the table is empty
            insert_stmt = table_name.insert().values([
                {'name': 'John Doe', 'age': 28, 'city': 'New York'},
                {'name': 'Jane Smith', 'age': 34, 'city': 'Los Angeles'},
                {'name': 'Emily Jones', 'age': 22, 'city': 'Chicago'},
                {'name': 'Chris Green', 'age': 45, 'city': 'Houston'}
            ])
            conn.execute(insert_stmt)
            conn.commit()

# Call the function to insert data
insert_initial_data(engine, table_name)

# Reading data into a DataFrame
query = "SELECT * FROM table_name"
df = pd.read_sql(query, engine)

# Displaying data in Streamlit
st.write(df)

Base = declarative_base()

# Define a model
class User(Base):
    __tablename__ = 'table_name'

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create a session
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Querying data
users = session.query(User).all()
for user in users:
    st.write(user.name)
    
# Assuming 'User' is a SQLAlchemy model and 'session' is a SQLAlchemy session
# Create
if st.button('Add New User'):
    new_user = User(name='New User')
    session.add(new_user)
    session.commit()

# Read
users = session.query(User).all()
for user in users:
    st.write(user.name)
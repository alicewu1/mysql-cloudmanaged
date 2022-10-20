#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SQLALCHEMY 

import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

### PLEASE USE .ENV FILE TO STORE YOUR PASSWORDS, USERNAMES, HOSTNAME, ETC. ###

# MYSQL_HOSTNAME = 'inserthere'
# MYSQL_USERNAME = 'inserthere'
# MYSQL_PASSWORD = 'inserthere'
# MYSQL_DATABASE = 'inserthere'

## Correct way example here:  https://pypi.org/project/python-dotenv/ 
# use dotenv to load in environment variables


load_dotenv()
GCP_MYSQL_HOSTNAME = os.getenv("GCP_MYSQL_HOSTNAME")
GCP_MYSQL_USER = os.getenv("GCP_MYSQL_USERNAME")
GCP_MYSQL_PASSWORD = os.getenv("GCP_MYSQL_PASSWORD")
GCP_MYSQL_DATABASE = os.getenv("GCP_MYSQL_DATABASE")


########

connection_string = f'mysql+pymysql://{GCP_MYSQL_USER}:{GCP_MYSQL_PASSWORD}@{GCP_MYSQL_HOSTNAME}:3305/{GCP_MYSQL_DATABASE}'
connection_string

engine = create_engine(connection_string)

TABLENAME = MYSQL_USER + 'fakeTableAssignment1'

fakeDataset.to_sql(TABLENAME, con=engine)
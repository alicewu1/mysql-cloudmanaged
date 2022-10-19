#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Creating schemas/tables for patient_portal Database##

import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

# AZURE_MYSQL_HOSTNAME = os.getenv("AZURE_MYSQL_HOSTNAME")
# AZURE_MYSQL_USER = os.getenv("AZURE_MYSQL_USERNAME")
# AZURE_MYSQL_PASSWORD = os.getenv("AZURE_MYSQL_PASSWORD")
# AZURE_MYSQL_DATABASE = os.getenv("AZURE_MYSQL_DATABASE")

GCP_MYSQL_HOSTNAME = os.getenv("GCP_MYSQL_HOSTNAME")
GCP_MYSQL_USER = os.getenv("GCP_MYSQL_USERNAME")
GCP_MYSQL_PASSWORD = os.getenv("GCP_MYSQL_PASSWORD")
GCP_MYSQL_DATABASE = os.getenv("GCP_MYSQL_DATABASE")



########

connection_string_azure = f'mysql+pymysql://{AZURE_MYSQL_USER}:{AZURE_MYSQL_PASSWORD}@{AZURE_MYSQL_HOSTNAME}:3306/{AZURE_MYSQL_DATABASE}'
db_azure = create_engine(connection_string_azure)

# Connect to GCP [MYSQL INSTANCE]
connection_string_gcp = f'mysql+pymysql://{GCP_MYSQL_USER}:{GCP_MYSQL_PASSWORD}@{GCP_MYSQL_HOSTNAME}:3306/{GCP_MYSQL_DATABASE}'
db_gcp = create_engine(connection_string_gcp)

#### note to self, need to ensure server_paremters => require_secure_transport is OFF in Azure 

### show databases
print(db_azure.table_names())
print(db_gcp.table_names())

### 
create_table_patients = """
create table if not exists patients_details_2 (
    id int auto_increment,
    mrn varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    zip_code varchar(255),
    dob varchar(255),
    gender varchar(255),
    contact_mobile varchar(255),
    contact_home varchar(255),
    PRIMARY KEY (id) 
); 
"""

create_table_medications = """
create table if not exists patients_medications (
    id int,
    mrn varchar(255),
    medication_id varchar(255),
    medication_dose varachar(255),
    PRIMARY KEY (id) 
); 
"""

create_table_treatment_procedures = """
create table if not exists medications (
    id int,
    med_ndc varchar(255),
    med_human_name varchar(255),
    med_is_dangerous varchar(255),
    PRIMARY KEY (id) 
); 
"""

create_table_conditions = """
create table if not exists patients_conditions (
    id int,
    mrn varchar(255),
    condition_id varchar(255),
    PRIMARY KEY (id) 
); 
"""

create_table_social_determinants = """
create table if not exists patients_conditions (
    id int,
    mrn varchar(255),
    condition_id varchar(255),
    PRIMARY KEY (id) 
); 
"""

db_gcp.execute(create_table_patients)
db_gcp.execute(create_table_medications)
db_gcp.execute(create_table_treatment_procedures)
db_gcp.execute(create_table_conditions)
db_gcp.execute(create_table_social_determinants)

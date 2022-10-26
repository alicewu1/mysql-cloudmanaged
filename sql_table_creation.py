#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#### CREATING THE SCHEMA/FRAME FOR TABLES IN patient_portal DATABASE ####

import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv # pip install python-dotenv
import os

### drop the old tables that do not start with production_
def droppingFunction_limited(dbList, db_source):
    for table in dbList:
        if table.startswith('production_') == False:
            db_source.execute(f'drop table {table}')
            print(f'dropped table {table}')
        else:
            print(f'kept table {table}')

# drops every single table in the db you are referencing 
def droppingFunction_all(dbList, db_source):
    for table in dbList:
        db_source.execute(f'drop table {table}')
        print(f'dropped table {table} succesfully!')
    else:
        print(f'kept table {table}')

load_dotenv()

GCP_MYSQL_HOSTNAME = os.getenv("GCP_MYSQL_HOSTNAME")
GCP_MYSQL_USER = os.getenv("GCP_MYSQL_USERNAME")
GCP_MYSQL_PASSWORD = os.getenv("GCP_MYSQL_PASSWORD")
GCP_MYSQL_DATABASE = os.getenv("GCP_MYSQL_DATABASE")

# AZURE_MYSQL_HOSTNAME = os.getenv("AZURE_MYSQL_HOSTNAME")
# AZURE_MYSQL_USER = os.getenv("AZURE_MYSQL_USERNAME")
# AZURE_MYSQL_PASSWORD = os.getenv("AZURE_MYSQL_PASSWORD")
# AZURE_MYSQL_DATABASE = os.getenv("AZURE_MYSQL_DATABASE")


########

# connection_string_azure = f'mysql+pymysql://{AZURE_MYSQL_USER}:{AZURE_MYSQL_PASSWORD}@{AZURE_MYSQL_HOSTNAME}:3306/{AZURE_MYSQL_DATABASE}'
# db_azure = create_engine(connection_string_azure)

# Connect to GCP [MYSQL INSTANCE]
connection_string_gcp = f'mysql+pymysql://{GCP_MYSQL_USER}:{GCP_MYSQL_PASSWORD}@{GCP_MYSQL_HOSTNAME}:3306/{GCP_MYSQL_DATABASE}'
connection_string_gcp
db_gcp = create_engine(connection_string_gcp)

#### note to self, need to ensure server_paremters => require_secure_transport is OFF in Azure 

### show tables from databases
# print(db_azure.table_names())
# print(db_gcp.table_names())
tableNames_gcp = db_gcp.table_names()
tableNames_gcp


# reoder tables: production_patient_conditions, production_patient_medications, production_medications, production_patients, production_conditions
# tableNames_azure = ['production_patient_conditions', 'production_patient_medications', 'production_medications', 'production_patients', 'production_conditions']
tableNames_gcp = ['production_patient_conditions', 'production_patient_medications', 'production_medications', 'production_patients', 'production_conditions']


# ### deletes all tables/everything, so you can start at clean slate
# using Python to execute SQL language programmatically and more efficiently
# droppingFunction_all(tableNames_azure, db_azure)
droppingFunction_all(tableNames_gcp, db_gcp)




### CREATING TABLES### 
# raw SQL query can be pasted in MySQL Workbench
#  
create_table_patients = """
create table if not exists production_patients (
    id int auto_increment,
    mrn varchar(255) default null unique,
    first_name varchar(255) default null,
    last_name varchar(255) default null,
    zip_code varchar(255) default null,
    dob varchar(255) default null,
    gender varchar(255) default null,
    contact_mobile varchar(255) default null,
    contact_home varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""

# Check bottom of script: db_gcp.execute(create_table_patients) # executes above command 

#check GCP MySQL Instance Console: show tables;

create_table_medications = """
create table if not exists production_medications (
    id int auto_increment,
    med_ndc varchar(255) default null unique,
    med_human_name varchar(255) default null,
    med_is_dangerous varchar(255),
    PRIMARY KEY (id)
); 
"""


create_table_conditions = """
create table if not exists production_conditions (
    id int auto_increment,
    icd10_code varchar(255) default null unique,
    icd10_description varchar(255) default null,
    PRIMARY KEY (id)
); 
"""


create_table_treatment_procedures = """
create table if not exists production_treatment_procedures (
    id int auto_increment,
    CPT_code varchar(255) default null unique,
    CPT_description varchar(255) default null,
    PRIMARY KEY (id)
); 
"""

create_table_social_determinants = """
create table if not exists production_social_determinants (
    id int auto_increment,
    LOINC_code varchar(255) default null unique,
    LOINC_description varchar(255) default null,
    PRIMARY KEY (id)
); 
"""



table_prod_patients_medications = """
create table if not exists production_patient_medications (
    id int auto_increment,
    mrn varchar(255) default null,
    med_ndc varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (med_ndc) REFERENCES production_medications(med_ndc) ON DELETE CASCADE
); 
"""

table_prod_patient_conditions = """
create table if not exists production_patient_conditions (
    id int auto_increment,
    mrn varchar(255) default null,
    icd10_code varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (icd10_code) REFERENCES production_conditions(icd10_code) ON DELETE CASCADE
); 
"""

table_prod_patient_treatment_procedures = """
create table if not exists production_patient_treatment_procedures (
    id int auto_increment,
    mrn varchar(255) default null,
    CPT_code varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (CPT_code) REFERENCES production_treatment_procedures(CPT_code) ON DELETE CASCADE
); 
"""

table_prod_patient_social_determinants = """
create table if not exists production_patient_social_determinants (
    id int auto_increment,
    mrn varchar(255) default null,
    LOINC_code varchar(255) default null,
    LOINC_description varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (LOINC_code) REFERENCES production_social_determinants(LOINC_code) ON DELETE CASCADE
); 
"""


db_gcp.execute(create_table_patients)
db_gcp.execute(create_table_medications)
db_gcp.execute(create_table_conditions)
db_gcp.execute(create_table_treatment_procedures)
db_gcp.execute(create_table_social_determinants)


db_gcp.execute(table_prod_patients_medications)
db_gcp.execute(table_prod_patient_conditions)
db_gcp.execute(table_prod_patient_treatment_procedures)
db_gcp.execute(table_prod_patient_social_determinants)
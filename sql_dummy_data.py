#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from faker import Faker # pip install faker (https://faker.readthedocs.io/en/master/)
import uuid # used to generate mrn numbers
import random # to create randomness


load_dotenv()

GCP_MYSQL_HOSTNAME = os.getenv("GCP_MYSQL_HOSTNAME")
GCP_MYSQL_USER = os.getenv("GCP_MYSQL_USERNAME")
GCP_MYSQL_PASSWORD = os.getenv("GCP_MYSQL_PASSWORD")
GCP_MYSQL_DATABASE = os.getenv("GCP_MYSQL_DATABASE")



########

connection_string = f'mysql+pymysql://{GCP_MYSQL_USER}:{GCP_MYSQL_PASSWORD}@{GCP_MYSQL_HOSTNAME}:3306/{GCP_MYSQL_DATABASE}'
db = create_engine(connection_string)


#### note to self, need to ensure server_paremters => require_secure_transport is OFF in Azure 

### show databases
print(db.table_names())


### Fake Data code
fake = Faker()

fake_patients = [
    {
        #keep just the first 8 characters of the uuid
        'mrn': str(uuid.uuid4())[:7], 
        'first_name':fake.first_name(), 
        'last_name':fake.last_name(),
        'zip_code':fake.zipcode(),
        'dob':(fake.date_between(start_date='-95y', end_date='-30y')).strftime("%Y-%m-%d"),
        'gender': fake.random_element(elements=('M', 'F')),
        'contact_mobile':fake.phone_number(),
        'contact_home':fake.phone_number()
    } for x in range(50)]

df_fake_patients = pd.DataFrame(fake_patients)

# drop duplicate mrn bc mrn numbers should be unique
df_fake_patients = df_fake_patients.drop_duplicates(subset=['mrn'])
df_fake_patients # view output




#### real icd10 codes (conditions table)
icd10codes = pd.read_csv('https://raw.githubusercontent.com/Bobrovskiy/ICD-10-CSV/master/2020/diagnosis.csv')
list(icd10codes.columns)
icd10codesShort = icd10codes[['CodeWithSeparator', 'ShortDescription']]
icd10codesShort.head(30) # view output

# take 1000 random icd10 codes and create a new df of it
icd10codesShort_1k = icd10codesShort.sample(n=1000)
# drop duplicates
icd10codesShort_1k = icd10codesShort_1k.drop_duplicates(subset=['CodeWithSeparator'], keep='first')
icd10codesShort_1k # view output



#### real ndc codes (medications table)
ndc_codes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/FDA_NDC_CODES/main/NDC_2022_product.csv')
# take 1000 random ndc codes
ndc_codes_1k = ndc_codes.sample(n=1000, random_state=1)
# drop duplicates from ndc_codes_1k
ndc_codes_1k = ndc_codes_1k.drop_duplicates(subset=['PRODUCTNDC'], keep='first')
ndc_codes_1k # view output


#### real cpt codes (treatment procedures table)
cpt_codes = pd.read_csv('https://gist.githubusercontent.com/lieldulev/439793dc3c5a6613b661c33d71fdd185/raw/25c3abcc5c24e640a0a5da1ee04198a824bf58fa/cpt4.csv')
# take 1000 random cpt codes 
cpt_codes_1k = cpt_codes.sample(n=1000, random_state=1)
#drop duplicates from cpt_codes_1k
cpt_codes_1k = cpt_codes_1k.drop_duplicates(subset=['com.medigy.persist.reference.type.clincial.CPT.code'], keep='first')
cpt_codes_1k # view output


### real loinc codes (social determinants table)
loinc_codes = pd.read_csv('data\Loinc.csv')
# take 1000 random loinc codes
loinc_codes_1k = loinc_codes.sample(n=1000, random_state=1)
#drop duplicates from loinc_codes_1k
loinc_codes_1k = loinc_codes_1k.drop_duplicates(subset=['LOINC_NUM'], keep='first')
loinc_codes_1k # view output



########## INSERTING IN FAKE PATIENTS ##########
########## INSERTING IN FAKE PATIENTS ##########
########## INSERTING IN FAKE PATIENTS ##########
########## INSERTING IN FAKE PATIENTS ##########
########## INSERTING IN FAKE PATIENTS ##########
########## INSERTING IN FAKE PATIENTS ##########



#### Approach 1: pandas to_sql
#### Approach 1: pandas to_sql
#### Approach 1: pandas to_sql
#### Approach 1: pandas to_sql


# df_fake_patients.to_sql('production_patients', con=db_azure, if_exists='append', index=False)
# df_fake_patients.to_sql('production_patients', con=db_gcp, if_exists='append', index=False)

# # query db_azure to see if data is there
# df_azure = pd.read_sql_query("SELECT * FROM production_patients", db_azure)
# db_gcp = pd.read_sql_query("SELECT * FROM production_patients", db_gcp)

#### Approach 2: sqlalchemy with dynamic modification of values 
#### Approach 2: sqlalchemy with dynamic modification of values 
#### Approach 2: sqlalchemy with dynamic modification of values 
#### Approach 2: sqlalchemy with dynamic modification of values 

insertQuery = "INSERT INTO production_patients (mrn, first_name, last_name, zip_code, dob, gender, contact_mobile, contact_home) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"


for index, row in df_fake_patients.iterrows():
    # db_azure.execute(insertQuery, (row['mrn'], row['first_name'], row['last_name'], row['zip_code'], row['dob'], row['gender'], row['contact_mobile'], row['contact_home']))
    db.execute(insertQuery, (row['mrn'], row['first_name'], row['last_name'], row['zip_code'], row['dob'], row['gender'], row['contact_mobile'], row['contact_home']))
    print("inserted row: ", index)

# # query dbs to see if data is there
# df_azure = pd.read_sql_query("SELECT * FROM production_patients", db_azure)
df_gcp = pd.read_sql_query("SELECT * FROM production_patients", db)
df_gcp # Verify dummy data has been in MySQL workbench: "select * from patient_portal.production_patients"




########## INSERTING IN FAKE CONDITIONS ##########
########## INSERTING IN FAKE CONDITIONS ##########
########## INSERTING IN FAKE CONDITIONS ##########

insertQuery = "INSERT INTO production_conditions (icd10_code, icd10_description) VALUES (%s, %s)"

startingRow = 0
for index, row in icd10codesShort_1k.iterrows():
    startingRow += 1
    print('startingRow: ', startingRow)
    # db_azure.execute(insertQuery, (row['CodeWithSeparator'], row['ShortDescription']))
    print("inserted row db_azure: ", index)
    db.execute(insertQuery, (row['CodeWithSeparator'], row['ShortDescription']))
    print("inserted row db_gcp: ", index)
    ## stop once we have 100 rows
    if startingRow == 100:
        break

# query dbs to see if data is there
# df_azure = pd.read_sql_query("SELECT * FROM production_conditions", db_azure)
df_gcp = pd.read_sql_query("SELECT * FROM production_conditions", db)
df_gcp


########## INSERTING IN FAKE MEDICATIONS ##########
########## INSERTING IN FAKE MEDICATIONS ##########
########## INSERTING IN FAKE MEDICATIONS ##########

# first, lets query production_medications and production_patients to get the ids

df_medications = pd.read_sql_query("SELECT med_ndc FROM production_medications", db) 
df_medications
df_patients = pd.read_sql_query("SELECT mrn FROM production_patients", db)
df_patients

# create a dataframe that is stacked and give each patient a random number of medications between 1 and 5
df_patient_medications = pd.DataFrame(columns=['mrn', 'med_ndc'])
# for each patient in df_patient_medications, take a random number of medications between 1 and 10 from df_medications and palce it in df_patient_medications
for index, row in df_patients.iterrows():
    # get a random number of medications between 1 and 5
    numMedications = random.randint(1, 5)
    # get a random sample of medications from df_medications
    df_medications_sample = df_medications.sample(n=numMedications)
    # add the mrn to the df_medications_sample
    df_medications_sample['mrn'] = row['mrn']
    # append the df_medications_sample to df_patient_medications
    df_patient_medications = df_patient_medications.append(df_medications_sample)

print(df_patient_medications.head(10))

# now lets add a random medication to each patient
insertQuery = "INSERT INTO production_patient_medications (mrn, med_ndc) VALUES (%s, %s)"

for index, row in df_patient_medications.iterrows():
    db.execute(insertQuery, (row['mrn'], row['med_ndc']))
    print("inserted row: ", index)





########## INSERTING IN FAKE TREATMENT PROCEDURES ##########
########## INSERTING IN FAKE TREATMENT PROCEDURES ##########
########## INSERTING IN FAKE TREATMENT PROCEDURES ##########

df_treatment_procedures = pd.read_sql_query("SELECT CPT_code FROM production_treatment_procedures", db)
df_patients = pd.read_sql_query("SELECT mrn FROM production_patients", db)

df_patient_treatment_procedures = pd.DataFrame(columns=['mrn', 'CPT_code'])

insertQuery = "INSERT INTO production_treatment_procedures (CPT_code, CPT_description) VALUES (%s, %s)"

proceduresRowCount = 0
for index, row in cpt_codes_1k.iterrows():
    startingRow += 1
    print('startingRow: ', startingRow)
    db.execute(insertQuery, (row['com.medigy.persist.reference.type.clincial.CPT.code'], row['label']))
    print("inserted row db_gcp: ", index)
    ## stop once we have 100 rows
    if startingRow == 100:
        break

df_gcp = pd.read_sql_query("SELECT * FROM production_treatment_procedures", db)
df_gcp


########## INSERTING IN FAKE SOCIAL DETERMINANTS ##########
########## INSERTING IN FAKE SOCIAL DETERMINANTS ##########
########## INSERTING IN FAKE SOCIAL DETERMINANTS ##########

df_social_determinants = pd.read_sql_query("SELECT LOINC_code from production_social_determinants", db)
df_patients = pd.read_sql_query("SELECT mrn FROM production_patients", db)

df_patient_social_determinants = pd.DataFrame(columns=['mrn', 'LOINC_code'])

for index, row in df_patients.iterrows():
    numSocDet= random.randint(1, 5)
    df_social_determinants_sample = df_social_determinants.sample(n=numSocDet)
    df_social_determinants_sample['mrn'] = row['mrn']
    df_patient_social_determinants = df_patient_social_determinants.append(df_social_determinants_sample)


print(df_patient_social_determinants.head(10))


# now lets add a random loinc code to each patient
insertQuery = "INSERT INTO production_social_determinants (mrn, LOINCS_code) VALUES (%s, %s)"

for index, row in df_patient_medications.iterrows():
    db.execute(insertQuery, (row['mrn'], row['LOINC_code']))
    print("inserted row: ", index)


df_gcp = pd.read_sql_query("SELECT * FROM production_social_determinants", db)
df_gcp
# mysql-cloudmanaged
**HHA504 / Assignment 8 / Cloud-managed SQL DB + ERD + Dummy Data**

### This repo aims to:
- create a cloud-managed MySQL db on GCP
- use python to create tables in sql and reproduce relationships between tables without repeating commands
- experiment with various methods of using MySQL (remote mysql instance, local using MySQL client, MySQL workbench) 
- create an ERD using MySQL Workbench
- create realistic patient dummy data usinf **faker** python package
<br>

### **Note:** Initially, I manually created dummy patient data to insert into the tables in my db/ However, I have since revised the python scripts to utilize the ***faker*** package to auto-generate realistic dummy patient data into my tables. I have included screenshots of my old dummy data versus my new dummy data in my ***images*** folder.

<br>

# **TASKS:**
# 1. **setup.md**: 
- How I setup and connect my GCP Compute Engine VM Instance to a MySQL dev env
- How I setup a GCP MySQL Instance
- How I setup MySQL Workbench
- Lists the corresponding dependencies for each module

<br>

# **2. Create a new DB in the MySQL instance called *patient_portal***
1. Log back into mysql server, create, verify new db using:
        
        mysql -u root -h [MySQL instance IP address] -p
        password
        create database patient_portal;
        show databases \G;
2. Change into new db directory to create a table:
       Use patient_portal;

<br>

------

# **3. CREATING TABLES AND TABLE RELATIONSHIPS IN PYTHON**
# Part 3.1: ***sql_table_creation.py:*** 
1.  Packages Used:
    -       import dbm
            import pandas as pd 
            import sqlalchemy
            from sqlalchemy import create_engine
            from dotenv import load_dotenv # pip install python-dotenv
            import os

2. Create tables (various methods):    
    -       production_patients
            production_medications
            production_conditions
            production_treatment_procedures
            production_social_determinants

    -  If using MySQL Workbench: Paste raw SQL Query into workbench
    -  If using terminal: Run code through instance console or local cmd terminal using MySQL client
    - id int auto_increment: is the index, auto generates ID variables
    - PRIMARY KEY (id): must define PRIMARY KEY or defaults to first line

    -       use patient_portal;
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

     
3. Verify that tables have been created within MySQL console
    - In MySQL Workbench:
    -      Refresh "Tables" tab under Schema
    - In SQL Instance Terminal
    -     show tables;





<br>

# Part 3.2: ***sql_dummy_data.py:*** Create realistic dummy patient data using the following resources
- Medications (NDC codes) : https://dailymed.nlm.nih.gov/dailymed/index.cfm 
- Treatments/Procedures (CPT) : https://www.aapc.com/codes/cpt-codes-range/1  
- Conditions (ICD10 codes): https://icdcodelookup.com/icd-10/codes
- Social_Determinants (LOINC codes) : https://www.findacode.com/loinc/LG41762-2--socialdeterminantsofhealth.html

    - Verify tables are populated in MySQL console


1. Packages Used:
    -       import dbm
            import pandas as pd 
            import sqlalchemy
            from sqlalchemy import create_engine
            from dotenv import load_dotenv
            import os
            from faker import Faker # https://faker.readthedocs.io/en/master/
            import uuid # used to generate mrn numbers
            import random # creates randomness

2. Use .csv of ICD10 codes 



<br>

-----
# 4. Create an Entity Relationship Diagram (ERD) for my DB design using MySQL Work Bench. 
- Must have at least two foreignKeys representing a relationship between at least 2 tables. 
- Shows the rows and columns in created within the tables 
- Shows elevated perspective of Schemas view

- In MySQL Workbench, select:
    -       Database > Reverse Engineer
            Loads host credentials and enter password
            Select db patient_portal
            Select Import MYSQL Table Objects
            Check: Place imported objects on a diagram 
            Execute
            Select: Reverse Engineer Selected Objects and Place Objects on Diagram
            Reorganize diagram using drag 
            Save and Export as .PNG

<br>

------

# 5. ***images*** folder
    - screen shot of a ERD of your proposed setup (use either popSQL or mysql work bench) 
    - screen shot of you connected to the sql server, performing the following two queries: 
        - Query1: show databases (e.g., show databases;) 
        - Query2: all of the tables from your database (e.g., show tables;)  
        - Query3: select * from patient_portal.medications 
        - Query4: select * from patient_portal.treatment_procedures
        - Query5: select * from patient_portal.conditions

<br>

------
# 6. Consider backups
- Hot Backups: Read Replicas on GCP, immediately jump into 2nd database
- Cold Backups: Typically .csv files that needs to be deployed to another mysql env

# mysql-cloudmanaged
HHA504 / Assignment 8 / ERD

### This repo aims to:
- create a cloud-managed MySQL db on GCP
- use python to create tables in sql and reproduce relationships between tables without repeating commands 

<br>

# **TASKS:**
# 1. ***setup.md:*** How i setup and connect my GCP Compute Engine VM Instance to a MySQL env

<br>

# 2. Create a new DB in the MySQL instance called patient_portal  
1. Log back into mysql server, create, verify new db using:
        
        mysql -u root -h [MySQL instance IP address] -p
        password
        create database patient_portal;
        show databases \G;
2. Change into new db directory to create a table:
       Use patient_portal;

<br>

------

# 3. Creating tables and table relationships using python
## ***sql_table_creation.py:*** Change into new db directory to create new tables

       use patient_portal;

1. Create tables:    
    - patients_details
    - patients_medications
    - treatments_procedures
    - patients_conditions
    - social_determinants
     
2. Verify that tables have been created within MySQL console

<br>

## ***sql_dummy_data.py:*** Create realistic dummy patient data using the following resources
- Medications (NDC codes) : https://dailymed.nlm.nih.gov/dailymed/index.cfm 
- Treatments/Procedures (CPT) : https://www.aapc.com/codes/cpt-codes-range/1  
- Conditions (ICD10 codes): https://icdcodelookup.com/icd-10/codes
- Social_Determinants (LOINC codes) : https://www.findacode.com/loinc/LG41762-2--socialdeterminantsofhealth.html

    - Verify tables are populated in MySQL console

<br>

-----
# 4. Create an ERD for your DB design using MySQL Work Bench. 
- You must have at least two foreignKeys representing a relationship between at least 2 tables. 



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

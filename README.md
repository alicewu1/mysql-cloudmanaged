# mysql-cloudmanaged
HHA504 / Assignment 8 / ERD

# This repo aims to:
1. Create a cloud-managed MySQL DB on either Azure or GCP
2. Create a new database inside of that mysql instance called patient_portal  
3. Create a python script called (sql_table_creation.py) that creates the following tables inside of patient_portal: patients, medications, treatments_procedures, conditions, and social determinants. Be sure to use a .env file to hide your login credentials 
4. Create a python script called (sql_dummy_data.py) using python and send some dummy data into each of the tables. Please see notes for ideas related to dummy data. 
5. Create an ERD for your DB design using MySQL Work Bench. You must have at least two foreignKeys representing a relationship between at least 2 tables. 

6. Github docs to include: 
- a python script that contains the SQL code to create db (sql_table_creation.py) 
- a python script that contains code to insert in some dummy data (sql_dummy_data.py) 
- a readme file that describes a) where you setup the mySQL db, b) any issues you ran into 
- a images folder that contains: 
    - screen shot of a ERD of your proposed setup (use either popSQL or mysql work bench) 
    - screen shots of you connected to the sql server, performing the following queries: 
        - Query1: show databases (e.g., show databases;) 
        - Query2: all of the tables from your database (e.g., show tables;)  
        - Query3: select * from patient_portal.medications 
        - Query4: select * from patient_portal.treatment_procedures
        - Query5: select * from patient_portal.conditions

Be CREATE with your dummy data and find examples that are from real-world codexes: 
Medications: NDC codes
Treatments/Procedures: CPT 
Conditions: ICD10 codes
Social_Determinants: LOINC codes 

Resources to pull some test data: 
NDC: https://dailymed.nlm.nih.gov/dailymed/index.cfm 
CPT: https://www.aapc.com/codes/cpt-codes-range/
ICD: https://icdcodelookup.com/icd-10/codes
LOINC: https://www.findacode.com/loinc/LG41762-2--socialdeterminantsofhealth.html


# sql_table_creation.py
- python script that contains the SQL code to create the db

# sql_dummy_data.py
- python script that contains code to insert dummy data for this exercise

<br>
-----

# SETTING UP MYSQL ENV ON GCP VM INSTANCE

## MySQL REQUIREMENTS AND DEPENDENCIES FOR THE INSTANCE
1. 2 vCPU | 4 GB RAM | 10 GB | Ubuntu 18.04 LTS
2. Allow traffic for: HTTP. HTTPS. SSH, MySQL
3. Create a new firewall rule to enable MySQL traffic (Open port 3306)
- Name: mysql-allow
- Target Tags: All instances in the network
- Source IP ranges: 0.0.0.0/0
- Protocols and ports: Check [TCP]: 3306

## EDITING THE CONFIG FILE TO CHANGE BIND ADDRESSES
1. Go to config file:
     -      sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
2. Change **bind address** and **mysqlx-bind-address** from 127.0.0.1 to 0.0.0.0/0
3. **Restart mysql server to activate changes:**
    -       sudo /etc/init.d/mysql restart
4. [For Azure VM, add: Inbound security rule
Service: MySQL, which auto-adds port 3306,
Name it: mysql-custom-allow]


## Store .env file in the foot directory with following structure: 
- MYSQL_HOSTNAME = "inserthere"
- MYSQL_USERNAME = "inserthere"
- MYSQL_PASSWORD = "inserthere"
- MYSQL_DATABASE = "inserthere"

## .SSH TERMINAL SETUP ON GCP
1.      sudo apt-get update 
2.      sudo apt install mysql-client mysql-server # provides many dbs
3.      sudo mysql # connecting to server 
4.      show databases \G; Show what databases exist within the server
5.      \q to leave the mysql server

<br>

## CREATE A NEW DBA USER (database administrator)
1. Create user: (@ = wildcard // % = where DBA can be connected from: anhywhere)
    -       Create user 'username'@'%' identified by 'ahi2022';
2. To get a list of users:
    -       select * from mysql.user 
3. To get **NEAT** list of users:
    -       select * from mysql.user \G;
4. Query to get a list of usernames only: 
    -       select user, host, password_expired, authentication_string, password_last_changed from mysql.user \G; 
5. Exit mysql server: 
   -        \q
6. LOGGING INTO MYSQL SERVER
    -       mysql -u alice -p 
7.      enter [password] 
8. ENTER QUERY:
   -        select * from mysql.users;
9. Fix user permissions error: 
    -       grant all privileges on *.* TO 'alice'@'%' with grant option;
10. Confirm privileges are opened to your user:
    -       show grants for alice \G;

<br>


## SETTING UP GCP [MYSQL INSTANCE]
1. Under SQL tab, create MySQL Instance with the following requirements:
- 2 vCPU | 8 GB Memory | 100 GB Storage  
- Version: MySQL 8.0 (Default)
- Choose Configuration: Development 
- Under Configuration Details:
    - Machine Type: Lightweight
- Everything else Default

2. Create Instance Name
3. Enter Password (becomes **root** user password)

## CONNECT GCP [COMPUTE ENGINE INSTANCE] TO GCP [MYSQL INSTANCE]
1. In GCP Compute Engine Instance:
-   mysql -u root [MySQL Instance IP Address] -p
2. Enter pass: [root user password] Ahi2020!

- 
## CREATE A NEW DB IN MYSQL SERVER
1. Log back into mysql server using:
   -        mysql -u root -p
2.      CREATE DATABASE patient_portal;
3. Verify db was created by show all databases using:
    -       show databases \G;
4. Change into new db directory to create a table:
    -       Use patient_portal;


# USING PYTHON TO CREATE TABLES WITHIN NEW DB [sql_table_creation.py]
1. Change into new db directory to create a table:
    -       Use patient_portal;
2. Create 5 table named: patients, medications, treatments_procedures, conditions,social determinants


# BACKUPS
1. Hot Backups: Read Replicas on GCP, immediately jump into 2nd database
2. Cold Backups: Typically .csv files that needs to be deployed to another mysql env


<br>

# /images folder
- screen shot of a ERD of your proposed setup (use either popSQL or mysql work bench) 
    - screen shot of you connected to the sql server, performing the following two queries: 
        - Query1: show databases (e.g., show databases;) 
        - Query2: all of the tables from your database (e.g., show tables;)  
        - Query3: select * from patient_portal.medications 
        - Query4: select * from patient_portal.treatment_procedures
        - Query5: select * from patient_portal.conditions



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


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


## patients_details table:
#     id int auto_increment,
#     mrn varchar(255),
#     first_name varchar(255),
#     last_name varchar(255),
#     zip_code varchar(255),
#     dob varchar(255),
#     gender varchar(255),
#     weight varchar (255),
#     contact_mobile varchar(255),
#     insurance_id varchar(255),
#     PRIMARY KEY (id) 

fakePatientDetailsTest = """
insert into patients_details (id, mrn, first_name, last_name, zip_code, dob, gender, weight, contact_mobile, insurance_id) values 
(1, '0001', 'aaron', 'kennedy', '10010', '01/01/1980', 'male', '182 lbs', '341-132-8830', '123456');
"""

fakePatientDetailsAll = """
insert into patients_details values 
(2, '0002', 'barry', 'applegate', '11012', '02/02/1981', 'male', '172 lbs', '132-465-4268', '234567'), 
(3, '0003', 'chelsea', 'smith', '10013', '01/01/1995', 'female', '130 lbs', '234-049-1102', '345678'), 
(4, '0004', 'daniel', 'taylor', '10234', '01/01/1993', 'male', '164 lbs', '621-435-5555', '456789'), 
(5, '0005', 'ezkiel', 'thompas', '11008', '01/01/1967', 'male', '202 lbs', '312-004-3312', '567890'), 
(6, '0006', 'fiona', 'lopez', '18225', '01/01/1975', 'female', '127 lbs', '621-963-1821', '028443'), 
(7, '0007', 'gary', 'miller', '10292', '01/01/2002', 'male', '129 lbs', '621-220-6457', '428914'), 
(8, '0008', 'harold', 'davis', '17392', '01/01/1991', 'male', '148 lbs', '621-325-1125', '889360'), 
(9, '0009', 'izzy', 'johnson', '11005', '01/01/1990', 'female', '116 lbs', '621-442-7990', '433219'), 
(10, '0010', 'jessica', 'lee', '17750', '01/01/2000', 'female', '102 lbs', '621-198-4239', '523482')
;
"""



## patients_medications table:
#     id int,
#     mrn varchar(255),
#     medication_id varchar(255),
#     medication_dose varchar(255),
#     drug_class varchar(255),
#     date_start_taking varchar(255),
#     side_effects varchar(255),
#     PRIMARY KEY (id)

fakeMedication = """
insert into patients_medications (id, mrn, medication_id, medication_dose, drug_class, date_start_taking, side_effects) values 
(1, '0001', '68727-100-01', '10mg', 'CNS depressants', '11/05/2002', 'slow brain function'),
(2, '0002', '42982-4441-1', '12mg', 'CNS stimulants', '05/28/2015', 'elevated BP'),
(3, '0003', '43598-678-11', '25mg', 'hallucinogens', '02/13/2009', 'hallucinations'),
(4, '0004', '53225-4210-1', '1mg', 'dissociative anesthetics', '10/19/2018', 'nausea'),
(5, '0005', '42192-618-05', '5mg', 'narcotic analgesics', '04/01/2021', 'constipation'),
(6, '0006', '73395-196-01', '84mcg', 'inhalants', '07/14/2016', 'slurred speech'),
(7, '0007', '73002-332-02', '2mg', 'cannabis', '04/24/2019', 'cough')
;
"""



## treatment_procedures table:
#     id int,
#     mrn varchar(255),
#     med_ndc varchar(255),
#     med_is_dangerous varchar(255),
#     procedure_code varchar(255),
#     signed_consent_form varchar(255),
#     PRIMARY KEY (id)

fakeTreatmentProcedures = """
insert into treatment_procedures (id, mrn, med_ndc, med_is_dangerous, procedure_code, signed_consent_form) values 
(1, '0001', '68727-100-01', 'Yes', '00160', 'Yes'),
(2, '0002', '42982-4441-1', 'Yes', '00604', 'Yes'),
(3, '0003', '43598-678-11', 'No', '0609T', 'No'),
(4, '0004', '53225-4210-1', 'Yes', '0249U', 'No'),
(5, '0005', '42192-618-05', 'Yes', '4035F', 'Yes'),
(6, '0006', '73395-196-01', 'No', '6102F', 'Yes'),
(7, '0007', '73002-332-02', 'No', '4153F', 'No')
;
"""



## patients_conditions table:
#     id int,
#     mrn varchar(255),
#     condition_id varchar(255),
#     chronic_condition_id varchar(255),
#     PRIMARY KEY (id)

fakePatientConditions = """
insert into patients_conditions (id, mrn, condition_id, chronic_condition_id) values 
(1, '0001', 'P91.4', 'E08'),
(2, '0002', 'F31', 'D63.1'),
(3, '0003', 'F25', 'K70'),
(4, '0004', 'F44.81', 'Z82.3'),
(5, '0005', 'F60.3', 'E08'),
(6, '0006', 'F06.0', 'I10'),
(7, '0007', 'P91.4', 'I27.0')
;
"""

# EXECUTE PREVIOUS COMMANDS

db.execute(fakePatientDetailsTest)
db.execute(fakePatientDetailsAll)
db.execute(fakeMedication)
db.execute(fakeTreatmentProcedures)
db.execute(fakePatientConditions)
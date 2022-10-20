## MySQL REQUIREMENTS AND DEPENDENCIES FOR THE INSTANCE
-       2 vCPU | 4 GB RAM | 10 GB | Ubuntu 18.04 LTS
        Allow traffic for: HTTP. HTTPS. SSH, MySQL
        Create a new firewall rule to enable MySQL traffic (Open port 3306)
            - Name: mysql-allow
            - Target Tags: All instances in the network
            - Source IP ranges: 0.0.0.0/0
            - Protocols and ports: Check [TCP]: 3306

## EDITING THE CONFIG FILE TO CHANGE BIND ADDRESSES
1. Go to config file:
    -       sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
2. Change **bind address** and **mysqlx-bind-address** from 127.0.0.1 to 0.0.0.0/0
3. **Restart mysql server to activate changes:**
    -       sudo /etc/init.d/mysql restart
4. For Azure VM, add: **Inbound security rule** 
    - Service: MySQL, which auto-adds port 3306 
    - Name it: mysql-custom-allow]


## Store .env file in the **root** directory with following structure: 
    MYSQL_HOSTNAME = "inserthere" 
    MYSQL_USERNAME = "inserthere"
    MYSQL_PASSWORD = "inserthere"
    MYSQL_DATABASE = "inserthere"

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
    -   2 vCPU | 8 GB Memory | 100 GB Storage  
    -   Version: MySQL 8.0 (Default)
    -   Choose Configuration: Development 
    -   Under Configuration Details:
        -   Machine Type: Lightweight
    -   Everything else Default

2. Create Instance Name
3. Enter Password (becomes **root** user password)

## CONNECT GCP [COMPUTE ENGINE INSTANCE] TO GCP [MYSQL INSTANCE]
1. In GCP Compute Engine Instance:
    -       mysql -u root -h [MySQL Instance IP Address] -p
2. Enter pass: [root user password] 

<br> 
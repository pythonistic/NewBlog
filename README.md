Database Installation
---------------------
The blog software schema is designed to work with MySQL and the 
SQLAlchemy driver is hardcoded to MySQL.  For the documentation, I'm 
using the database name _mischiefblog_.

### Debian/Ubuntu
    apt-get install mysql libmysqlclient-dev python-dev

### MacPorts
    sudo port install mysql56 mysql56-server
    sudo -u _mysql /opt/local/lib/mysql56/bin/mysql_install_db
    sudo port load mysql56-server
    opt/local/lib/mysql56/bin/mysqladmin -u root password 'new-password'
    echo 'export PATH=/opt/local/lib/mysql56/bin:$PATH' >> ~/.bash_profile
    chmod u+x ~/.bash_profile
    source ~/.bash_profile
    echo '[mysqld]' > /opt/local/etc/mysql56/macports-default.cnf

Use the password you configured when setting up mysql to connect to the 
database using the MySQL client.

    mysql -u root -p
    create database if not exists mischiefblog charset utf8 collate utf8_general_ci; 

I create three users:
* A schema owner (mischiefblog) used to apply the DDL
* An application user (mischiefblog_u) with limited rights
* A unit test (mischiefblog_ut) user with more rights

    grant all on mischiefblog.* to 'mischiefblog'@'localhost';
    set password for 'mischiefblog'@'localhost' = password('mischiefblog'); 
    grant all on mischiefblog.* to 'mischiefblog'@'127.0.0.1';
    set password for 'mischiefblog'@'127.0.0.1' = password('mischiefblog'); 
    grant all on mischiefblog.* to 'mischiefblog'@'::1';
    set password for 'mischiefblog'@'::1' = password('mischiefblog'); 

    grant select, insert, update, show view, create temporary tables on mischiefblog.* to 'mischiefblog_u'@'localhost';
    set password for 'mischiefblog_u'@'localhost' = password('mischiefblog_u');
    grant select, insert, update, show view, create temporary tables on mischiefblog.* to 'mischiefblog_u'@'127.0.0.1';
    set password for 'mischiefblog_u'@'127.0.0.1' = password('mischiefblog_u');
    grant select, insert, update, show view, create temporary tables on mischiefblog.* to 'mischiefblog_u'@'::1';
    set password for 'mischiefblog_u'@'::1' = password('mischiefblog_u');
     
    grant select, insert, update, delete, show view, create temporary tables on mischiefblog.* to 'mischiefblog_ut'@'localhost';
    set password for 'mischiefblog_ut'@'localhost' = password('mischiefblog_ut'); 
    grant select, insert, update, delete, show view, create temporary tables on mischiefblog.* to 'mischiefblog_ut'@'127.0.0.1';
    set password for 'mischiefblog_ut'@'127.0.0.1' = password('mischiefblog_ut'); 
    grant select, insert, update, delete, show view, create temporary tables on mischiefblog.* to 'mischiefblog_ut'@'::1';
    set password for 'mischiefblog_ut'@'::1' = password('mischiefblog_ut'); 

The grants should be tightened to the app server IPs in a production 
environment.

Deploy the schema to the database using the schem owner account.

    mysql -h 127.0.0.1 -P 3306 -u mischiefblog -p mischiefblog < db/ddl.sql

Python Version
--------------
The blog software is written in Python 2.7 to match the deployment 
environment (Dreamhost).

### Debian/Ubuntu 
    apt-get install python python-virtualenv

### MacPorts
    sudo port install python27 py27-setuptools

Python Environment
------------------
I typically write and install software to a _virtualenv_.  Python 3.3+ 
users can use virtualenv or pyvenv.

    virtualenv -p python2.7 Blog
    
Activate the virtualenv to install the Python packages using pip.

    source Blog/activate
    pip install Flask SQLAlchemy Flask-SQLAlchemy MySQL-python coverage

Environment Variables
---------------------
To run the blog software, you need to set *BLOG_DB_CONFIG* to point to 
your copy of db.properties. I recommend you install this in a secured 
directory and only make the directory and start script readable to the 
user ID running the blog software.

When unit testing, you can create a separate BLOG_DB_CONFIG environment 
variable to point to a unit test configuration for the database which 
uses the unit test user:  unit tests need delete, while your normal blog 
application user won't.

You may need to use an explicit path and I would recommend that for all 
production installations.

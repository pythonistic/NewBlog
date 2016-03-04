Database Installation
---------------------
The blog software schema is designed to work with MySQL and the SQLAlchemy driver is hardcoded to 
MySQL.  For the documentation, I'm using the database name _mischiefblog_.

    apt-get install mysql libmysqlclient-dev python-dev
    mysql –u root –p 

Use the password you configured when setting up mysql.

    create database if not exists mischiefblog charset utf8 collate utf8_general_ci; 

I create three users:
* A schema owner (mischiefblog) used to apply the DDL
* An application user (mischiefblog_u) with limited rights
* A unit test (mischiefblog_ut) user with more rights

    grant all on mischiefblog.* to 'mischiefblog'@'localhost'; 
    set password for 'mischiefblog'@'localhost' = password('mischiefblog'); 

    grant select, insert, update, show view, create temporary tables on mischiefblog.* to 'mischiefblog_u'@'%'; 
    set password for 'mischiefblog_u'@'%' = password('mischiefblog_u');
     
    grant select, insert, update, delete, show view, create temporary tables on mischiefblog.* to 'mischiefblog_ut'@'%'; 
    set password for 'mischiefblog_ut'@'%' = password('mischiefblog_ut'); 

The grants should be tightened to the app server IPs in a production environment. 

Python Version
--------------
The blog software is written in Python 2.7 to match the deployment environment (Dreamhost).
The following instructions are appropriate for Debian or Ubuntu based systems.  

    apt-get install python python-virtualenv
        
Python Environment
------------------
I typically write and install software to a _virtualenv_.  Python 3.3+ users can use virtualenv or pyvenv.

    virtualenv -p python2.7 Blog
    
Activate the virtualenv to install the Python packages using pip.

    source Blog/activate
    pip install Flask SQLAlchemy Flask-SQLAlchemy MySQL-python coverage

Environment Variables
---------------------
To run the blog software, you need to set *BLOG_DB_CONFIG* to point to your copy of db.properties.  
I recommend you install this in a secured directory and only make it readable to the user ID
running the blog software.

When unit testing, you can create a separate BLOG_DB_CONFIG environment variable to point to
a unit test configuration for the database which uses the unit test user:  unit tests need
delete, while your normal blog application user won't.

You may need to use an explicit path, and I would recommend that for all production installations.
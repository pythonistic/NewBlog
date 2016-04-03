from __future__ import print_function
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ConfigParser
import os
import sqlalchemy.pool
import sys

# environment variable pointing to the DB properties file
db_props_file = './db.properties'

if 'BLOG_DB_CONFIG' in os.environ:
    db_props_file = os.environ['BLOG_DB_CONFIG']

if not os.path.exists(db_props_file):
    print('BLOG_DB_CONFIG path %s does not exist' % db_props_file, file=sys.stderr)
    sys.exit(-2)

db_section = 'Database'
db_configuration = ConfigParser.SafeConfigParser()
db_configuration.read(db_props_file)
db_debug = db_configuration.getboolean(db_section, 'debug')
db_hostname = db_configuration.get(db_section, 'hostname')
db_port = db_configuration.getint(db_section, 'port')
db_schema = db_configuration.get(db_section, 'schema')
db_username = db_configuration.get(db_section, 'username')
db_password = db_configuration.get(db_section, 'password')
db_pooling = db_configuration.get(db_section, 'pooling')

db_pool = None

if db_pooling not in ['NullPool', 'QueuePool', 'SingletonThreadPool', 'StaticPool']:
    print('WARNING: pool %s may not be supported' % db_pooling, file=sys.stderr)
else:
    if db_pooling == 'NullPool':
        db_pool = sqlalchemy.pool.NullPool
    elif db_pooling == 'QueuePool':
        db_pool = sqlalchemy.pool.QueuePool
    elif db_pooling == 'SingletonThreadPool':
        db_pool = sqlalchemy.pool.SingletonThreadPool
    elif db_pooling == 'StaticPool':
        db_pool = sqlalchemy.pool.StaticPool

db_pool_size = None
db_max_overflow = None
db_timeout = None

if db_pooling == 'QueuePool':
    db_pool_size = 5
    db_max_overflow = 10
    db_timeout = 30
    if db_configuration.has_option(db_section, 'pool_size'):
        db_pool_size = db_configuration.getint(db_section, 'pool_size')
    if db_configuration.has_option(db_section, 'max_overflow'):
        db_max_overflow = db_configuration.getint(db_section, 'max_overflow')
    if db_configuration.has_option(db_section, 'db_timeout'):
        db_timeout = db_configuration.getint(db_section, 'db_timeout')
elif db_pooling == 'SingletonThreadPool':
    if db_configuration.has_option(db_section, 'pool_size'):
        db_pool_size = db_configuration.getint(db_section, 'pool_size')

db_url = 'mysql://%s:%s@%s:%d/%s' % (db_username, db_password, db_hostname, db_port, db_schema)
print(db_url)

if db_pool:
    if db_pool_size:
        if db_max_overflow and db_timeout:
            db_engine = create_engine(db_url, echo=db_debug, poolclass=db_pool, pool_size=db_pool_size,
                                      max_overflow=db_max_overflow, timeout=db_timeout)
        else:
            db_engine = create_engine(db_url, echo=db_debug, poolclass=db_pool, pool_size=db_pool_size)
    else:
        db_engine = create_engine(db_url, echo=db_debug, poolclass=db_pool)
else:
    db_engine = create_engine(db_url, echo=db_debug)

Session = sessionmaker()
Session.configure(bind=db_engine)

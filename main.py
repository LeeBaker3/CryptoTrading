import numpy as np
import pandas as pd
import tensorflow as tf
from appconfig.loadconfig import LoadConfig as lc
from db.createdb import CreateDB

# Load applications settings
# Variable 'c' is a LoadSetting object
# Variable 'settings' is dictionary that holds applications settings
# Application settings definition xxxxxx 
c = lc()
settings = c.get_config()
print('Mode: ', settings['STATE']['mode'])
db_name='cryptotradingdb.db' 
sql_file_name='cryptotradingdb.sql'
csv_table_map_filename='base_data_file_to_table_map.csv'
db_location='db/' 
db_files_location='db/'
db = CreateDB(db_name, db_location, db_files_location, sql_file_name, csv_table_map_filename, )
db.create_new_db()




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
db = CreateDB()
db.create_new_db()



import numpy as np
import pandas as pd
import tensorflow as tf
from loadconfig import LoadConfig as lc

# Load applications settings
# Variable 'c' is a LoadSetting object
# Variable 'settings' is dictionary that holds applications settings
# Application settings definition xxxxxx 
c = lc()
settings = c.getConfig()
print('Mode: ', settings['STATE']['mode'])

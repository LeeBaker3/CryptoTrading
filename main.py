import numpy as np
import pandas as pd
import tensorflow as tf
from loadsettings import LoadSetting as ld

# Load applications settings
# Vadriable 's' is a LoadSetting object
# Variable 'settings' is dictonary that holds applications settings
# Application settings definition xxxxxx 
s = ld()
settings = s.get_Settings()
print('Mode: ', settings['MODE'])

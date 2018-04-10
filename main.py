import numpy as np
import pandas as pd
#import tensorflow as tf
from loadsettings import LoadSetting as ld

#Load applications settings

s = ld()
settings = s.get_Settings()
print('Mode: ', settings['MODE'])

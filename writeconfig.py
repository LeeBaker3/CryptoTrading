"""[Summary]
Generate application settings.ini file
"""

import configparser as cp
# configparser documentation https://docs.python.org/3/library/configparser.html

config = cp.ConfigParser(allow_no_value=True)
config['DEFAULT'] = {'MODE': 'Training'}

config['STATE'] = {}
config.set('STATE', 'MODE', 'Training')
config.set('STATE', ' # Three options available for Mode:') 
config.set('STATE', ' # Training = Used to training the machine learning model.')
config.set('STATE', ' # Testing = Used to test the application.')
config.set('STATE', ' # Production = Used to run the application.')

with open('settings.ini', 'w') as configfile:
    config.write(configfile)
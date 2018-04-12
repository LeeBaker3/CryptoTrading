class LoadSetting(object):

    import json
    import configparser as cp

    def __init__(self, settings = None):
        self.settings = settings

    def as_dict(self, config):
    
    #Converts a ConfigParser object into a dictionary.
    #The resulting dictionary has sections as keys which point to a dict of the
    #sections options as key => value pairs.

        the_dict = {}
        for section in config.sections():
            the_dict[section] = {}
            for key, val in config.items(section):
                the_dict[section][key] = val
        return the_dict 
    
    def get_Settings(self):

        #with open("settings.json") as json_file:
             #self.settings = self.json.load(json_file)

        config = self.cp.ConfigParser()
        config.read('settings.ini')

        self.settings = self.as_dict(config)

        return self.settings
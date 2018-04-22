"""[Summary]
Reads the application settings from .ini file. Converts it to a dictionary object
and returns the dictionary to the calling object.
"""

class LoadConfig(object):

    import configparser as cp
    # configparser documentation https://docs.python.org/3/library/configparser.html

    def __init__(self, settings = None):
        self.settings = settings

    def as_dict(self, config):
        """[summary]
        Converts a ConfigParser object into a dictionary.
    
        Arguments:
            config {[configparser object]} -- 
    
        Returns:
            [dictionary object] -- [The resulting dictionary has sections as 
            keys which point to a dict of the sections options as key => value pairs.]
        """

        the_dict = {}
        for section in config.sections():
            the_dict[section] = {}
            for key, val in config.items(section):
                the_dict[section][key] = val
        return the_dict 

    def get_config(self):
        """[summary]
        Returns a dictionary of the application settings from the settings.ini file
        
        Returns:
            [dictionary object] -- [The resulting dictionary has sections as 
            keys which point to a dict of the sections options as key => value pairs.]
        """
        config = self.cp.ConfigParser()

        try:
            config.read('AppConfig/config.ini')
            self.settings = self.as_dict(config)
            print ("Application settings loaded")

        except IOError as err:
            print ("Error: Can't find settings file or read data\n{}".format(err))

        return self.settings

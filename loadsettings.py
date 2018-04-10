class LoadSetting(object):

    import json

    def __init__(self, settings = dict()):
        self.settings = settings
    
    def get_Settings(self):

        with open("settings.json") as json_file:
             self.settings = self.json.load(json_file)

        return self.settings
        
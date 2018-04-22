"""[Summary]
This class manages all connections to the database
"""

class dbConnector(object):

    import sqlite3

    def __init__(self, db = 'cryptotrading.db'):
         self.conn = self.sqlite3.connect(db)

    def load_test_data(self, token = 'all'):
        return None
    
    def insert_coin_data(self, token):
        return None

    def insert_trade_data(self, parameter_list):
        pass


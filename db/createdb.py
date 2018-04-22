"""[Summary]
This class is used to delete and create a blank CryptoTrading database
"""
class CreateDB(object):

    import sqlite3 
    import pandas as pd

    dbname = None

    def __init__(self, dbname = 'cryptotrading.db'):
        self.dbname = dbname
    
    def _create_connector(self, dbname):
        """[summary]
        
        Arguments:
            dbname {[string]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        try:
            self.conn = self.sqlite3.connect(self.dbname)
            print(self.sqlite3.version)
        except IOError as e:
            print(e)
        return self.conn
    
    def _create_table(self, conn, sql_script):
        """[summary]
        
        Arguments:
            conn {[sqlite3.connect]} -- [description]
            sql_script {[str]} -- [description]
        """

        self.cur = conn.cursor()
        self.cur.execute(sql_script)

    def create_new_db(self):
        """[summary]
        """

        self.conn = self._create_connector(self.dbname)
        
        drop_coins_tbl = ("""
            DROP TABLE IF EXISTS Coins_tbl;
            """)

        create_coins_tbl =("""
            CREATE TABLE IF NOT EXISTS Coins_tbl (
                coin_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                coin TEXT,
                coin_name TEXT, 
                coin_symbol TEXT
            );
            """)
        
        drop_price_action_tbl=("""
            DROP TABLE IF EXISTS Price_action_tbl;
            """)
        
        create_price_action_tbl=("""
            CREATE TABLE IF NOT EXISTS Price_action_tbl (
                price_action_if INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                coin_id INTEGER,
                price_action_open REAL,
                price_action_close REAL,
                price_action_high REAL,
                price_action_low REAL,
                price_action_volume REAL,
                period_id INTEGER,
                source_id INTEGER
            );
            """)

        drop_sources_tbl=("""
            DROP TABLE IF EXISTS Sources_tbl;
            """)
        
        create_sources_tbl=("""
            CREATE TABLE IF NOT EXISTS Sources_tbl (
                source_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                source_name TEXT,
                source_type_id INTEGER
            ); 
            """)
        
        drop_periods_tbl=("""
            DROP TABLE IF EXISTS Periods_tbl;
            """)
        
        create_periods_tbl=("""
            CREATE TABLE IF NOT EXISTS Periods_tbl (
                period_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                period_name TEXT,
                period_seconds INTEGER
            );
            """)
        
        drop_sources_types_tbl=("""
            DROP TABLE IF EXISTS Source_types_tbl;
            """)
        
        create_sources_types_tbl=("""
            CREATE TABLE IF NOT EXISTS Source_types_tbl (
                source_type_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                source_type TEXT
            );
            """)

        self._create_table(self.conn, drop_coins_tbl)
        self._create_table(self.conn, drop_periods_tbl)
        self._create_table(self.conn, drop_price_action_tbl)
        self._create_table(self.conn, drop_sources_tbl)
        self._create_table(self.conn, drop_sources_types_tbl)

        self._create_table(self.conn, create_coins_tbl)
        self._create_table(self.conn, create_periods_tbl)
        self._create_table(self.conn, create_price_action_tbl)
        self._create_table(self.conn, create_sources_tbl)
        self._create_table(self.conn, create_sources_types_tbl)

        self.conn.close()

        self.add_base_data()

        print ('Database created, db name {}'.format(self.dbname))

    def delete_db(self, parameter_list):
        pass
    
    def add_base_data(self):

        self.conn = self._create_connector(self.dbname)
        
        df = self.pd.read_csv('coins.csv')
        df.to_sql('Coins_tbl', self.conn, if_exists='append', index=False)
        self.conn.close()
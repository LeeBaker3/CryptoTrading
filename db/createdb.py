'''
    Author: Lee Baker
    Date: 2018-05-02
    Version: 1.0
 '''

class CreateDB(object):
    """Used to create, load base data, and delete a database. Database schema is created using an
       external SQL file. Base data is held in external csv files. One csv file for each table in
       the database schema that requires base data.

       Attributes:
            db_name {string} -- Database name to be created or deleted.
            db_location {string} -- Directory of the database file.
            db_files_location {string} -- Directory where the files are held to create the database.
            sql_file_name {string} -- Filename of the SQL file used to create the database.
            csv_table_map_filename {string} -- Filename of the csv file that maps the base data CSV   
                files to the database tables.
    """

    import sqlite3 
    import pandas as pd
    import os
    import csv

    db_name = None 
    db_location = None 
    db_files_location = None 
    sql_file_name = None 
    csv_table_map_filename = None

    def __init__(self, db_name, db_location, db_files_location, sql_file_name='create_database.sql', 
        csv_table_map_filename='base_data_file_to_table_map.csv'):

        self.db_name = db_name
        self.db_location = db_location
        self.db_files_location = db_files_location
        self.sql_file_name = sql_file_name
        self.csv_table_map_filename = csv_table_map_filename
    
    def _create_connector(self):
        """Creates a sqlite database Connection object to be used by other class methods.

        Returns:
            sqlite Connection object -- Connection object used by other methods.
        """ 

        try:
            self.conn = self.sqlite3.connect(self.db_location + self.db_name)
            print(self.sqlite3.version)
            return self.conn
        except self.sqlite3.Error as e:
            print('Database connection failed: ', e.args[0])

    def _check_db_exists(self):
        """Check if a database exists with a matching name
        
        Returns:
            boolean -- Returns True if a database exists otherwise returns False.
        """
        # Hold boolean value which is the result of check if the database exists
        self.exists = None

        try:
            # Creates the correct string format so that when sqlite3 try's connect to 
            # a database it will only read and write (?mode=rw) it will not create.
            # sqlite query paramaters https://www.sqlite.org/uri.html#recognized_query_parameters
            self.db_file_uri = 'file:' + self.db_location + self.db_name + '?mode=rw'
            # Try's to connect to the database.
            self.conn = self.sqlite3.connect(self.db_file_uri, uri=True)
            # If exists, then the 'exists' variable is set to True.
            self.exists = True
            print('Database {} already exist.'.format(self.db_location + self.db_name)) 
        except:
            # If the database doesn't exist, then an error is raised and the 'exists' 
            # variable is set to False.
            self.exists = False
            print('Database {} does not exist.'.format(self.db_location + self.db_name)) 
        return self.exists

    def _insert_base_data_into_table_from_csv(self, filename, conn=None):
        """Inserts base data into databases tables from csv files.
        
        Arguments:
            filename {string} -- The filename of the csv file holding the mapping of 
                                 the files holding the base data to the database tables.
        
        Keyword Arguments:
            conn {sqlite Connection object} -- sqlite database connector to be used. (default: {None})
        """

        self.filename = self.db_files_location + filename
        self.conn = conn

        # Open and read csvfile.
        self.csvfile = open(self.filename, 'r')
        self.reader = self.csv.reader(self.csvfile)

        # Move read object past header line of csvfile.
        next(self.reader)

        # Read the csvfile file one row at a time.
        for self.row in self.reader:    
            try:
                # Extract the csv_filename and coresponding database table for the
                # base data to be loaded into. 
                self.csv_filename, self.tbl = self.row
                print('Inserted base data from {} into {}. '.format(self.db_files_location + self.csv_filename, self.tbl))
                # Load the base data from the csv file into a pandas dataframe then
                # use the pandas dataframe functionality to append the data to the 
                # database table.
                df = self.pd.read_csv(self.db_files_location + self.csv_filename)
                df.to_sql(self.tbl, self.conn, if_exists='append', index=False)
            except self.csv.Error as e:
                print('Error reading CSV file: ', e.args[0])
    
    def _execute_scripts_from_file(self, filename, conn):
        """Executes a SQL script held in separate file using a given Connection object.
        
        Arguments:
            filename {string} -- The filename of the SQL file to be executed. 
            conn {sqlite Connection object} -- sqlite database connector to be used.
        """

        self.filename = filename
        self.conn = conn

        # Open and read the file as a single buffer
        self.fd = open(self.filename, 'r')
        self.sql_file = self.fd.read()
        self.fd.close()

        # All SQL commands (split on ';')
        self.sql_commands = self.sql_file.split(';')

        # Execute every command from the input file
        for self.command in self.sql_commands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
            try:
                self.conn.execute(self.command)
            except self.sqlite3.Error as e:
                print('Command skipped: ', e.args[0])

    def create_new_db(self):
        """Create a new database using an external SQL file and inserts base data from external csv files.
        """

        # First checks to see if the database request already exists.
        if (self._check_db_exists() == False):
            # Creates a connection the sqlite DBMS.
            self.conn = self._create_connector()
            # Create the database schema using the external SQL file.
            self._execute_scripts_from_file(self.db_files_location + self.sql_file_name, self.conn)
            print ('Database {} created'.format(self.db_name))
            # Insert the base data into the tables.
            self._insert_base_data_into_table_from_csv(self.csv_table_map_filename, self.conn)
            self.conn.close()  
        else:
            print ('Database {} not created'.format(self.db_name))

    def delete_db(self):
        """Deletes database file.
        """
        
        try:
            self.os.remove(self.db_location + self.db_name)
            print ('Database {} deleted.'.format(self.db_name))
        except self.sqlite3.Error as e:
            print('Database deletion failed:', e.args[0])    
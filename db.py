import os
import sqlite3
from sqlite3 import Error
from sql import SELECT_QUERY
from logger import logger as logging

HOME_DIR = os.path.expanduser('~')
DB_LOCATION = f"{HOME_DIR}\\sensors_1.db"


class DataBase:
    """sqlite3 database class"""

    def __init__(self):
        """
        Initialize DB class object
        """
        logging.info("Initializing connection to database....")
        self.connection = sqlite3.connect(DB_LOCATION)
        self.cur = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            logging.error(str(exc_value), exc_info=True)
            self.connection.rollback()
        else:
            self.commit_changes()
        self.close_conn()

    def close_conn(self):
        """
        Close sqlite3 connection
        """
        logging.info("Closing database connection....")
        self.connection.close()

    def select_query(self, table, cols='*', condition='TRUE'):
        """
        Select rows from table
        @param table: table name
        @param cols: str -> name of columns (separated by , )
        @param condition: str -> where clause of SQL
        """
        logging.info(f"Selecting from table : {table}")
        query = SELECT_QUERY.format(table=table, cols=cols, condition=condition)
        self.execute_query(query=query)

        return self.cur.fetchall()

    def execute_query(self, query, raise_exception=True):
        """
        Execute a query
        @param query: str -> query to be executed
        @param raise_exception: bool -> true if required to raise exception
        """
        logging.info(f"Executing : {query}")
        return self.cur.execute(query)

    def commit_changes(self):
        """
        Commit changes to the DB
        """
        logging.info("Commiting changes to the database")
        self.connection.commit()

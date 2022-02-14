import sql
from db import DataBase
from logger import logger as logging


QUERY_MAPPER = {
    'sensor_status' : {
        'insert': sql.INSERT_INTO_SENSOR_STATUS_QUERY,
        'empty_table': sql.DELETE_FROM_QUERY
    },
    'sensor_report' : {
        'insert': sql.INSERT_INTO_SENSOR_REPORT_QUERY
    }
}

class QueryMapper:
    """
    Class to manage queries
    """
    def __init__(self, mapper=QUERY_MAPPER):
        self.query_mapper = mapper

    def _get_mapper_obj(self, key):
        return self.query_mapper.get(key)

    def _get_query(self, table, query_type) -> str:
        query_obj = self._get_mapper_obj(table)

        if not query_obj:
            raise Exception(f'Mapper for the table {table} not present')

        query = query_obj.get(query_type)

        if not query:
            raise Exception(f'{query_type.capitalize()} query for {table} not present')

        return query

    def get_insert_query(self, table):
        """
        Get insert query for the given table
        @param table: table name
        """
        return self._get_query(table, 'insert')

    def get_empty_table_query(self, table):
        """
        Get empty table query for the given table
        @param table: table name
        """
        return self._get_query(table, 'empty_table')

def prepare_required_data():
    """
    Create necessary tables and inserting data
    """
    with DataBase() as db:
        logging.info("Creating sensor_status table")
        db.execute_query(sql.CREATE_SENSOR_STATUS_TABLE_QUERY)

        status_data = select_from_table('sensor_status', 'status_id')

        if len(status_data) > 0:
            empty_table('sensor_status')

        logging.info("Inserting default data in sensor_status table")
        db.execute_query(sql.INSERT_SENSOR_STATUS_VALUE_QUERY)

        logging.info("Creating sensor_report table")
        db.execute_query(sql.CREATE_SENSOR_REPORT_TABLE_QUERY)

        logging.info("Data prepared")

def insert_data_in_table(table_name, data):
    """
    Insert data into particular table
    @param table_name: Name of the table
    @param data: dictionary of data
    """
    logging.info(f"Inserting {data} into table : {table_name}")
    query = QueryMapper().get_insert_query(table_name).format(**data)

    with DataBase() as db:
        db.execute_query(query)

def empty_table(table_name):
    """
    Empty/Truncate the table
    @param table_name: Name of the table
    """
    logging.info(f"Emptying the table : {table_name}")
    query = QueryMapper().get_empty_table_query(table_name).format(table=table_name)

    with DataBase() as db:
        db.execute_query(query)

def select_from_table(table_name, cols='*', condition='TRUE'):
    """
    Select rows from the table
    @param table_name: name of the table
    @param cols: str columns needed (separated by , )
    @param condition: str where clause of SQL
    """
    with DataBase() as db:
        return db.select_query(table_name, cols, condition)

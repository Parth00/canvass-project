CREATE_SENSOR_REPORT_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS sensor_report (
        id INTEGER PRIMARY KEY,
        deviceId TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        pressure REAL NOT NULL,
        status_id INTEGER NOT NULL,
        temperature REAL NOT NULL,
        FOREIGN KEY (status_id)
            REFERENCES sensor_status (status_id)
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
    );
'''

CREATE_SENSOR_STATUS_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS sensor_status (
        status_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
'''

INSERT_SENSOR_STATUS_VALUE_QUERY = '''
    INSERT INTO sensor_status (name)
    VALUES 
        ('ON'),
        ('OFF'),
        ('ACTIVE'),
        ('INACTIVE');
'''

INSERT_INTO_SENSOR_STATUS_QUERY = '''
    INSERT INTO sensor_status (name)
    VALUES ('{0}')
'''

SELECT_QUERY = '''
    SELECT {cols} from {table} WHERE {condition};
'''

INSERT_INTO_SENSOR_REPORT_QUERY = '''
    INSERT INTO sensor_report (deviceId, timestamp, pressure, status_id, temperature)
    VALUES ('{deviceId}', '{timestamp}', {pressure}, {status_id}, {temperature})
'''

DELETE_FROM_QUERY = '''
    DELETE FROM {table};
'''

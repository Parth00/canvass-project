import logging
import numpy as np
import pandas as pd
logging.getLogger('matplotlib').setLevel(logging.WARNING)
import matplotlib.pyplot as plt
from helper import select_from_table, insert_data_in_table, prepare_required_data


def prepare_data_for_server():
    """
    Create table and insert required data
    """
    prepare_required_data()

def store_sensor_data(sensor_data_json):
    """
    Store the sensor JSON data to the sensor_report table
    @param sensor_data_json: JSON data to feed
    """
    status = sensor_data_json['status']

    sensor_data_json.pop('status')

    query_condition = f"name='{status}' LIMIT 1"
    sensor_data_json['status_id'] = select_from_table('sensor_status', 'status_id', query_condition)[0][0]

    insert_data_in_table('sensor_report', sensor_data_json)

    return True

def get_histogram(device_id):
    """
    Get a histogram of the device device_id
    @param device_id: ID of the sensor
    """
    query_condition = f"deviceId='{device_id}'"
    device_report_data = select_from_table('sensor_report', cols='status_id', condition=query_condition)

    if len(device_report_data) == 0:
        logging.info(f"No record found for {device_id}")
        return False

    all_status = select_from_table('sensor_status', 'name')

    x_ticks = []

    for data in all_status:
        x_ticks.append(data[0])

    status_list = []

    for data in device_report_data:
        status_list.append(data[0])

    status = pd.Series(status_list)

    _, bins = np.histogram(status)

    status.hist(bins=bins)
    plt.title(f'Status of {device_id}')
    plt.xlabel('Status')
    plt.ylabel('Counts')
    plt.xlim(0,4)
    plt.xticks([1, 2, 3, 4], x_ticks)
    plt.ylim(0,10)
    plt.show()

    return True

from logger import logger as logging
from api import store_sensor_data, get_histogram, prepare_data_for_server
from xmlrpc.server import SimpleXMLRPCServer

prepare_data_for_server()

server = SimpleXMLRPCServer(('localhost', 8000))

server.register_function(store_sensor_data, 'store')
server.register_function(get_histogram, 'histogram')

logging.info("Listening to locathost:8000.....")

server.serve_forever()

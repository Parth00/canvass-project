# canvass-project
 Canvass interview project

A simple CLI based project to accept some sensor data in JSON, storing it in a SQLite DB and plots histogram from the data

# To Run
 1. Install all the packages from requirements.txt file. pip install -r requirements.txt
 2. Simply run server.py using python3 server.py command in the command prompt and wait for the server to initiate.
 3. Once running, run the simulator.py. It will generate random data after every 3 seconds and store in the DB
 4. It will post data 5 times and then get histogram of random device id

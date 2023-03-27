#!/usr/bin/env python3

import argparse
import os
import importlib
import subprocess

# Check if mysql-connector-python is installed
try:
    importlib.import_module('mysql.connector')
    # mysql-connector-python is already installed'
except ImportError:
    # Install mysql-connector-python using pip
    print('mysql-connector-python is not installed')
    subprocess.run(['pip', 'install', 'mysql-connector-python'])

import mysql.connector

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--host', required=True, help='database host')
parser.add_argument('--port', required=True, type=int, help='database port')
parser.add_argument('--database', required=True, help='database name')
args = parser.parse_args()

# Read username and password from environment variables
username = os.environ.get('PLANETSCALE_DB_USERNAME')
password = os.environ.get('PLANETSCALE_DB_PASSWORD')

# Connect to database
cnx = mysql.connector.connect(user=username, password=password,
                              host=args.host, port=args.port,
                              database=args.database)

# Do your database things
cursor = cnx.cursor()
cursor.execute('SHOW TABLES')
table_names = [table[0] for table in cursor]

for table_name in table_names:
    cursor.execute("SHOW CREATE TABLE {}".format(table_name))
    result = cursor.fetchone()
    print(result[1].replace('CREATE TABLE', 'CREATE TABLE IF NOT EXISTS') + ';\n')
    print()

# Bye!
cursor.close()
cnx.close()

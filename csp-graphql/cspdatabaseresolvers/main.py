import psycopg
import asyncio
import json
import typing
from pathlib import Path
import datetime

"""
Config is pulled from /home/csp/config.json

Example config
{
        "location":"nowhere",
        "database":"csp",
        "username":"noone",
        "password":"nothing",
        "port":"5432"
}
"""

config = json.loads(str(open(f'{Path.home()}/csp/config.json', 'r').read())) #load config
connectionstring = ''.join([f'{x}={y} ' for x, y in zip(config.keys(), config.values())]) #dict to key value list
connection = psycopg.connect(connectionstring)

def masterresolver(schema: str, table: str, field: str, value):
	command = f"SELECT * FROM csp.{table} where {field} = "
	if type(value) == str:	command = command + f"'{value}'"
	else:					command = command + f"{value}"
	query = connection.cursor().execute(command)
	return [{x.name: y
	           for x, y in zip(query.description, x)} for x in query.fetchall()]

def cspresolver(table: str, field: str, value):
	return masterresolver("csp", table, field, value)
import psycopg
import json
from pathlib import Path

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

config = json.loads(str(open(f'{Path.home()}/csp/config.json', 'r').read()))  # load config
connectionstring = ''.join([f'{x}={y} ' for x, y in zip(config.keys(), config.values())])  # dict to key value list
connection = psycopg.connect(connectionstring)


def masterresolver(schema: str, table: str, field: str, value):
	command = f"SELECT * FROM csp.{table} where {field} = %s"
	query = connection.cursor().execute(command, [value])
	return [{x.name: y for x, y in zip(query.description, x)} for x in query.fetchall()]


def cspresolver(table: str, field: str, value):
	return masterresolver("csp", table, field, value)
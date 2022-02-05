import psycopg
import asyncio
import json
import typing
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

config = json.loads(str(open(f'{Path.home()}/csp/config.json', 'r').read())) #load config
connectionstring = ''.join([f'{x}={y} ' for x, y in zip(config.keys(), config.values())]) #dict to key value list
connection = psycopg.connect(connectionstring)


def resolveUser(username: str):
	query = connection.cursor().execute(f"SELECT * FROM csp.USER where username = {username}")
	return {x.name: y for x, y in zip(query.description, query.fetchone())}
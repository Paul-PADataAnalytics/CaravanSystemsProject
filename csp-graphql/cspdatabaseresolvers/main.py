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

config = json.loads(str(open(f'{Path.home()}/csp/config.json', 'r').read()))
connectionstring = f"dbname={config['database']} user={config['username']} password={config['username']}"
connection = psycopg.connect(connectionstring)


def resolveUser(username: str):
	output = connection.cursor().execute(f"SELECT * FROM csp.USER where username = {username}").fetchone()
	return {"username": username, "passwordhash": "fdasfdsaf"}
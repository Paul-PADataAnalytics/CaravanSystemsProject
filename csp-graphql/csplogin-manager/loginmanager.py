from cspdatabaseresolvers import main as dr
from cspgraphql import schema as dataschema


def login(username: str, password: str) -> dataschema.credentials:
    user = dr.cspresolver("user", "username", username)
    dr.user(user)
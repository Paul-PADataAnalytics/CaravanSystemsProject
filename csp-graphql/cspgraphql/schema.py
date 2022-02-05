import strawberry
import typing
import datetime
import asyncio
from cspdatabaseresolvers import main as cspdatabaseresolvers

@strawberry.type
class User:
    username: str
    passwordhash: str


@strawberry.type
class LocationRating:
    overallrating: int
    facilities: int
    location: int
    journey: int
    scenery: int


@strawberry.type
class Location:
    lat: str
    lng: str
    name: str
    rating: [LocationRating]


@strawberry.type
class Trip:
    startdate: datetime.date
    enddate: datetime.date
    booker: [User]
    location: [Location]


async def user(self) -> User:
    output = cspdatabaseresolvers.resolveUser(username = "Patrick")
    print(output)
    return User(username = output["username"], passwordhash = output["passwordhash"])


@strawberry.type
class Query:
    user: str = strawberry.field(resolver=user)


schema = strawberry.Schema(query=Query)
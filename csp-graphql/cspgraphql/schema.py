import strawberry
import typing
import datetime
import asyncio
from cspdatabaseresolvers import main as db


@strawberry.type
class User:
    username: str
    passwordhash: str
    created: datetime.date
    updated: datetime.date


@strawberry.type
class LocationRating:
    overallrating: int
    facilities: int
    journey: int
    scenery: int
    created: datetime.date
    updated: datetime.date


@strawberry.type
class Location:
    lat: str
    lng: str
    name: str
    rating: [LocationRating]
    created: datetime.date
    updated: datetime.date


@strawberry.type
class Trip:
    startdate: datetime.date
    enddate: datetime.date
    booker: [User]
    location: [Location]
    created: datetime.date
    updated: datetime.date


User.trips: [Trip]
    

async def user(self, username) -> User:
    output = db.cspresolver("user", "username",username)
    return User(**output)


@strawberry.type
class Query:
    user: str = strawberry.field(resolver=user)


schema = strawberry.Schema(query=Query)
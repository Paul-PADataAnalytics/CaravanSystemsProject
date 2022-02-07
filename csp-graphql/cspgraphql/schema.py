import strawberry
from strawberry.types import Info
import typing
import datetime
import asyncio
from cspdatabaseresolvers import main as db


@strawberry.type
class LocationRating:
    id: int
    overallrating: int
    locationid: int
    facilitiesrating: int
    locationrating: int
    journeyrating: int
    sceneryrating: int
    comment: str = 'N'
    created: datetime.date = '2001-01-01'
    updated: datetime.date = '2001-01-01'
    deleted: str = 'N'


@strawberry.type
class Location:
    id: int = 0
    lat: str = '0'
    lng: str = '0'
    name: str = 'Unknown Location'
    rating: (LocationRating) = None
    created: datetime.date = '2001-01-01'
    updated: datetime.date = '2001-01-01'
    deleted: str = 'N'


@strawberry.type
class Trip:
    id: int =0
    startdate: datetime.date = '2001-01-01'
    enddate: datetime.date = '2001-01-01'
    bookinguserid: int = 0
    triplocationid: int = 0
    location: (Location) = None
    created: datetime.date = 0
    updated: datetime.date = 0
    deleted: str = 'N'


@strawberry.type
class User:
    id: int =0
    username: str = 'N'
    passwordhash: str = 'N'
    created: datetime.date = '2001-01-01'
    updated: datetime.date = '2001-01-01'
    deleted: str = 'N'
    trips: typing.List[Trip] = None


async def getUser(username: str) -> typing.List[User]:
    fetch = db.cspresolver("user", "username", username)
    for x in fetch:
        x["trips"] = getTrips(userid=x["id"])
    return [User(**fetched) for fetched in fetch]


async def getTrips(tripid: int = 0, userid: str = "", startdate: str = "") -> typing.List[Trip]:
    if tripid != 0:     fetch = db.cspresolver("trip", "id", tripid)
    if userid != "":    fetch = db.cspresolver("trip", "bookinguserid", userid)
    if startdate != "": fetch = db.cspresolver("trip", "startdate", startdate)
    # for x in fetch:
    #     x["trips"] = getLocations(id = x["triplocationid"])
    return [Trip(**fetched) for fetched in fetch]


async def getLocations(id: int = 0) -> typing.List[Location()]:
    fetch = db.cspresolver("location", "id", id)
    # for x in fetch:
    #     fetch["rating"] = db.cspresolver("locationrating", "locationid", id)
    return [Location(**fetched) for fetched in fetch]

@strawberry.type
class Query:
    @strawberry.field
    def user(self, info: Info, username: strawberry.ID) -> typing.List[User]:
        return getUser(username=username)
    
    @strawberry.field
    def trip(self, info, userid: strawberry.ID =0, triplocationid: int = 0, startdate: str = "") -> typing.List[Trip]:
        return getTrips(tripid=triplocationid, userid=userid, startdate=startdate)
        
    # @strawberry.field
    # def location(self, info, tripid: strawberry.ID) -> Location:
    #     fetch = db.cspresolver("location", "id", tripid)
    #     print(self.locationrating(locationid = fetch["id"]))
    #     fetch["rating"] = self.locationrating(locationid = fetch["id"])
    #     return Location(**fetch)

    # @strawberry.field
    # def locationrating(self, info, locationid: strawberry.ID) -> LocationRating:
    #     print(info.selected_fields)
    #     fetch = db.cspresolver("locationrating", "id", locationid)
    #     return [LocationRating(**x) for x in fetch]


schema = strawberry.Schema(query=Query)
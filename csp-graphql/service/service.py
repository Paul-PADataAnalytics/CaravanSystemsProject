import strawberry
import typing
import datetime


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


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)

schema = strawberry.Schema(query=Query)
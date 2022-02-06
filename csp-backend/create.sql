CREATE DATABASE csp;
--CREATE DATABASE csp;
CREATE SCHEMA csp;
CREATE TABLE csp.user(
    id SERIAL,
    username TEXT,
    passwordhash TEXT,
    created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted TEXT NOT NULL DEFAULT 'N'
);
CREATE TABLE csp.locationrating(
    id SERIAL,
    locationid int,
    overallrating INT,
    facilitiesrating INT,
    locationrating INT,
    journeyrating INT,
    sceneryrating INT,
    comment text,
    created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted TEXT NOT NULL DEFAULT 'N'
);
CREATE TABLE csp.location(
    id SERIAL,
    lat TEXT,
    lng TEXT,
    name TEXT NOT NULL DEFAULT 'UNKNOWN LOCATION',
    created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted TEXT NOT NULL DEFAULT 'N'
);
CREATE TABLE csp.trip(
    id SERIAL,
    startdate DATE,
    enddate DATE,
    bookinguserid int,
    triplocationid int,
    created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted TEXT NOT NULL DEFAULT 'N'
);
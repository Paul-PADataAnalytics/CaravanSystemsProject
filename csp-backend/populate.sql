INSERT INTO csp.user (id,username,passwordhash,created,updated,deleted)
VALUES (default,'test','123',default,default,default);

INSERT INTO csp.location(id,lat,lng,name,created,updated,deleted)
VALUES (default,'0','0','test location',default,default,default);

INSERT INTO csp.trip(id,startdate,enddate,bookinguserid,triplocationid,created,updated,deleted)
VALUES (default, '2001-01-01', '2001-01-10', 1, 1,default,default,default);

INSERT INTO csp.locationrating(id,locationid,overallrating,facilitiesrating,locationrating,journeyrating,sceneryrating,comment,created,updated,deleted)
VALUES (default,1,5,4,3,2,1,'test',default,default,default);
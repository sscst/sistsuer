DROP TABLE IF EXISTS advise;
CREATE TABLE advise(
       ad varchar(2000) not null
)default charset=utf8;

DROP TABLE IF EXISTS story;
CREATE TABLE story(
       uid varchar(200) not null,
       status varchar(20) not null,
       name_status varchar(20) not null,
       past_content varchar(1000) not null
)default charset=utf8;


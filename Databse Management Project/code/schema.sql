drop table if exists inventory CASCADE;
drop table if exists wine CASCADE;
drop table if exists charcuterie CASCADE;
drop table if exists orders CASCADE;
drop table if exists region CASCADE;
drop table if exists owner CASCADE;
drop table if exists contents CASCADE;
drop table if exists stocked CASCADE;
drop table if exists consists CASCADE;
drop table if exists make CASCADE;
drop table if exists winery_owns CASCADE;
drop table if exists account_has CASCADE;
drop table if exists customer_belong CASCADE;
drop table if exists place CASCADE;


create table inventory (
invid varchar(8) primary key,
bottlecount integer not null,
type varchar(50) not null
);

create table wine (
wineid integer primary key,
name varchar(100) not null,
age integer not null,
type varchar(30) not null,
price integer not null,
alcohol_percentage integer not null,
popularity integer not null
);

create table charcuterie (
boardid varchar(8) primary key,
name varchar(50) unique not null
);

create table orders (
orderid varchar(8) primary key,
odate date not null,
cost integer not null
);

create table region (
regionid varchar(4) primary key,
country varchar(30) unique not null
);

create table owner(
owner_ssn varchar(16) not null,
winery varchar(100) not null,
license varchar(24),
contact bigint not null,
primary key (license)
);

create table contents(
boardid varchar(8),
content varchar(128),
category varchar(16),
primary key(boardid, content, category)
);

create table stocked (
wineid integer,
invid varchar(8),
primary key (wineid, invid),
foreign key (wineid) references wine(wineid),
foreign key (invid) references inventory(invid)
);

create table consists (
orderid varchar(8),
wineid integer,
boardid varchar(8),
primary key(wineid, boardid, orderid),
foreign key (wineid) references wine(wineid),
foreign key (boardid) references charcuterie(boardid),
foreign key (orderid) references orders(orderid)
);

create table winery_owns (
wineryid integer primary key,
name varchar(50) not null,
capacity integer not null,
area integer not null,
address varchar(124) not null,
license varchar(24),
foreign key(license) references owner(license)
);

create table make(
wineid integer,
wineryid integer,
primary key(wineid, wineryid),
foreign key (wineid) references wine(wineid),
foreign key (wineryid) references winery_owns(wineryid)
);


create table account_has(
ssn varchar(16) primary key,
name varchar(24) not null,
username varchar(24) unique not null,
dob date not null,
contact bigint not null,
password varchar(100) not null,
email varchar(100) unique not null,
license varchar(24) unique,
foreign key(license) references owner(license)
);

create table customer_belong (
cid varchar(24) primary key,
name varchar(24) not null,
contact bigint not null,
address varchar(100) not null,
ssn varchar(16) not null,
foreign key(ssn) references account_has(ssn)
);

create table place (
orderid varchar(8),
cid varchar(24),
primary key(orderid, cid),
foreign key (orderid) references orders(orderid),
foreign key (cid) references customer_belong(cid)
);

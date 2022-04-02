# Online Winery Database Management System
# Upasana Mehta - um2024
# Pranav Bawiskar - pb2581

create table Inventory (
invid integer primary key,
bottlecount integer not null,
type varchar(24) 
);

create table Wine (
wineid integer primary key,
name varchar(24) not null,
age integer,
type varchar(24) not null,
alcohol% integer not null
);

create table stocked(
wineid integer,
invid integer,
primary key (wineid, invid),
foreign key (wineid) references Wine(wineid),
foreign key (invid) references Inventory(invid)
);

create table Charcuterie_Board (
name varchar(24) primary key,
wineid integer,
cheese varchar(24),
crackers varchar(24),
meat varchar(24),
berries varchar(24),
dryfruits varchar(24),
olives varchar(24),
);

create table Order (
orderid integer primary key,
odate date not null,
cost not null
);

create table consist (
wineid integer,
name varchar(24),
orderid integer,
primary key(wineid, name, orderid),
foreign key (wineid) references Wine(wineid),
foreign key (name) references Charcuterie_Board(name),
foreign key (orderid) references Order(orderid)
);

create table make(
wineid integer,
wineryid integer,
primary key(wineid, wineryid),
foreign key (wineid) references Wine(wineid),
foreign key (wineryid) references Winery_owns(wineryid)
);

create table Winery_owns (
wineryid integer primary key,
name varchar(24),
capacity integer,
address varchar(124),
area integer,
license integer unique,
foreign key(license) references Owner(license)
);

create table Region (
regionid integer primary key,
country varchar(24)
);

create table situated (
wineryid integer,
regionid integer,
primary key (wineryid, regionid),
foreign key (wineryid) references Winery_owns(wineryid), 
foreign key (regionid) references Region(regionid)
);

create table Owner(
ssn integer,
winery varchar(24),
license varchar(24) primary key,
contact integer,
);

create table Account_has(
ssn integer primary key,
name varchar(24),
contact integer,
username varchar(24),
password varchar(24),
email varchar(24),
dob date,
license varchar(24) not null,
foreign key (license) references Owner(license)
);

create table customer_belong (
cid integer primary key,
name varchar(24),
contact integer,
address varchar(24),
ssn integer unique not null,
foreign key(ssn) references Account_has(ssn)
);

create table place (
orderid integer,
cid integer,
primary key(orderid, cid),
foreign key (orderid) references Order(orderid),
foreign key (cid) references customer_belong(cid)
);

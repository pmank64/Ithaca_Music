create table Artist(
  id integer primary key autoincrement,
  firstname varchar(64) not null,
  lastname varchar(64) not null,
  hometown varchar(128)
);

create table Venue(
  id integer primary key autoincrement,
  name varchar(64) not null,
  street varchar(128),
  city varchar(128),
  state varchar(64),
  zipcode float
);

create table ArtistToVenue(
  id integer primary key autoincrement,
  artistID integer not null,
  venueID integer not null,
  foreign key (artistID) references Artist(id),
  foreign key (venueID) references Venue(id)
);

create table Event(
  id integer primary key autoincrement,
  name varchar(128),
  venueID integer not null,
  date varchar(64),
  foreign key (venueID) references Venue(id)
);

create table ArtistToEvent(
  id integer primary key autoincrement,
  artistID integer not null,
  eventID integer not null,
  foreign key (artistID) references Artist(id),
  foreign key (eventID) references Event(id)
);

create table Genre(
  id integer primary key autoincrement,
  name varchar(128)
);

create table GenreToArtist(
  id integer primary key autoincrement,
  genreID integer not null,
  artistID integer not null,
  foreign key (genreID) references Genre(id),
  foreign key (artistID) references Artist(id)
);
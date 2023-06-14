
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, delete
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# #Create the Database
engine = create_engine("sqlite:///database.db", echo=True)
# #Creates a session.
Session = sessionmaker(bind=engine)
session = Session()

#Create a class for an Account.
class User(Base, UserMixin):
    __tablename__ = "users"
    
    Username = Column("UserName", String(80), primary_key=True, nullable=False)
    Password = Column("Password", String(30), nullable=False)
    Email = Column("Email", String, unique=True, nullable=False)
    Mana = Column("Mana", Integer)
    # Posts = Column("Posts", Integer)
    # Comments = db.Column("Comments", db.Integer)
    Awards = Column("Awards", Integer)
    # AccountType = db.Column("AccountType", db.String)
    
    def __init__(self, Username, Password, Email, Mana, Awards):
        self.Username = Username
        self.Password = Password
        self.Email = Email
        self.Mana = Mana
        # self.Posts = Posts
        # self.Comments = Comments
        self.Awards = Awards
        # self.AccountType = AccountType

    def __repr__(self):
        return f"({self.Username}) ({self.Password}) ({self.Email}) ({self.Mana}) ({self.Awards})"
    
    def get_id(self):
        return str(self.Username)
    
    # children: Mapped[List["Child"]] = relationship(back_populates="parent")


class World(User):
    __tablename__ = "Worlds"
    
    # id: Mapped[int] = mapped_column(primary=True)
    # parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    # parent: Mapped["Parent"] = relationship(back_populates="children")
    
    WorldUser = Column("User", ForeignKey('users.Username'))
    WorldName = Column("WorldName", String(50), primary_key=True, nullable=False)
    WorldDescription = Column("WorldDescription", String, nullable=False)

    def __init__ (self, WorldUser, WorldName, WorldDescription):
        self.WorldUser = WorldUser
        self.WorldName = WorldName
        self.WorldDescription = WorldDescription
    
    def __repr__(self):
        return f"({self.WorldUser}) ({self.WorldName}) ({self.WorldDescription})"
    
    def get_id(self):
        return str(self.Username)


class History(World):
    __tablename__ = "History"
    HistoryUser = Column("HistoryUser", ForeignKey('users.Username'))
    HistoryTitle = Column("HistoryTitle", String, nullable=False)
    HistoryDescription = Column("HistoryDescription", String, nullable=False)

    def __init__ (self, HistoryUser, HistoryName, HistoryDescription):
        self.HistoryUser = HistoryUser
        self.HistoryName = HistoryName
        self.HistoryDescription = HistoryDescription
        
    def __repr__(self):
        return f"({self.HistoryUser}) ({self.HistoryName}) ({self.HistoryDescription})"

class Culture(World):
    __tablename__ = "Cultures"

    CultureUser = Column("CultureUser", ForeignKey('users.Username'))
    CultureTitle = Column("CultureTitle", String, nullable=False)
    CultureDescription = Column("CultureDescription", String, nullable=False)

    def __init__ (self, CultureUser, CultureName, CultureDescription):
        self.CultureUser = CultureUser
        self.CultureName = CultureName
        self.CultureDescription = CultureDescription

    def __repr__(self):
        return f"({self.CultureUser}) ({self.CultureName}) ({self.CultureDescription})"


class Religion(World):
    __tablename__ = "Religions"

    ReligionUser = Column("ReligionUser", ForeignKey('users.Username'))
    ReligionTitle = Column("ReligionTitle", String, nullable=False)
    ReligionDescription = Column("ReligionDescription", String, nullable=False)

    def __init__ (self, ReligionUser, ReligionName, ReligionDescription):
        self.ReligionUser = ReligionUser
        self.ReligionName = ReligionName
        self.ReligionDescription = ReligionDescription

    def __repr__(self):
        return f"({self.ReligionUser}) ({self.ReligionName}) ({self.ReligionDescription})"

class Species(World):
    __tablename__ = "Species"

    SpeciesUser = Column("SpeciesUser", ForeignKey('users.Username'))
    SpeciesTitle = Column("SpeciesTitle", String, nullable=False)
    SpeciesDescription = Column("SpeciesDescription", String, nullable=False)

    def __init__ (self, SpeciesUser, SpeciesName, SpeciesDescription):
        self.SpeciesUser = SpeciesUser
        self.SpeciesName = SpeciesName
        self.SpeciesDescription = SpeciesDescription

    def __repr__(self):
        return f"({self.SpeciesUser}) ({self.SpeciesName}) ({self.SpeciesDescription})"

class Timeline(World):
    __tablename__ = "Timelines"

    TimelineUser = Column("TimelineUser", ForeignKey('users.Username'))
    TimelineTitle = Column("TimelineTitle", String, nullable=False)
    TimelineEntry = Column("TimelineEntry", String, nullable=False)

    def __init__ (self, TimelineUser, TimelineName, TimelineDescription):
        self.TimelineUser = TimelineUser
        self.TimelineName = TimelineName
        self.TimelineDescription = TimelineDescription

    def __repr__(self):
        return f"({self.TimelineUser}) ({self.TimelineName}) ({self.TimelineDescription})"


# #Uses the engine to create the tables for data.
Base.metadata.create_all(engine)
# ({self.Mana}) ({self.Posts}) ({self.Comments}) ({self.Awards}) ({self.AccountType})

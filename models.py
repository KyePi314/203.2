from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, delete, LargeBinary, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from datetime import date


Base = declarative_base()

# #Create the Database
engine = create_engine("sqlite:///database.db", echo=True)
# #Creates a session.
Session = sessionmaker(bind=engine)
session = Session()

#Create a class for an Account.
class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer,  autoincrement=True)
    UserName = Column("UserName", String(80), primary_key=True, nullable=False)
    Password = Column("Password", String(30), nullable=False)
    Email = Column("Email", String, unique=True, nullable=False)
    Mana = Column("Mana", Integer)
    Posts = Column("Posts", Integer)
    Comments = Column("Comments", Integer)
    Awards = Column("Awards", Integer)
    AccountType = Column("AccountType", String)
    

    def __init__(self, id, UserName, Password, Email, Mana, Awards, Posts, Comments, AccountType):
        self.id = id
        self.UserName = UserName
        self.Password = Password
        self.Email = Email
        self.Mana = Mana
        self.Posts = Posts
        self.Comments = Comments
        self.Awards = Awards
        self.AccountType = AccountType

    def __repr__(self):
        return f"({self.id})({self.UserName}) ({self.Password}) ({self.Email}) ({self.Mana}) ({self.Awards}) ({self.Comments}) ({self.AccountType}) ({self.Posts})"
    
    def get_id(self):
        return str(self.UserName)
    

# Uses the engine to create the tables for data.

    # children: Mapped[List["Child"]] = relationship(back_populates="parent")


class World(Base):
    __tablename__ = "Worlds"
    
    # id: Mapped[int] = mapped_column(primary=True)
    # parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    # parent: Mapped["Parent"] = relationship(back_populates="children")
    user = relationship('User')
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)    
    UserName = Column(String, nullable=False)
    WorldName = Column("WorldName", String(50), nullable=False)
    WorldDescription = Column("WorldDescription", String, nullable=False, primary_key=True)

    def __init__ (self,id, UserName, WorldName, WorldDescription):
        self.id = id
        self.UserName = UserName
        self.WorldName = WorldName
        self.WorldDescription = WorldDescription
    
    def __repr__(self):
        return f"({self.UserName}) ({self.WorldName}) ({self.WorldDescription})"
    
    # def get_id(self):
    #     return str(self.Username)


class History(Base):
    __tablename__ = "History"
    user = relationship('User')
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    UserName = Column(String, nullable=False)
    WorldName = Column("WorldName", String(50))
    HistoryTitle = Column("HistoryTitle", String, nullable=False, primary_key=True)
    HistoryDescription = Column("HistoryDescription", String, nullable=False)

    def __init__ (self,id, UserName, WorldName, HistoryTitle, HistoryDescription):
        self.id = id
        self.UserName = UserName
        self.WorldName = WorldName
        self.HistoryTitle = HistoryTitle
        self.HistoryDescription = HistoryDescription
        
    def __repr__(self):
        return f"({self.UserName}) ({self.WorldName}) ({self.HistoryTitle}) ({self.HistoryDescription})"

class Culture(Base):
    __tablename__ = "Cultures"
    user = relationship('User')
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    UserName = Column(String, nullable=False)
    WorldName = Column("WorldName", String(50))
    CultureTitle = Column("CultureTitle", String, nullable=False, primary_key=True)
    CultureDescription = Column("CultureDescription", String, nullable=False)

    def __init__ (self,id, UserName, WorldName, CultureTitle, CultureDescription):
        self.id = id
        self.UserName = UserName
        self.WorldName = WorldName
        self.CultureTitle = CultureTitle
        self.CultureDescription = CultureDescription

    def __repr__(self):
        return f"({self.UserName}) ({self.WorldName}) ({self.CultureTitle}) ({self.CultureDescription})"


class Religion(Base):
    __tablename__ = "Religions"
    user = relationship('User')
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    UserName = Column(String, nullable=False)
    WorldName = Column("WorldName", String(50))
    ReligionTitle = Column("ReligionTitle", String, nullable=False, primary_key=True)
    ReligionDescription = Column("ReligionDescription", String, nullable=False)

    def __init__ (self, id,UserName, WorldName, ReligionTitle, ReligionDescription):
        self.id = id
        self.UserName = UserName
        self.WorldName = WorldName
        self.ReligionTitle = ReligionTitle
        self.ReligionDescription = ReligionDescription

    def __repr__(self):
        return f"({self.UserName}) ({self.WorldName}) ({self.ReligionTitle}) ({self.ReligionDescription})"

class Species(Base):
    __tablename__ = "Species"
    user = relationship('User')
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    UserName = Column(String, nullable=False)
    WorldName = Column("WorldName", String(50))
    SpeciesTitle = Column("SpeciesTitle", String, nullable=False, primary_key=True)
    SpeciesDescription = Column("SpeciesDescription", String, nullable=False)

    def __init__ (self,id, UserName, WorldName, SpeciesTitle, SpeciesDescription):
        self.id = id
        self.UserName = UserName
        self.WorldName = WorldName
        self.SpeciesTitle = SpeciesTitle
        self.SpeciesDescription = SpeciesDescription

    def __repr__(self):
        return f"({self.UserName}) ({self.WorldName}) ({self.SpeciesTitle}) ({self.SpeciesDescription})"

class Timeline(Base):
    __tablename__ = "Timelines"
    user = relationship('User')
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    UserName = Column(String, nullable=False)
    WorldName = Column("WorldName", String(50))
    TimelineTitle = Column("TimelineTitle", String, nullable=False, primary_key=True)
    TimelineEntry = Column("TimelineEntry", String, nullable=False)

    def __init__ (self,id, UserName, WorldName, TimelineTitle, TimelineEntry):
        self.id = id
        self.UserName = UserName
        self.WorldName = WorldName
        self.TimelineTitle = TimelineTitle
        self.TimelineEntry = TimelineEntry

    def __repr__(self):
        return f"({self.UserName}) ({self.WorldName}) ({self.TimelineTitle}) ({self.TimelineEntry})"

class Img(Base):
    __tablename__ = "Images"
    user = relationship('User')
    id = Column(Integer, ForeignKey("users.id"), primary_key=True, autoincrement=True)
    worldName = Column(String, nullable=False)
    UserName = Column(String, nullable=False)
    data = Column(LargeBinary, nullable=False)
    rendered_data = Column(Text, nullable=False)

    def __init__(self, id, worldName, UserName, data, rendered_data):
        self.id = id
        self.worldName = worldName
        self.UserName = UserName
        self.data = data
        self.rendered_data = rendered_data

    def __repr__(self):
        return f"({self.id}) ({self.worldName}) ({self.UserName}) ({self.data}) ({self.rendered_data})"

currentdate = date.today()
time = datetime.now()

# Fix later:

# class Issue(Base):
#     __tablename__ = "Issues"
#     id = Column(Integer, ForeignKey("users.id"), primary_key=True, autoincrement=True)
#     UserName = Column("UserName", String, nullable=False)
#     IssueInfo = Column("IssueInfo", String, nullable=False)
#     Date = Column("Date", currentdate, String)
#     Time = Column("Time", time, String)

#     def __init__(self, id, UserName, IssueInfo, date, time):
#         self.id = id
#         self.UserName = UserName
#         self.IssueInfo = IssueInfo
#         self.Date = date
#         self.Time = time

#     def __repr__(self):
#         return f"({self.id}) ({self.UserName}) ({self.IssueInfo}) ({self.Date}) ({self.Time})"


# #Uses the engine to create the tables for data.

# engine = create_engine("sqlite:///database.db", echo=True)

#Create the classs for the Posts.
class Post(Base):
    __tablename__ = "posts"
    user = relationship('User')
    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, autoincrement=True)
    UserName = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    posted_date = Column(DateTime, default=datetime.now)
    Likes = Column(Integer, default=0)
    ## Relationship with the likes and comments tables
    # likes = relationship("Likes", backref="post") 
    comments = relationship("Comment", backref="post", cascade="all, delete-orphan")

    def __init__(self, id, user_id, UserName, title, content, posted_date, Likes):
        self.id = id
        self.user_id = id
        self.UserName = UserName
        self.title = title
        self.content = content
        self.posted_date = posted_date
        self.Likes = Likes
    
    def __repr__(self):
        return f"({self.user_id}) ({self.title}) ({self.UserName}) ({self.content}) ({self.posted_date})"

# class Likes(Base):
#     __tablename__ = 'likes'
#     user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
#     post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
#     user = relationship('User', backref='likes')
#     post = relationship('Post', backref='likes')

#     def __init__(self, user_id, post_id):
#         self.user_id = user_id
#         self.post_id = post_id


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    author = Column(String, nullable=False)
    content = Column(String, nullable=False)

    def __init__(self, post_id, author, content):
        self.post_id = post_id
        self.author = author
        self.content = content
    
    def __repr__(self):
        return f"Comment(id={self.id}, post_id={self.post_id}, author='{self.author}', content='{self.content}')"

Base.metadata.create_all(engine)

# # Delete Tables
# # User.__table__.drop(bind=engine)
# # World.__table__.drop(bind=engine)
# # History.__table__.drop(bind=engine)
# # Culture.__table__.drop(bind=engine)
# # Species.__table__.drop(bind=engine)
# # Religion.__table__.drop(bind=engine)
# # Timeline.__table__.drop(bind=engine)
# # # Commit changes.
# Comment.__table__.drop(bind=engine)
# Post.__table__.drop(bind=engine)
# session.commit()
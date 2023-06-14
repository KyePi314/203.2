
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
    Password = Column("Password", String(300), nullable=False)
    Email = Column("Email", String, unique=True, nullable=False)
    Mana = Column("Mana", Integer)
    Posts = Column("Posts", Integer)
    Comments = Column("Comments", Integer)
    Awards = Column("Awards", Integer)
    AccountType = Column("AccountType", String)
    
    def __init__(self, Username, Password, Email, Mana, Awards, Posts, Comments, AccountType):
        self.Username = Username
        self.Password = Password
        self.Email = Email
        self.Mana = Mana
        self.Posts = Posts
        self.Comments = Comments
        self.Awards = Awards
        self.AccountType = AccountType

    def __repr__(self):
        return f"({self.Username}) ({self.Password}) ({self.Email}) ({self.Mana}) ({self.Awards}) ({self.Comments}) ({self.AccountType}) ({self.Posts})"
    
    def get_id(self):
        return str(self.Username)
    
# Uses the engine to create the tables for data.
Base.metadata.create_all(engine)

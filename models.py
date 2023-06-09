
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy


Base = declarative_base()
# #Create the Database
engine = create_engine("sqlite:///database.db", echo=True)
# #Create the Database
# #Uses the engine to create the tables for data.
Base.metadata.create_all(bind=engine)
# #Creates a session.
Session = sessionmaker(bind=engine)
session = Session()
db = SQLAlchemy()


#Create a class for an Account.
class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement = True)
    Username = Column("UserName", String(80))
    Password = Column("Password", String(300))
    Email = Column("Email", String, unique=True)
    
    # Mana = db.Column("Mana", db.Integer)
    # Posts = db.Column("Posts", db.Integer)
    # Comments = db.Column("Comments", db.Integer)
    # Awards = db.Column("Awards", db.Integer)
    # AccountType = db.Column("AccountType", db.String)
    
    def __init__(self, Username, Password, Email):
        self.Username = Username
        self.Password = generate_password_hash(Password)
        self.Email = Email
        # self.Mana = Mana
        # self.Posts = Posts
        # self.Comments = Comments
        # self.Awards = Awards
        # self.AccountType = AccountType

    def is_active(self):
       return True
    
    def __repr__(self):
        return f"({self.Username}) ({self.Password}) ({self.Email})"
    
    def verify_password(self, pwd):
        return check_password_hash(self.Password, pwd)

# ({self.Mana}) ({self.Posts}) ({self.Comments}) ({self.Awards}) ({self.AccountType})


sqlalchemy.inspect(engine).has_table("users")
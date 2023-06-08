## The init file ##
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

#Create a class for an Account.
class User(Base):
    __tablename__ = "users"

    Username = Column("UserName", String, primary_key=True)
    Password = Column("Password", String)
    Email = Column("Email", String)
    Mana = Column("Mana", Integer)
    Posts = Column("Posts", Integer)
    Comments = Column("Comments", Integer)
    Awards = Column("Awards", Integer)
    AccountType = Column("AccountType", String)
    
    def __init__(self, UserName, Password, Email, Mana, Posts, Comments, Awards, AccountType):
        self.Username = UserName
        self.Password = Password
        self.Email = Email
        self.Mana = Mana
        self.Posts = Posts
        self.Comments = Comments
        self.Awards = Awards
        self.AccountType = AccountType

    def __repr__(self):
        return f"({self.Username}) ({self.Password}) ({self.Email}) ({self.Mana}) ({self.Posts}) ({self.Comments}) ({self.Awards}) ({self.AccountType})"

#Create the Database
engine = create_engine("sqlite:///database.db", echo=True)
#Uses the engine to create the tables for data.
Base.metadata.create_all(bind=engine)
#Creates a session.
Session = sessionmaker(bind=engine)
session = Session()

User1 = User("KingdomCome", "Empire123", "janelynn@email.com", 12, 1, 2, 0, "Celestial")

User2 = User("Rambunctious51", "George12", "yeyeye23@email.com", 113, 3, 14, 2, "Classic")

User3 = User("firebrand", "password", "fieryone@email.com", 44, 7, 4, 1, "Classic")

session.add(User1)
session.add(User2)
session.add(User3)

session.commit()

# temp database until proper one hooked up
database = {'Jane':'123',
            'Dean':'666',
            'Ollie':'999'}

# Temporary database dictionary for storing information for worlds
database2 = {"Jane": "World1",
             "WorldName" : "Derias",
             "Email": "janestrong@email.com",
             "ManaPoints": "51",
             "Posts": "2",
             "Comments": "1",
             "Awards": "0",
             "History": "Type here to add lore...",
             "Cultures": "Type here to add lore...",
             "Species": "Type here to add lore...",
             "Religions": "Type here to add lore..."}

#Database for Timeline entries.
database3 = {"TimelineTitle": "Type here to add timeline name...",
             "TimelineBox1: " : "..."}
# Put database stuff in here

def create_app():
    app = Flask(__name__)
    # @login_manager.user_loader
    ## Add user database stuff in here once database is connected
    # def load_user(user_id):
     #   return User.query.get(int(user_id))

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
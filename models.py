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
    id = Column(Integer, ForeignKey("users.id"), primary_key=True, autoincrement=True)
    UserName = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    posted_date = Column(DateTime, default=datetime.now)

    def __init__(self, id, UserName, title, content, posted_date):
        self.id = id
        self.UserName = UserName
        self.title = title
        self.content = content
        self.posted_date = posted_date
    
    def __repr__(self):
        return f"({self.id}) ({self.title}) ({self.UserName}) ({self.content}) ({self.posted_date})"

# engine = create_engine("sqlite:///database.db", echo=True)



Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
# World Database initialise.

# w1 = World("KingdomCome", "Vardattia", "In the realm of Eldoria, a vast and enchanting world, magic flows through every corner, shaping the very essence of existence. Eldoria is composed of diverse landscapes, from towering mountain ranges to sprawling forests and serene coastal regions. The land is adorned with ancient ruins, mystical portals, and hidden realms waiting to be discovered. The celestial bodies hold great significance in Eldorian culture, and the skies are often adorned with breathtaking displays of celestial magic.")


# w2a = World("Rambunctious51", "Dardeccia", "Dardeccia is a vast and enchanting world, brimming with breathtaking landscapes and mystical wonders. It is comprised of diverse terrains, ranging from lush forests teeming with ancient trees to towering mountains that touch the heavens. The realm is dotted with sparkling rivers, majestic lakes, and hidden caves that hold secrets untold. Dardeccia is known for its ever-changing weather, with regions experiencing distinct climates, including tropical jungles, arid deserts, and icy tundras. Magic permeates every aspect of life, and the veil between the mortal realm and the supernatural is thin, allowing for fantastical creatures and extraordinary phenomena to roam freely.")

# w2b = World("Rambunctious51", "Sorata", "A land of coolness, chill and awesome - edit later.")


# w3 = World("firebrand", "Fantasia", "This world is based on a famous ancient Atlantis Myth.")


# History Database initialise.

# h1a = History("KingdomCome", "Vardattia", "The History of Vardattia", "Long ago, Eldoria was a land of chaos and darkness. The Elder Gods, beings of immense power and wisdom, emerged from the cosmic ether and brought balance to the realm. They established the mystical Arcane Council, a group of magical beings tasked with safeguarding the delicate equilibrium of Eldoria. Over the centuries, great empires rose and fell, leaving behind legacies etched into the annals of history. The world witnessed cataclysms, wars, and periods of enlightenment, each shaping the destiny of Eldoria.")

# h1b = History("KingdomCome", "Vardattia", "The History of Moloresh", "During the Era of Lost Kingdoms, a forgotten chapter in Eldoria's history, magnificent realms and powerful empires thrived across the land known as the Moloresh. These kingdoms possessed unimaginable wealth, profound knowledge, and incredible magical artifacts. However, their fates were ultimately sealed by a combination of internal strife, external threats, and mysterious calamities.")


# h2 = History("Rambunctious51", "Dardeccia", "History of the Kingdom", "Dardeccia is home to a rich tapestry of cultures, each with its own customs, traditions, and values. The Elven civilization, residing within the ancient forests, is deeply attuned to nature and magic. They are masters of archery, craftsmanship, and arcane arts. The Dwarves, dwelling in sprawling underground cities and mountains, excel in mining, engineering, and the forging of legendary weapons and armor. Known for their stoicism and love for exploration, they have an insatiable thirst for knowledge.")

# h3 = History("firebrand", "Fantasia", "The Five Steel Provinces", "Please insert lore...")


# # Culture Database initialise.

# c1 = Culture("KingdomCome", "Vardattia", "The Steelhorns", "The Steelborns are a culture that use a metal bee in their sigil.")

# c2 = Culture("Rambunctious51", "Dardeccia", "Firefoots", "The Firefoots are a culture of fireflies that can spew lava from their feet.")

# c3 = Culture("firebrand", "Fantasia", "Centaurs", "Centaurs roam the wild forests.")


# # Religion Database initialise.

# r1 = Religion("KingdomCome", "Vardattia", "Fire Worshippers", "The Fire Worshippers worship the great torch in the sky.")

# r2 = Religion("Rambunctious51", "Dardeccia", "Bendigata", "A great wizard who became a prophet.")

# r3 = Religion("firebrand", "Fantasia", "Tartarians", "Worshippers of the Greek Titans.")


# # Species Database initialise.

# s1 = Species("KingdomCome", "Vardattia", "Fire Ferrets", "A species of red panda that can breathe fire.")

# s2 = Species("Rambunctious51", "Dardeccia", "Orbols", "Orb beings that like to chill.")

# s3 = Species("firebrand", "Fantasia", "Centaurs", "Centaurs are quadrupeds with two extra human arms and are half man, half horse.")


# # Timeline Database initialise.

# t1a = Timeline("KingdomCome", "Vardattia", "23AR: The Great Flamer War.", "A great war which tore the countries apart because of trolls.")

# t1b = Timeline("KingdomCome", "Vardattia", "45AR: The Relaxing.", "The war settled to a close and peace was again fostered.")

# t1c = Timeline("KingdomCome", "Vardattia", "64AR: Here We Go Again Conflict.", "Those dang evildoers are at it again.")


# t2a = Timeline("Rambunctious51", "Dardeccia", "Year 1: Forges of the Gods.", "The Forges of the Gods are lit and the world springs to life in fire and glory.")

# t2b = Timeline("Rambunctious51", "Dardeccia", "Year 14: The Great Smiths.", "Several apprentices to the gods set out to make their own kingdoms apart from the gods.")


# t3a = Timeline("firebrand", "Fantasia", "360BC: The Titan Awakening.", "The Athenians discover a way into Atlantis deep beneath the ocean and awaken the titans.")

# t3b = Timeline("firebrand", "Fantasia", "2023AD: The Story Begins!", "The Greek Gods must seal the titans back away with the help of other gods.")




# #Add all new sessions.
# session.add(w1)
# session.add(h1a)
# session.add(h1b)
# session.add(h2)
# session.add(h3)
# session.add(c1)
# session.add(c2)
# session.add(c3)
# session.add(r1)
# session.add(r2)
# session.add(r3)
# session.add(s1)
# session.add(s2)
# session.add(s3)
# session.add(t1a)
# session.add(t1b)
# session.add(t1c)
# session.add(t2a)
# session.add(t2b)
# session.add(t3a)
# session.add(t3b)
# session.add(w1)
# session.add(w2a)
# session.add(w2b)
# session.add(w3)
# session.add(h1a)
# session.add(h1b)
# session.add(h2)
# session.add(h3)
# session.add(c1)
# session.add(r1)
# session.add(s1)
# session.add(t1a)

# # Delete Tables
# # User.__table__.drop(bind=engine)
# # World.__table__.drop(bind=engine)
# # History.__table__.drop(bind=engine)
# # Culture.__table__.drop(bind=engine)
# # Species.__table__.drop(bind=engine)
# # Religion.__table__.drop(bind=engine)
# # Timeline.__table__.drop(bind=engine)
# # # Commit changes.
# Img.__table__.drop(bind=engine)
# session.commit()
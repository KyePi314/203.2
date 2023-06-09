## The init file ##
from flask import Flask, render_template, request, Blueprint
from flask_sqlalchemy import SQLAlchemy

# #Create the Database
# engine = create_engine("sqlite:///database.db", echo=True)
# #Uses the engine to create the tables for data.
# Base.metadata.create_all(bind=engine)
# #Creates a session.
# Session = sessionmaker(bind=engine)
# session = Session()

# User1 = User("KingdomCome", "Empire123", "janelynn@email.com", 12, 1, 2, 0, "Celestial")

# User2 = User("Rambunctious51", "George12", "yeyeye23@email.com", 113, 3, 14, 2, "Classic")

# User3 = User("firebrand", "password", "fieryone@email.com", 44, 7, 4, 1, "Classic")

# session.add(User1)
# session.add(User2)
# session.add(User3)

# session.commit()

# # temp database until proper one hooked up
# database = {'Jane':'123',
#             'Dean':'666',
#             'Ollie':'999'}

# # Temporary database dictionary for storing information for worlds
# database2 = {"Jane": "World1",
#              "WorldName" : "Derias",
#              "Email": "janestrong@email.com",
#              "ManaPoints": "51",
#              "Posts": "2",
#              "Comments": "1",
#              "Awards": "0",
#              "History": "Type here to add lore...",
#              "Cultures": "Type here to add lore...",
#              "Species": "Type here to add lore...",
#              "Religions": "Type here to add lore..."}

# #Database for Timeline entries.
# database3 = {"TimelineTitle": "Type here to add timeline name...",
#              "TimelineBox1: " : "..."}

# The function that initializes the application and its authentication system/databse 

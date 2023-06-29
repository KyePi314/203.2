#  This python file handles all of the updating and editing features, such as editing world details, updating specific details and adding new ones, posting posts on home feed etc 
from datetime import datetime
from base64 import b64encode
import base64
from io import BytesIO #Converts data from Database into bytes
from flask import render_template, request, Blueprint, redirect, session, url_for, flash, jsonify
from models import (engine, User, session, Img, World, Culture, History, Timeline, Religion, Species, Post, Comment, Like)
from flask_login import current_user, login_required
from sqlalchemy import MetaData

update = Blueprint('update', __name__)

### Functions that handle the homefeed functions:
## This function handles the posts themselves
@update.route('/Post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        # Gets the User input from the form
        title = request.form.get("title")
        content = request.form.get("content")
        rows = session.query(Post).count()
        # sets the posted time column of the database to the time the post is posted
        now = datetime.now()
        post_time = now.strftime("%d-%m-%y %H:%M")
        post_datetime = datetime.strptime(post_time, "%d-%m-%y %H:%M")
        # Allows multiple posts from the same user by manually incrememnting the post id
        postID = rows + 1
        # Adding the new post to the database
        new_post = Post(UserName=current_user.UserName, id=postID, user_id=current_user.id, title=title, content=content, posted_date=post_datetime, Likes=0)
        session.add(new_post)
        session.commit()
        # Finding all the data needed to display content on the home page
        find_comments = session.query(Comment).all()
        find_post = session.query(Post).all()
        return redirect(url_for("main.home", username=current_user.UserName, posts=find_post, comments=find_comments))
    return render_template("Post.html")

## This function handles taking the comments submitted, saving them to the database and then displaying them
@update.route('/post_comment', methods=['POST', 'GET'])
def post_comment():
    find_post = session.query(Post).all()
    find_comments = session.query(Comment).all()
    if request.method == 'POST':
        post_id = request.form['post_id']
        author = request.form['author']
        content = request.form['content']
        # Flash error message displays if the user tries to comment without entering anything into the comment input section
        if not content:
            flash('Nothing to comment!')
            return redirect(url_for("main.home", username=current_user.UserName, posts=find_post, comments=find_comments))
        # Saves the post to the database linking it to the post its under, and reloads the page with the new comment
        else:
            comment = Comment(post_id=post_id, author=author, content=content)
            session.add(comment)
            session.commit()
    return redirect(url_for("main.home", username=current_user.UserName, posts=find_post, comments=find_comments))

## This function handles taking the likes and saving them to the correct post in the database and then displaying the correct number on the post
@update.route('/like_post', methods=['POST', 'GET'])
@login_required
def like_post():
    # Getting all the posts and comments so when the page reloads it loads with the correct data
    find_post = session.query(Post).all()
    find_comments = session.query(Comment).all()
    # If the liked button is clicked then the post's liked number is incrememnted by one
    if request.method == 'POST':
        post_id = request.form['post_id']
        post = session.query(Post).filter_by(id=post_id).first()
        print("POST: ", post)
        user_id = current_user.id
        already_liked = session.query(Like).filter_by(post_id=post_id, user_id=user_id).first()
        if not already_liked:
            post.Likes += 1
            new_like = Like(post_id=post_id, user_id=user_id)
            session.add(new_like)
            session.commit()
        is_liked = already_liked  # Assign already_liked to is_liked
        return render_template("home.html", username=current_user.UserName, posts=find_post, comments=find_comments, is_liked=is_liked)
    return redirect(url_for("main.home", username=current_user.UserName, posts=find_post, comments=find_comments))

### Code that handles getting the correct world ###
@update.route("/worldspage", methods=['POST', 'GET'])
@login_required
def worlds():
    worlds = session.query(World.WorldName).filter_by(UserName = current_user.UserName).all()
    world_names = [world[0] for world in worlds]  # Extract only the string values
    
    return render_template("worldsPage.html", worlds_list=world_names)

@update.route("/worldinfo/", methods=['POST'])
def worldinfo():
    if request.method == 'POST':
        # Gets the world choice dropdown from the html form
        select = request.form.get('option')
        if select == "choose":
            flash('please choose a world from the dropdown')
            return redirect(url_for('update.worlds'))
        elif select is None:
            flash('No worlds avaliable. Please create one.')
            return redirect(url_for('update.worlds'))
        else:
            ## Getting all the details to fill out the HTML page
            world = session.query(World).filter_by(WorldName=select, UserName=current_user.UserName).first()
            culture = session.query(Culture).filter_by(WorldName=select).all()
            history = session.query(History).filter_by(WorldName=select).all()
            timelines = session.query(Timeline).filter_by(WorldName=select).all()
            religion = session.query(Religion).filter_by(WorldName=select).all()
            species = session.query(Species).filter_by(WorldName=select).all()
            return render_template("worldinfo.html", WorldName=world.WorldName if world else None, description=world.WorldDescription if world else None, Culture_details=culture if culture else None, History_details=history if history else None, Timeline_details=timelines if timelines else None, Species_details=species if species else None, Religions_details=religion if religion else None)
    else:
        return render_template("")
    
### Code for the various specific detail routes ####
@update.route("/religion/")
def religion():
    worldname = request.args.get("WorldName")
    details = session.query(Religion).filter_by(WorldName=worldname).all()
    return render_template("religion.html", WorldName=worldname, details=details)

@update.route("/species/")
def species():
    worldname = request.args.get("WorldName")
    details = session.query(Species).filter_by(WorldName=worldname).all()
    return render_template("species.html", WorldName=worldname, details=details)

@update.route("/Timeline/", methods=['GET', 'POST'])
def timeline():
    worldname = request.args.get("WorldName")
    details = session.query(Timeline).filter_by(WorldName=worldname).all()
    return render_template("Timeline.html", WorldName=worldname, details=details)

@update.route("/history/")
def history():
    worldname = request.args.get("WorldName")
    details = session.query(History).filter_by(WorldName=worldname).all()
    return render_template("history.html", WorldName=worldname, details=details)

@update.route("/culture/", methods=['GET', 'POST'])
def culture():
    worldname = request.args.get("WorldName")
    details = session.query(Culture).filter_by(WorldName=worldname).all()
    return render_template("culture.html", WorldName=worldname, details=details)

# Handles the editing of the specific world details
@update.route("/specificDetails", methods=['GET', 'POST'])
def specificDetails():
    # Sets the existing_details variable as empty to start with and  gets the world's name from the URL parameters in order to display it on the page
    existing_details = [] 
    worldname = request.args.get("WorldName")
    if request.method == 'GET':
        select = request.args.get('choose_detail')
        return render_template("specificDetails.html", WorldName=worldname, existing_detail=existing_details)
    elif request.method == 'POST':
        # Getting all the form input information
        choice = request.form.get('choice')
        world_name = request.form.get("WorldName")
        select = request.form.get('choose_detail')
        title =  request.form.get('title')
        description = request.form.get('detail_description')
        choose_existing_detail = request.form.get('choose_existing_detail')
        # Checks that the form isn't empty
        if title != '' and description != '' or choice == 'delete':
            # If the user hasn't chosen a detail to edit this message will be shown
            if select == "choose":
                flash('please choose a detail to edit from the dropdown')
            # Code for if the user picks Culture
            if select == 'Culture':
                rows = session.query(Culture).count()
                rowID = rows + 1
                # Adding new culture details
                if choice == 'add':
                    update_details = Culture(id=rowID, UserName=current_user.UserName, WorldName=world_name, CultureTitle=title, CultureDescription=description)
                    session.add(update_details)
                elif choice == 'edit':
                    # This if statement checks to see whether or not the user has choosen a detail to edit
                    if choose_existing_detail == 'choose':
                        flash('Please choose an existing detail to edit')
                        return render_template("specificDetails.html", WorldName=world_name)
                    else:
                        # Update existing Culture detail
                        add_details = session.query(Culture).filter_by(CultureTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                        add_details.CultureTitle = title
                        add_details.CultureDescription = description
                        session.commit()
                # Deletes the choosen detail
                elif choice == 'delete':
                    delete_detail = session.query(Culture).filter_by(CultureTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                    session.delete(delete_detail)
                # This error is thrown is the user hasn't selected a radio button
                else:
                    flash('Please choose if you want to add a new detail to your world or edit an existing one!')
                    return render_template("specificDetails.html", WorldName=world_name)
                # Saving the changes to the database and redirecting to the culture page
                session.commit()
                update_details = session.query(Culture).filter_by(WorldName=world_name, UserName=current_user.UserName).all()
                return redirect(url_for('update.culture', details=update_details, WorldName=world_name))
            # Code for if the user picks History
            elif select == 'History':
                rows = session.query(History).count()
                rowID = rows + 1
                # Adding a new detail for the world's history
                if choice == 'add':
                    update_details = History(id=rowID, UserName=current_user.UserName, WorldName=world_name, HistoryTitle=title, HistoryDescription=description)
                    session.add(update_details)
                elif choice == 'edit':
                    if choose_existing_detail == 'choose':
                        flash('Please choose an existing detail to edit')
                        return render_template("specificDetails.html", WorldName=world_name)
                    else:
                        # Update existing details in the world's history
                        add_details = session.query(History).filter_by(HistoryTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                        add_details.HistoryTitle = title
                        add_details.HistoryDescription = description
                        session.commit()
                # Deletes the choosen detail
                elif choice == 'delete':
                    delete_detail = session.query(History).filter_by(HistoryTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                    session.delete(delete_detail)
                # This error is thrown is the user hasn't selected a radio button    
                else:
                    flash('Please choose what you want to do!')
                    return render_template("specificDetails.html", WorldName=worldname)
                session.commit()
                update_details = session.query(History).filter_by(WorldName=world_name, UserName=current_user.UserName).all()
                return redirect(url_for('update.history', details=update_details, WorldName=world_name))
            # Code for if the user picks Religion
            elif select == 'Religion':
                rows = session.query(Religion).count()
                rowID = rows + 1
                # Adding a new Religion for the world
                if choice == 'add':
                    update_details = Religion(id=rowID, UserName=current_user.UserName, WorldName=world_name, ReligionTitle=title, ReligionDescription=description)
                    session.add(update_details)
                # Editing an exising religion in the world
                elif choice == 'edit':
                    if choose_existing_detail == 'choose':
                        flash('Please choose an existing detail to edit')
                        return render_template("specificDetails.html", WorldName=world_name)
                    else:
                        add_details = session.query(Religion).filter_by(ReligionTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                        add_details.ReligionTitle = title
                        add_details.ReligionDescription = description
                        session.commit()
                # Deletes the choosen detail
                elif choice == 'delete':
                    delete_detail = session.query(Religion).filter_by(ReligionTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                    session.delete(delete_detail)
                # This error is thrown is the user hasn't selected a radio button
                else:
                    flash('Please choose if you want to add a new detail to your world or edit an existing one!')
                    return render_template("specificDetails.html", WorldName=world_name)
                session.commit()
                update_details = session.query(Religion).filter_by(WorldName=world_name, UserName=current_user.UserName).all()
                return redirect(url_for('update.religion', details=update_details, WorldName=world_name))
            # Code for if the user picks Species
            elif select == 'Species':
                rows = session.query(Species).count()
                rowID = rows + 1
                # Add a new species to the world
                if choice == 'add':
                    update_details = Species(id=rowID, UserName=current_user.UserName, WorldName=world_name, SpeciesTitle=title, SpeciesDescription=description)
                    session.add(update_details)
                # Update existing Species' detail
                elif choice == 'edit':
                    if choose_existing_detail == 'choose':
                        flash('Please choose an existing detail to edit')
                        return render_template("specificDetails.html", WorldName=world_name)
                    else:
                        add_details = session.query(Species).filter_by(SpeciesTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                        add_details.SpeciesTitle = title
                        add_details.SpeciesDescription = description
                        session.commit()
                # Deletes the choosen detail
                elif choice == 'delete':
                    delete_detail = session.query(Species).filter_by(HistoryTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                    session.delete(delete_detail)
                # This error is thrown is the user hasn't selected a radio button
                else:
                    flash('Please choose if you want to add a new detail to your world or edit an existing one!')
                    return render_template("specificDetails.html", WorldName=world_name)
                session.commit()
                update_details = session.query(Species).filter_by(WorldName=world_name, UserName=current_user.UserName).all()
                return redirect(url_for('update.species', details=update_details, WorldName=world_name))
            # Code for if the user picks Timeline
            elif select == 'Timeline':
                rows = session.query(Timeline).count()
                rowID = rows + 1
                # Add a new entry to the timeline
                if choice == 'add':
                    update_details = Timeline(id=rowID, UserName=current_user.UserName, WorldName=world_name, TimelineTitle=title, TimelineEntry=description)
                    session.add(update_details)
                # Update existing Timeline detail
                elif choice == 'edit':
                    if choose_existing_detail == 'choose':
                        flash('Please choose an existing detail to edit')
                        return render_template("specificDetails.html", WorldName=world_name)
                    else:
                        add_details = session.query(Timeline).filter_by(TimelineTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                        add_details.TimelineTitle = title
                        add_details.TimelineEntry = description
                        session.commit()
                # Deletes the choosen detail
                elif choice == 'delete':
                    delete_detail = session.query(Timeline).filter_by(TimelineTitle=choose_existing_detail, WorldName=world_name, UserName=current_user.UserName).first()
                    session.delete(delete_detail)
                # This error is thrown is the user hasn't selected a radio button
                else:
                    flash('Please choose if you want to add a new detail to your world or edit an existing one!')
                    return render_template("specificDetails.html", WorldName=world_name)
                session.commit()
                update_details = session.query(Timeline).filter_by(WorldName=world_name, UserName=current_user.UserName).all()
                return redirect(url_for('update.timeline', details=update_details, WorldName=world_name)) 
            # This Error is thrown if the user hasn't chosen a detail to edit
            else:
                flash('Please Fill out the form!')
                return render_template("specificDetails.html", WorldName=world_name, existing_detail=existing_details)
        # This Error is thrown if the user hasn't filled out any details
        else:
            flash('Please choose a detail to edit!')
            return render_template("specificDetails.html", WorldName=world_name, existing_detail=existing_details)

    return render_template("specificDetails.html", WorldName=worldname, existing_detail=existing_details)


### Code used to dynamically updated the edit existing details dropdown on the specificDetails page
@update.route("/getExistingDetails", methods=['POST'])
def getExistingDetails():
    select = request.form.get('select')
    worldname = request.form.get("WorldName")
    existing_details = []
    if select == 'Choose':
        flash('Please choose a detail to edit!')
        return render_template("specificDetails.html", WorldName=worldname, existing_detail=existing_details)
    if select == 'Culture':
        existing_cultures = session.query(Culture).filter_by(WorldName=worldname).all()
        existing_details = [{'choice': 'Culture', 'detailType': culture.CultureTitle} for culture in existing_cultures]
        print("TEST: ", existing_details)
    elif select == 'History':
        existing_histories = session.query(History).filter_by(WorldName=worldname).all()
        existing_details = [{'choice': 'History', 'detailType': history.HistoryTitle} for history in existing_histories]
    elif select == 'Religion':
        existing_religions = session.query(Religion).filter_by(WorldName=worldname).all()
        existing_details = [{'choice': 'Religion', 'detailType': religion.ReligionTitle} for religion in existing_religions]
    elif select == 'Species':
        existing_species = session.query(Species).filter_by(WorldName=worldname).all()
        existing_details = [{'choice': 'Species', 'detailType': species.SpeciesTitle} for species in existing_species]
    elif select == 'Timeline':
        existing_timelines = session.query(Timeline).filter_by(WorldName=worldname).all()
        existing_details = [{'choice': 'Timeline', 'detailType': timeline.TimelineTitle} for timeline in existing_timelines]
    return jsonify(existing_details)

#### Code for uploading pictures to Image database and updating the world's details ####
def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

@update.route("/editworldinfo/", methods=['POST', 'GET'])
def editworld():
    world_name = request.args.get('WorldName')
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_description = request.form.get('worldDetails')
        world_name = request.form.get('worldName')
        if request.files['imageFile']:
            img = request.files['imageFile']
            data = img.read()
            render_file = render_picture(data)
            rows = session.query(Img).count()
            imgId = rows + 1
            imgFile = Img(worldName=new_name if new_name else world_name, id=imgId, UserName=current_user.UserName, data=data, rendered_data=render_file)
            session.add(imgFile)
        updateWorld = session.query(World).filter_by(WorldName = world_name).first()
        update_culture = session.query(Culture).filter_by(WorldName=world_name).all()
        
        update_history = session.query(History).filter_by(WorldName=world_name).all()
        update_religion = session.query(Religion).filter_by(WorldName=world_name).all()
        update_species = session.query(Species).filter_by(WorldName=world_name).all()
        update_timeline= session.query(Timeline).filter_by(WorldName=world_name).all()
        if not new_name and not new_description.strip():
            flash('Please enter some information to update!')
            return redirect(url_for('update.editworld', worldName=world_name))
        if new_name:
            updateWorld.WorldName = new_name
            for c in update_culture:
                c.WorldName = new_name
            for h in update_history:
                h.WorldName = new_name
            for r in update_religion:
                r.WorldName = new_name
            for s in update_species:
                s.WorldName = new_name
            for t in update_timeline:
                t.WorldName = new_name
        if new_description.strip():
            updateWorld.WorldDescription = new_description
        session.commit()
        return redirect(url_for('update.worlds', worldName=world_name))
    
    return render_template("editworldinfo.html", worldName=world_name)
    


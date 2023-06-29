from datetime import datetime
from flask import render_template, request, Blueprint, redirect, session, url_for, flash, jsonify
from models import (engine, session, Post, Comment, Like)
from flask_login import current_user, login_required

homefeed = Blueprint('homefeed', __name__)

### Functions that handle the homefeed functions:
## This function handles the posts themselves
@homefeed.route('/Post', methods=['GET', 'POST'])
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
@homefeed.route('/post_comment', methods=['POST', 'GET'])
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
@homefeed.route('/like_post', methods=['POST', 'GET'])
@login_required
def like_post():
    # Getting all the posts and comments so when the page reloads it loads with the correct data
    find_post = session.query(Post).all()
    find_comments = session.query(Comment).all()
    
    if request.method == 'POST':
        post_id = request.form['post_id']
        post = session.query(Post).filter_by(id=post_id).first()
        print("POST: ", post)
        user_id = current_user.id
        # Checks if the user has already liked the post or not
        already_liked = session.query(Like).filter_by(post_id=post_id, user_id=user_id).first()
        # If the user has not already liked the post, their like is add to it 
        if not already_liked:
            # If the liked button is clicked then the post's liked number is incrememnted by one
            post.Likes += 1
            # Adds their like to the like table with their user_id and the post_id
            new_like = Like(post_id=post_id, user_id=user_id)
            session.add(new_like)
            session.commit()
        is_liked = already_liked  # Assign already_liked to is_liked
        return render_template("home.html", username=current_user.UserName, posts=find_post, comments=find_comments, is_liked=is_liked)
    return redirect(url_for("main.home", username=current_user.UserName, posts=find_post, comments=find_comments))

from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import LoginForm, QueryForm
from app.facebook_launcher.launcher import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    form = QueryForm()
    if form.validate_on_submit():
        your_name = form.my_username.data
        user_requested = form.username.data
        chat_counts = get_chats_and_messages(user_requested)
        message_count = get_message_count(user_requested)
        chat_participation = get_chat_participation(user_requested)
        chat_count_dict = get_chat_count_dict()
        total_p = sum(chat_participation.values())
        my_part = get_chat_participation(your_name)
        return render_template('count.html', title= 'Facebook Message Counter', your_name = your_name, message_count = message_count, other_user = user_requested, chat_counts = chat_counts, chat_participation = chat_participation, chat_count_dict = chat_count_dict, total_p = total_p, my_part = my_part)
        #redirect(url_for('index'))
    return render_template('facebook.html', title='Facebook Message Counter', form=form)

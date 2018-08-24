# project/home/views.py

#################
#### imports ####
#################

from flask import render_template, Blueprint, request, redirect, url_for, flash


################
#### config ####
################

home_blueprint = Blueprint('home', __name__)

##########################
#### helper functions ####
##########################

################
#### routes ####
################

@home_blueprint.route('/')
def go_home():
    return render_template('home.html')

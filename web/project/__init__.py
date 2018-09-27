#################
#### imports ####
#################

from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, TEXT, configure_uploads

################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)

# Configure the files uploading via Flask-Uploads
files = UploadSet('files', TEXT)
configure_uploads(app, files)

####################
#### blueprints ####
####################

from project.home.views import home_blueprint
from project.papers.views import papers_blueprint

# register the blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(papers_blueprint)

# TODO:  Move this to ingx
@app.route('/files/<filename>')
def uploaded_file(filename):
    return send_from_directory(
        app.config['UPLOADS_IMAGES_DEST'],
        filename
    )

############################
#### custom error pages ####
############################

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@app.errorhandler(410)
def page_not_found(e):
    return render_template('410.html'), 410

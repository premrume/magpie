# project/papers/views.py

#################
#### imports ####
#################

from flask import render_template, Blueprint, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from project.models import Paper
from project import db, images
from .forms import AddPaperForm

################
#### config ####
################

papers_blueprint = Blueprint('papers', __name__)

##########################
#### helper functions ####
##########################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'info')

################
#### routes ####
################
@papers_blueprint.route('/papers/upload/', methods=['GET','POST'])
def go_images_upload():
    form = AddPaperForm()
    if request.method == 'POST':
        try:
         if form.validate_on_submit():
             # TODO: make this a secure filename
             filename = images.save(request.files['upload'])
             url = images.url(filename)
             new_paper = Paper(form.title.data, filename, url)
             db.session.add(new_paper)
             db.session.commit()
             flash('SUCCESS: Title {} added'.format(new_paper.title), 'success')
             return redirect(url_for('papers.go_images_upload'))

         else:
             flash('ERROR: try again', 'error')

        except IntegrityError:
             flash('ERROR: Title {} is a duplicate, try again'.format(new_paper.title), 'error')

    return render_template('images_upload.html',
                           form=form)

@papers_blueprint.route('/papers/list', methods=['GET'])
def go_images_list():
    all_papers = Paper.query.all()
    return render_template('images_list.html', papers=all_papers)

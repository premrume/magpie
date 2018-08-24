# project/papers/forms.py


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from project import images


class AddPaperForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    upload = FileField('Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])

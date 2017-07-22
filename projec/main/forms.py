from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename



class UploadForm(FlaskForm):
    #file_1 = FileField('First File',validators=[FileRequired()])
    file_1 = FileField('First File')
    #file_2 = FileField('Second File',validators=[FileRequired()])
    #file_2 = FileField('Second File')


# project/main/views.py


#################
#### imports ####
#################

from project.decorators import check_confirmed
from flask import render_template, Blueprint, url_for, \
    redirect, flash, request 
from flask_login import login_user, logout_user, \
    login_required, current_user
from .forms import UploadForm
from werkzeug import secure_filename
from project.cosine import similarity
from project import app
################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


###########################
ALLOWED_EXTENSIONS = set(['txt'])
 

################
#### routes ####
################


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@main_blueprint.route('/')
def home():
    return render_template('main/index.html')
      

@main_blueprint.route('/compare', methods=['GET', 'POST'])
@login_required
@check_confirmed
def compare():
     if request.method == 'POST':
              if request.method == 'POST':
              	       p = None
              	       t = None
              	       fname1 = None
              	       fname2 = None
                         # check if the post request has the file part
                       if 'file1' not in request.files or 'file2' not in request.files:
                                   flash('No file part')
                                   return redirect(request.url)
                       file1 = request.files['file1']
                       file2 = request.files['file2']
                       if file1.filename == '' or file2.filename == '':
                                 flash('No selected file')
                                 return redirect(request.url)
                       if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
                       	           #str = unicode(str, errors='ignore')
                       	          f1 = unicode(request.files['file1'].read(),errors='ignore') 
                       	          f2 = unicode(request.files['file2'].read(),errors='ignore') 
                       	                                                                       #f2 = request.files['file2'].read()
                                  fname1 = file1.filename
                                  fname2 = file2.filename
                       	          p = similarity(f1,f2)
                       	          t = True
                                  
                       	          #if p == 0:
                       	          	#flash('There are no similarity')
                       	          	#return render_template('main/upload.html',p='',fname1='',fname2='')


                       	          #return str(p)                           # p= 80
                       	          return render_template('main/upload.html',p=p,fname1=fname1,fname2=fname2,t=t)
                       	           
                

     return render_template('main/upload.html',p='',fname1='',fname2='')

from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
UPLOAD_FOLDER = '/home/dtc/site/upload'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif','doc','docx','mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
   return render_template('dtchome.html')


@app.route('/dtc')
def dtc():
   return render_template('dtchome.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('download')
def download():
   return render_template('download.html')

def allowed_file(filename):
   return '.' in filename and \
      filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET','POST'])
def upload():
   if request.method == 'POST':
      file = request.files['file']
      if file and allowed_file(file.filename):
         filename = secure_filename(file.filename)
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         return render_template('uploadsuccessful.html')
   return render_template('upload.html')

if __name__=='__main__':
   app.run(port=5000)

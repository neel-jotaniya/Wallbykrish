from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

email = ['jotaniyaneel07@gmail.com','jotaniyakrish07@gmail.com']

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("postgres", "postgresql")

# sqlite:////test.db
# os.environ.get('DATABASE_URL').replace("postgres", "postgresql")
global security_code
security_code = False


db = SQLAlchemy(app)
class Content(db.Model):
    Wallpaper_link = db.Column(db.String(1000),nullable=False)
    Wallpaper_title = db.Column(db.String(1000),nullable=False)   
    Wallpaper_thumbnail_link = db.Column(db.String(1000),nullable=False)
    Wallpaper_description = db.Column(db.String(1000),nullable=False)
    SNO = db.Column(db.Integer, primary_key=True,nullable=False)
    Wallpaper_compatibility = db.Column(db.String(1000),nullable=False)
    
    
class Feedback(db.Model):
    name = db.Column(db.String(1000),nullable=False)
    rating = db.Column(db.String(1000),nullable=False)
    suggestion = db.Column(db.String(1000),nullable=False)
    SNO = db.Column(db.Integer, primary_key=True,nullable=False)
    

    
db.init_app(app)
db.create_all()

@app.route('/',methods = ['GET','POST'])
def home():
    all_image = Content.query.all()  
    if request.method == 'POST':
        name = request.form.get('name')
        rating = request.form.get('rating')
        suggestion = request.form.get('message')
        feedback_form = Feedback(name = name,rating = rating,suggestion = suggestion)
        db.session.add(feedback_form)
        db.session.commit()

        


             
    return render_template('index.html', all_image = all_image)

@app.route('/add',methods = ['GET','POST'])
def private_route():
    if request.method == 'POST':   
        Wallpaper_title = request.form.get('title')
        Wallpaper_thumbnail_link = request.form.get('thumbnailLink')
        Wallpaper_link = request.form.get('wallpaperLink')
        Wallpaper_description = request.form.get('wallDesc')
        Wallpaper_compatibility = request.form.get('wallpaperType')
        entry = Content(Wallpaper_description = Wallpaper_description,
                        Wallpaper_link = Wallpaper_link,
                        Wallpaper_title = Wallpaper_title,
                        Wallpaper_thumbnail_link = Wallpaper_thumbnail_link,
                        Wallpaper_compatibility = Wallpaper_compatibility
                        )
        
        db.session.add(entry)
        db.session.commit()
        
        return render_template('addWallpaper.html')
    else:
        
        if security_code == True:
            return render_template('addWallpaper.html')
        else :
            return "Not autheticated"
        
        
    
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('uniqueid')
        password = request.form.get('inputpassword')
        if id in email and password == '101010':
            global security_code
            security_code = True
            return render_template('admin.html')
      
    else :
        return render_template('login.html')
    
    
@app.route('/admin' ,methods = ['GET','POST'])
def admin():
    if security_code == True:
        return render_template('admin.html')
    else :
        return "Not autheticated"
    

@app.route('/delete/<int:SNO>' )
def delete(SNO):  
    todo = Content.query.filter_by(SNO=SNO).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/delete")

@app.route('/delete' ,methods = ['GET','POST'])
def delete_page():
    all_image = Content.query.all()
    if security_code:       
        return render_template('deleteWallpaper.html', all_image = all_image)
    else:
        return "Not autheticated"
    

@app.route('/feedback')
def feedback_form():
    all_feedback = Feedback.query.all()
    if security_code:
        return render_template('suggestionEntry.html',all_feedback = all_feedback)
    else :
        return "Not autheticated"




    


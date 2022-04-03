from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)#mysql://fkobrltakxhyef:7df23ed83fcd49d0b3d61296506a64684cdcb39a1e5f90fa91f3a4f51c0ff87a@server/db

email = ['jotaniyaneel07@gmail.com','jotaniyakrish07@gmail.com']

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

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

        
             
    return render_template('index.html', all_image = all_image)

@app.route('/admin',methods = ['GET','POST'])
def private_route():
    if request.method == 'POST':      
        Wallpaper_title = request.form.get('wallpaper Title')
        Wallpaper_thumbnail_link = request.form.get('Wallpaper Thumbnail Link')
        Wallpaper_link = request.form.get('Wallpaper Link')
        Wallpaper_description = request.form.get('Wallpaper Description')
        Wallpaper_compatibility = request.form.get('Wallpaper Compatibility')
        # print(Wallpaper_compatibility)
        entry = Content(Wallpaper_description = Wallpaper_description,
                        Wallpaper_link = Wallpaper_link,
                        Wallpaper_title = Wallpaper_title,
                        Wallpaper_thumbnail_link = Wallpaper_thumbnail_link,
                        Wallpaper_compatibility = Wallpaper_compatibility
                        )
        
        db.session.add(entry)
        db.session.commit()
        
        return redirect('/')
    else:
        return render_template('admin.html')
    
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('uniqueid')
        password = request.form.get('inputpassword')
        if id in email and password == '101010':
            return render_template('admin.html')
        else :
            return render_template('login.html')
    else :
        return render_template('login.html')
    
if __name__ == "__main__":
    app.run(debug=True)
        



    


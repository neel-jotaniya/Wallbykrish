from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)#mysql://username:password@server/db


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
class Content(db.Model):
    Wallpaper_link = db.Column(db.String(1000),nullable=False)
    Wallpaper_title = db.Column(db.String(1000),nullable=False)   
    Wallpaper_thumbnail_link = db.Column(db.String(1000),nullable=False)
    Wallpaper_description = db.Column(db.String(1000),nullable=False)
    SNO = db.Column(db.Integer, primary_key=True,nullable=False)
    Wallpaper_compatibility = db.Column(db.String(1000),nullable=False)

    
db.init_app(app)
db.create_all()

@app.route('/',methods = ['GET','POST'])
def home():
    all_image = Content.query.all()
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



    


from flask import Flask, render_template
from models import db, Admin, Reservation
from reservation.routes import res_bp

import os


#import packages we created for the admin and reservatib blueprints
from admin.routes import admin_bp
from reservation.routes import res_bp
from admin.routes import admin_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'reservations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

#register blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(res_bp, url_prefix='/reservation')

@app.route('/', methods=['GET'])
def index():
   
 
  return render_template('index.html')

with app.app_context():
    db.create_all()



#run the application
if  __name__ == '__main__':
    app.run(host = "0.0.0.0")


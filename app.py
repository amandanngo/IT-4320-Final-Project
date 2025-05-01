from flask import Flask, render_template
from models import db
from reservation.routes import res_bp

#import packages we created for the admin and reservatib blueprints
from admin.routes import admin_bp
from reservation.routes import res_bp
from admin.routes import admin_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#register blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(res_bp, url_prefix='/reservation')

@app.route('/', methods=['GET'])
def index():
   
 
    return render_template('index.html')


#run the application
if  __name__ == '__main__':
    app.run(debug=True,port=5016)


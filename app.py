from flask import Flask

#import packages we created for the admin and reservatib blueprints
from admin.routes import admin_bp
from reservation.routes import res_bp

app = Flask(__name__)

#register blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(res_bp, url_prefix='/reservation')

#run the application
if  __name__ == '__main__':
    app.run(debug=True,port=5016)


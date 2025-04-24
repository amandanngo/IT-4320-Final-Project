#routes/views for the main sections of the app
from flask import Blueprint, render_template

#Set up SQLAlchemy


res_bp = Blueprint('reservation', __name__, template_folder='templates', url_prefix='/reservation')

#Create entry in 'reservations' table in db
@res_bp.route('/create', methods=['POST'])
def reservation_create():
    #Get info from form
    
    #Generate confirmation code
  
    #Add entry using SQLAlchemy

    #Display order confirmation on page
    
    pass

@res_bp.route('/delete/<int:id>', methods=['POST'])
def reservation_delete(id):
    #get the task based on id

    #delete the task
    
    pass

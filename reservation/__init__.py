from flask import Blueprint

# Create the reservation blueprint
res_bp = Blueprint('reservation', __name__, template_folder='templates', url_prefix='/reservation')

# Import routes to register them with the blueprint
from . import routes

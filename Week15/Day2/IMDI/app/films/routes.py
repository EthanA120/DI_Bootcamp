from flask import render_template, Blueprint

films = Blueprint('films', __name__, url_prefix="/films", template_folder='templates', static_folder='static')


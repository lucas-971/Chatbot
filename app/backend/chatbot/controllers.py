from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
    print('eee')
    return render_template('index.html', name="Bot")
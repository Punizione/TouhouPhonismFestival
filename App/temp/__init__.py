""" temp music folder """

from flask import Blueprint, render_template


music_bp = Blueprint('music', __name__,
						url_prefix='/music',
						static_url_path='/',
						static_folder='./',
						template_folder='./'
						)

@music_bp.route('/')
def index():
	return render_template('index.html')
from flask import Blueprint, render_template
from flask import request

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    query = request.args.get('query')
    if query is None:
        return render_template('base.html')
    API_KEY = 'AIzaSyCSeh4VV3_OrZFXrhj9dgr32-miMWyeKiM'
    SEARCH_ENGINE_ID = '349dd0a468c6430c'
    start = 1 
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    data = request.get(url).json()
    return data 


from flask import Blueprint, render_template
from flask import request
from .models import Result 

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
    #convert JSON response to an array of Result objections and return that array 
    search_items = data.get('items')
    results = []
    for i, search_item in enumerate(search_items, start=1):
        try:
            long_description = search_item["pagemap"]["metatags"][0]["og:description"]
        except KeyError:
            long_description = "N/A"
        print(long_description)
        results.append(Result(title=search_item.get("title"),description=long_description, snippet=search_item.get("snippet"),url=search_item.get("link")))
    return render_template('response_view.html', results=results)
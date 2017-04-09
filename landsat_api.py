import feedparser as fp
from flask import Flask
from flask.ext.cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def helloworld():
	return 'Hello!'

@app.route('/api/landsat')
def landsat_rss():
	feed = fp.parse('https://landsat.usgs.gov/landsat/rss/Landsat_L1T.rss')
	number_of_entries = len(feed.entries)

    response = jsonify([serialize_landsat_entry(entry) for entry in feed.entries])
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


def serialize_landsat_entry(entry):
	return {
        'title': entry.title,
        'latitude': float(entry.geo_lat),
        'longitude': float(entry.geo_long),
        'imageLink': entry.id,
    }

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)


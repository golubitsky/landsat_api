import feedparser as fp
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def helloworld():
	return 'Hello!'

@app.route('/api/landsat')
def landsat_rss():
	feed = fp.parse('https://landsat.usgs.gov/landsat/rss/Landsat_L1T.rss')
	number_of_entries = len(feed.entries)

	return jsonify([serialize_landsat_entry(entry) for entry in feed.entries])


def serialize_landsat_entry(entry):
	return {
        'title': entry.title,
        'latitude': float(entry.geo_lat),
        'longitude': float(entry.geo_long),
        'imageLink': entry.id,
    }

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)


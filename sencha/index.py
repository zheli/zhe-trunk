import os, logging
import simplejson as json

from google.appengine.dist            import use_library
use_library('django', '1.2')

from google.appengine.ext.webapp      import template
from google.appengine.ext             import webapp
from google.appengine.api             import urlfetch
from google.appengine.ext.webapp.util import run_wsgi_app

ROOT_PATH = os.path.dirname(__file__)
TEMPLATE = os.path.join(ROOT_PATH, 'templates')

class MainPage(webapp.RequestHandler):
    def get(self):
        index_page = os.path.join(TEMPLATE, 'index.html')
        template_values = {}
        self.response.out.write(template.render(index_page, template_values))

class get_station(webapp.RequestHandler):
    def get(self):
        url = 'https://api.trafiklab.se/samtrafiken/resrobot/StationsInZone.json?key=70ce12e0a6549010b4b38e00848ab8aa&centerX=11.980084&centerY=57.709185&radius=500&coordSys=WGS84&apiVersion=2.1'
        result = urlfetch.fetch(url).content
        logging.info(result)
        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
        self.response.out.write(json.dumps(trim(json.loads(result)["stationsinzoneresult"]), indent=2))

def trim(data):
    bus_station = []
    blacklist = ['rtDate', 'bgColor', 'stroke', 'fgColor', 'JourneyDetailRef', \
        'id', 'date', 'type', 'routeIdx']
    #Remove Train Station
    for station in data.get(u'location'):
        if not station.get(u'stationinfo'):
            bus_station.append(station)
#    for key in blacklist:
#        for trip in bus_trip:
#            if key in trip: 
#                del trip[key]
#            if key in trip.get('Origin'):
#                del trip.get('Origin')[key]
#            if key in trip.get('Destination'):
#                del trip.get('Destination')[key]

    return bus_station

routes = [
        ('/', MainPage),
        ('/get_station/', get_station)
        ]
application = webapp.WSGIApplication(routes, debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

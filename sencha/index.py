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

class get_buses(webapp.RequestHandler):
    def get(self):
        #url = 'https://api.trafiklab.se/samtrafiken/resrobot/StationsInZone.json?key=70ce12e0a6549010b4b38e00848ab8aa&centerX=11.980084&centerY=57.709185&radius=500&coordSys=WGS84&apiVersion=2.1'
        url = 'https://api.trafiklab.se/samtrafiken/resrobotstops/GetDepartures.json?key=c97a3f0255bfa5f758df1b2d4f0ccdca&apiVersion=2.2&locationId=7425695&coordSys=WGS84'
        bus_data = urlfetch.fetch(url).content
        logging.info(bus_data)
        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
        #result = dict(buses = transform_bus_list(json.loads(bus_data)))
        result = transform_bus_list(json.loads(bus_data))
        self.response.out.write(json.dumps(result, indent=2))

def transform_bus_list(bus_data):
    bus_list = []
    blacklist = ['rtDate', 'bgColor', 'stroke', 'fgColor', 'JourneyDetailRef', \
        'id', 'date', 'type', 'routeIdx']
    #Remove Train Station
    buses = bus_data.get(u'getdeparturesresult').get(u'departuresegment')
    if buses:
        for bus in buses:
            bus_list.append(dict(
                id = bus[u'segmentid'][u'carrier'][u'id'],
                number = bus[u'segmentid'][u'carrier'][u'number'],
                type = bus[u'segmentid'][u'mot'][u'#text'],
                departure_time = bus[u'departure'][u'datetime'],
                direction = bus[u'direction'],
                station_name = bus[u'departure'][u'location'][u'name'],
                station_id = bus[u'departure'][u'location'][u'@id'],
                x = bus[u'departure'][u'location'][u'@x'],
                y = bus[u'departure'][u'location'][u'@y']
                ))
            #break
        logging.info(bus_list)
        return bus_list
    else:
        return None

routes = [
        ('/', MainPage),
        ('/get_buses', get_buses)
        ]
application = webapp.WSGIApplication(routes, debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

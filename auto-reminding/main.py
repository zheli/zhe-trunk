#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from app_settings import *
from facebook_sdk import Facebook, FacebookApiError
from vasttrafik_sdk import vast_trafik
import urllib
import logging
import webapp2
import webapp2_extras.local
from django.utils import simplejson as json
from google.appengine.api import urlfetch
from datetime import datetime

fb = Facebook(app_id = app_id, app_secret = app_secret)
vt = vast_trafik(app_key = vt_api_key)

class main_handler(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
        try:
            result = fb.api(u'/me/events')
        except FacebookApiError:
            self.response.headers.add_header('content-type', 'text/html', charset='utf-8')
            self.response.out.write('<a href="/auth/">Connect Your Facebook Account</a>')
            #return webapp2.redirect('/auth/')
        else:
            #TODO: Get address from result, geocode it and get the coordinates
            event_id = result.get(u'data','')[0].get(u'id', '')
            event_data = fb.api(u'/%s' % event_id)
            del event_data['end_time']
            dest = event_data.get(u'venue')
            event_time = datetime.strptime(event_data.get(u'start_time', ''), "%Y-%m-%dT%H:%M:%S")
            bus_trips = trim(vt.trip(
                    origin_lat = 57.70822,
                    origin_lon = 11.93862,
                    origin_name = u'Start',
                    dest_lat = dest.get(u'latitude'), #57.660211,
                    dest_lon = dest.get(u'longitude'), #11.917849,
                    dest_name = u'End',
                    time = '%02d:%02d' % (event_time.hour, event_time.minute),
                    date = '%4d-%02d-%02d' % (event_time.year, event_time.month, event_time.day),
                    search_for_arrival = 1,
                    num_trips = 1))
            bus_trips = dict(trips = bus_trips)
            event_data.update(bus_trips)
            self.response.out.write(json.dumps(event_data, indent=2))
        
class fb_auth(webapp2.RequestHandler):
    def get(self):
        fb_code = self.request.get('code', '')
        if not fb_code:
            self.response.headers['Content-Type'] = 'text/html'
            url =\
             'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&scope=user_events' % (app_id, app_url)                                           
            logging.debug('"Code" var doesnt exist!')
            self.response.out.write('<script>top.location.href = "%s" </script>' % url)
            #self.response.out.write('redirect')
        else:
            url = \
            'https://graph.facebook.com/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s' % (app_id, app_url, app_secret, fb_code)
            result = urlfetch.fetch(url)
            (fb.access_token, expire_time) = result.content.split('&')
            fb.access_token = fb.access_token[13:]
            logging.debug('"Code" var exists!')
            return webapp2.redirect('/')

def geocoding(address = None):
    logging.info('Querying Location [%s]...' % address)
    query = urllib.urlencode(dict(q=address.encode('utf-8')))
    url = 'http://where.yahooapis.com/geocode?%s&appid=%s&flags=CGJ' % (query, yahoo_api_key)
    #params = {
    #        'q': address,
    #        'appid': yahoo_api_key,
    #        'flags': 'CGJ',
    #        }
    logging.debug('fetching [%s]...' % url)
    response = urlfetch.fetch(url).content
    logging.info(response)
    return json.loads(response)
    #return dict(lat = 57.707451, lon = 11.934790)

def trim(data):
    bus_trip = []
    blacklist = ['rtDate', 'bgColor', 'stroke', 'fgColor', 'JourneyDetailRef', \
        'id', 'date', 'type', 'routeIdx']
    for trip in data.get(u'TripList').get(u'Trip').get(u'Leg'):
        if trip.get(u'type') != 'WALK':
            bus_trip.append(trip)
    for key in blacklist:
        for trip in bus_trip:
            if key in trip: 
                del trip[key]
            if key in trip.get('Origin'):
                del trip.get('Origin')[key]
            if key in trip.get('Destination'):
                del trip.get('Destination')[key]
                    
    return bus_trip

def main():
    routes = [
        (r'/', main_handler),
        (r'/auth/', fb_auth),
        ]
    application = webapp2.WSGIApplication(routes = routes, debug=True)
    application.run()


if __name__ == '__main__':
    main()


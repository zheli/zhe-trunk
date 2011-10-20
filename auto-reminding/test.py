# -*- encoding: utf-8 -*-
import json

data = """
{
"TripList":{
  "noNamespaceSchemaLocation":"http://api.vasttrafik.se/v1/hafasRestTrip.xsd",
  "Trip":{
    "Leg":[{
      "name":"Walk",
      "type":"WALK",
      "Origin":{
        "name":"Start",
        "type":"ADR",
        "time":"09:20",
        "date":"2011-10-10"
        },
      "Destination":{
        "name":"Lindholmen, Göteborg",
        "type":"ST",
        "id":"9022014004490001",
        "time":"09:21",
        "date":"2011-10-10"
        }
      },{
      "name":"Walk",
      "type":"WALK",
      "Origin":{
        "name":"Lindholmen, Göteborg",
        "type":"ST",
        "id":"9022014004490001",
        "time":"09:21",
        "date":"2011-10-10"
        },
      "Destination":{
        "name":"Lindholmen, Göteborg",
        "type":"ST",
        "id":"9022014004490004",
        "time":"09:21",
        "date":"2011-10-10"
        }
      },{
      "name":"Buss 99",
      "type":"BUS",
      "id":"9015002009900032",
      "direction":"Frölunda Torg",
      "fgColor":"#003273",
      "bgColor":"#ffffff",
      "stroke":"Solid",
      "Origin":{
        "name":"Lindholmen, Göteborg",
        "type":"ST",
        "id":"9022014004490004",
        "routeIdx":"8",
        "time":"09:21",
        "date":"2011-10-10",
        "track":"D "
        },
      "Destination":{
        "name":"Frölunda Torg, Göteborg",
        "type":"ST",
        "id":"9022014002530011",
        "routeIdx":"18",
        "time":"09:42",
        "date":"2011-10-10",
        "track":"K "
        },
      "JourneyDetailRef":{
        "ref":"http://api.vasttrafik.se/bin/rest.exe/v1/journeyDetail?ref=13986%2F7773%2F813626%2F402151%2F80%3Fdate%3D2011-10-10%26station_evaId%3D4490004%26station_type%3Ddep%26authKey%3Dbf776963-e764-451a-9cf4-25128ae817b1%26format%3Djson%26jsonpCallback%3D%26"
        }
      },{
      "name":"Walk",
      "type":"WALK",
      "Origin":{
        "name":"Frölunda Torg, Göteborg",
        "type":"ST",
        "id":"9022014002530011",
        "time":"09:47",
        "date":"2011-10-10"
        },
      "Destination":{
        "name":"Frölunda Torg, Göteborg",
        "type":"ST",
        "id":"9022014002530001",
        "time":"09:47",
        "date":"2011-10-10"
        }
      },{
      "name":"Spårvagn 1",
      "type":"TRAM",
      "id":"9015002000100069",
      "direction":"Östra Sjukhuset",
      "fgColor":"#ffffff",
      "bgColor":"#ffffff",
      "stroke":"Solid",
      "Origin":{
        "name":"Frölunda Torg, Göteborg",
        "type":"ST",
        "id":"9022014002530001",
        "routeIdx":"3",
        "time":"09:49",
        "date":"2011-10-10",
        "track":"A "
        },
      "Destination":{
        "name":"Musikvägen, Göteborg",
        "type":"ST",
        "id":"9022014004870001",
        "routeIdx":"5",
        "time":"09:51",
        "date":"2011-10-10",
        "track":"A "
        },
      "JourneyDetailRef":{
        "ref":"http://api.vasttrafik.se/bin/rest.exe/v1/journeyDetail?ref=889419%2F300022%2F533220%2F29863%2F80%3Fdate%3D2011-10-10%26station_evaId%3D2530001%26station_type%3Ddep%26authKey%3Dbf776963-e764-451a-9cf4-25128ae817b1%26format%3Djson%26jsonpCallback%3D%26"
        }
      },{
      "name":"Walk",
      "type":"WALK",
      "Origin":{
        "name":"Musikvägen, Göteborg",
        "type":"ST",
        "id":"9022014004870001",
        "time":"09:51",
        "date":"2011-10-10"
        },
      "Destination":{
        "name":"Musikvägen, Göteborg",
        "type":"ST",
        "id":"9022014004870002",
        "time":"09:51",
        "date":"2011-10-10"
        }
      },{
      "name":"Walk",
      "type":"WALK",
      "Origin":{
        "name":"Musikvägen, Göteborg",
        "type":"ST",
        "id":"9022014004870002",
        "time":"09:51",
        "date":"2011-10-10"
        },
      "Destination":{
        "name":"End",
        "type":"ADR",
        "time":"09:55",
        "date":"2011-10-10"
        }
      }]
    }
  }
}
"""

trip = json.loads(data)
counter = 0
bus_trip = []
for item in trip.get(u'TripList').get(u'Trip').get(u'Leg'):
    if item.get(u'type') != 'WALK':
        bus_trip.append(item)
print(bus_trip)        
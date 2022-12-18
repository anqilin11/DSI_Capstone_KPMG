import json
import urllib.parse
import urllib.request
import requests
import pandas as pd
import numpy as np

MAPQUEST_API_KEY = "J3mUQvH3EFyMQvkFgcAYpZGaighdGjZP"

BASE_MAPQUEST_URL = "http://www.mapquestapi.com/"

# function to build url with positions
def build_search_url_pos(start_posi, end_posi) -> str:
    query_parameters = [('key',MAPQUEST_API_KEY),('from',start_posi),('to',end_posi)]
    return BASE_MAPQUEST_URL +"directions/v2/route?" + urllib.parse.urlencode(query_parameters)

# function to build url with lat&long
def build_search_url_latlong(start_lat:str, start_lon:str, 
                     ends_lat:str, ends_lon:str) -> str:
    query_parameters = [('key',MAPQUEST_API_KEY),('from',start_lat+','+start_lon),('to',ends_lat+','+ends_lon)]
    return BASE_MAPQUEST_URL +"directions/v2/route?" + urllib.parse.urlencode(query_parameters)


# function to build url with start position and end lat long
def build_search_url_pos_latlong(start_posi, 
                       ends_lat:str, ends_lon:str) -> str:
    query_parameters = [('key',MAPQUEST_API_KEY),('from',start_posi),('to',ends_lat+','+ends_lon)]
    return BASE_MAPQUEST_URL +"directions/v2/route?" + urllib.parse.urlencode(query_parameters)

# function that get the web result(dictionary) of MAPQUEST
def get_result(url: str) -> dict:
    result = None
    try:
        result = urllib.request.urlopen(url)
        json_text = result.read().decode(encoding = 'utf-8')
#        print(json_text)
        return json.loads(json_text)

    finally:
        if result != None:
            result.close()
            
# get distance, units in miles
def get_route_distance(json_result):
    dis = json_result['route']['distance']
    return dis


def build_corridor_search_url() -> str:
    query_parameters = [('key', MAPQUEST_API_KEY)]
    return BASE_MAPQUEST_URL +"search/v2/corridor?" + urllib.parse.urlencode(query_parameters)

def build_corridor_search_body(sessionId, dataList, width=10) -> str:
    json_map = {
        "sessionId": sessionId,
        "remoteDataList": dataList,
        "options": {
            "width": str(width),
            "units": 'm',
            "maxMatches": 500
        }
    }
    return json.dumps(json_map)

def post_corridor_search_request(sessionId, dataList, width=10):
    result = None
    url = build_corridor_search_url()
    body = build_corridor_search_body(sessionId, dataList, width)
    try:
        result = requests.post(url, body)
        return result.json()

    finally:
        if result != None:
            result.close()

def getRemoteDataList(df,lt,lg,name):
  df['shapePoints'] = df.apply(lambda x: [x[lt],x[lg]],axis=1)
  remoteDataList = []
  for row in range(df.shape[0]):
    inner = {}
    r_data = df.iloc[row]
    inner['key'] = str(row)
    inner['name'] = str(r_data[name])
    inner['shapePoints'] = r_data['shapePoints']
    remoteDataList.append(inner)
  return remoteDataList



def build_radius_search_url() -> str:
    query_parameters = [('key', MAPQUEST_API_KEY)]
    return BASE_MAPQUEST_URL +"search/v2/radius?" + urllib.parse.urlencode(query_parameters)

def build_radius_search_body(origin, dataList, radius=10) -> str:
    json_map = {
        "origin": {
            "latLng": { 
                "lat": origin[0], 
                "lng": origin[1]
            }
        },
        "remoteDataList": dataList,
        "options": {
            "radius": str(radius),
            "units": 'm',
            "maxMatches": 500
        }
    }
    return json.dumps(json_map)

def post_radius_search_request(origin, dataList, radius=10):
    result = None
    url = build_radius_search_url()
    body = build_radius_search_body(origin, dataList, radius)
    try:
        result = requests.post(url, body)
        return result.json()

    finally:
        if result != None:
            result.close()


def get_closest_exit(origin, exitList):
    exit_result = post_radius_search_request(origin, exitList)
    if exit_result['resultsCount'] > 0:
      filtered_exits = pd.DataFrame(exit_result['searchResults'])
      closest_exit = filtered_exits.iloc[filtered_exits['distance'].argmin()]
      return closest_exit['distance'], closest_exit['name'], closest_exit['shapePoints'] 
    else:
      return np.NaN, np.NaN, [np.NaN,np.NaN]

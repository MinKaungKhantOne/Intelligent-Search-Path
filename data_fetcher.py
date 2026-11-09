import json

import requests

def get_geocode(city):
    API_KEY = "ZiZDneNn2gj7Fpe9CoPJ0wXGWMiitE7UeaE670yaTxGWCWMGLvu175CRNipselUP"
    url = "https://api.distancematrix.ai/maps/api/geocode/json"
    params = {
        'address': city + ", Myanmar",
        'key': API_KEY,
    }
    response = requests.get(url=url,params=params)
    geocode_data = response.json()
    return {
        'lat': geocode_data['result'][0]['geometry']['location']['lat'],
        'lng': geocode_data['result'][0]['geometry']['location']['lng']
    }

#https://api.distancematrix.ai/maps/api/distancematrix/json?origins=51.4822656,-0.1933769&destinations=51.4994794,-0.1269979&key=c1eM2L6hX9xqM1wzgPswA7YSpn9dEhkN6WYbUy1mNwiy6om2DWO2v30GEcmsHwCS
def get_distance(origins, destinations):
    API_KEY = "c1eM2L6hX9xqM1wzgPswA7YSpn9dEhkN6WYbUy1mNwiy6om2DWO2v30GEcmsHwCS"
    url= "https://api.distancematrix.ai/maps/api/distancematrix/json"
    params = {
        'origins': origins,
        'destinations': destinations,
         'key': "c1eM2L6hX9xqM1wzgPswA7YSpn9dEhkN6WYbUy1mNwiy6om2DWO2v30GEcmsHwCS",
     }
    response = requests.get(url=url,params=params)
    distance_data = response.json()
    return(float(distance_data['rows'][0]['elements'][0]['distance']['text'][:-3]))

cities = [
    'Hinthada', 'Meiktila',
    'Bagan', 'Taunggyi',
    'Lashio', 'Mudon',
    'Pyay', 'Pyin Oo Lwin',
    'Mawlamyine', 'Thaton',
    'Yangon', 'Bago',
    'Loikaw', 'Mandalay',
    'Phyu', 'Naypyidaw',
    'Mrauk-U', 'Magway',
    'Taungoo', 'Mogok',
    'Pathein', 'Hpa-An'
]
connections = [
    # Central Myanmar
    ("Mandalay", "Bagan"),
    ("Mandalay", "Meiktila"),
    ("Mandalay", "Pyin Oo Lwin"),
    ("Mandalay", "Mogok"),
    ("Mandalay", "Lashio"),

    ("Bagan", "Magway"),
    ("Meiktila", "Naypyidaw"),
    ("Meiktila", "Taunggyi"),
    ("Pyin Oo Lwin", "Lashio"),
    ("Magway", "Pyay"),

    # Central to Southern
    ("Naypyidaw", "Taungoo"),
    ("Naypyidaw", "Taunggyi"),
    ("Taungoo", "Phyu"),
    ("Taungoo", "Bago"),
    ("Phyu", "Bago"),

    ("Pyay", "Bago"),
    ("Pyay", "Hinthada"),

    # Yangon / Delta
    ("Yangon", "Bago"),
    ("Yangon", "Pathein"),
    ("Yangon", "Hinthada"),
    ("Yangon", "Mawlamyine"),
    ("Pathein", "Hinthada"),

    # Mon / Kayin
    ("Bago", "Thaton"),
    ("Thaton", "Hpa-An"),
    ("Thaton", "Mawlamyine"),
    ("Hpa-An", "Mawlamyine"),
    ("Mawlamyine", "Mudon"),

    # Shan / Kayah
    ("Taunggyi", "Loikaw"),
    ("Taunggyi", "Lashio"),
    ("Loikaw", "Naypyidaw"),

    # Western Myanmar
    ("Mrauk-U", "Bagan"),
]

def get_map_data(cities, connections):
    map_data = {'cities':{}}

    # making coordinates for cities
    for city in cities:
        map_data['cities'][city] = get_geocode(city)

    a_list = []
    b_list = []
    for a, b in connections:
        a_list.append(a)
        b_list.append(b)
    a_list = set(a_list)
    b_list = set(b_list)

    map_data['graph'] = {}
    for a in a_list:
        map_data['graph'][a] = {}
        for connection in connections:
            if connection[0] == a:
                map_data['graph'][a][connection[1]] = 0
                origin_coordinate = f"{map_data['cities'][a]['lat']},{map_data['cities'][a]['lng']}"
                destination_coordinate = f"{map_data['cities'][connection[1]]['lat']},{map_data['cities'][connection[1]]['lng']}"
                map_data['graph'][a][connection[1]] = get_distance(origin_coordinate,destination_coordinate)

    for b in b_list:
        if not (b in map_data['graph'].keys()):
            map_data['graph'][b] = {}
        for connection in connections:
            if connection[1] == b:
                map_data['graph'][b][connection[0]] = 0
                map_data['graph'][b][connection[0]] = map_data['graph'][b][connection[0]] = map_data['graph'][connection[0]].get(b)

    return map_data

with open('map_data.json', 'w') as f:
    json.dump(get_map_data(cities, connections), f, indent=4)
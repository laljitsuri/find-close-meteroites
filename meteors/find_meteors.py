import math
import requests

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def get_distance(meteor):
    return(meteor.get('dist',math.inf))

if __name__ == '__main__':
    my_location = (-38.272689,144.84375)

    meteor_response = requests.get('https://data.nasa.gov/resource/y77d-th95.json')

    meteor_data = meteor_response.json()

    for meteor in meteor_data:
        if not meteor.get('reclat') or not meteor.get('reclong'):continue
        d=distance((my_location[0],my_location[1]),(float(meteor.get('reclat')),float(meteor.get('reclong'))))
        meteor['dist']=d

    meteor_data.sort(key=get_distance)

    print(meteor_data[0:10])
    print("\nThe nearest ten distances are \n")
    for i in range(0,10):print(meteor_data[i].get('dist'))

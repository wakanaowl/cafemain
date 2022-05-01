

from mapapi_files.parsejson import parsejson

from mapapi_files.process import process


def index():
    loc = {
	"lat": 35.6619707,
	"lng": 139.703795
}

    place_result = process(loc)
    json_data= parsejson(place_result)
    return json_data

index()
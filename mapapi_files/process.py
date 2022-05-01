from mapapi_files.createClient import createClient


def process(loc):
    client = createClient()
    place_results = client.places_nearby(
        location=loc, radius=100, keyword='カフェ', language='ja')
    
    return place_results


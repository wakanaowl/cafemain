import googlemaps

def createClient():
    api_key = "AIzaSyA-XS7P52yc7vUcY5JseKJViysWO-jEjMk"
    client = googlemaps.Client(api_key)
    return client
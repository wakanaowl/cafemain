from mapapi_files.createClient import createClient

def parsejson(place_results):
    
    jsonify = ({
        "data":[],
        "photos":[]
        })

    photoreference_array = ({
        "photo":[]
        })
    

    client = createClient()
    key = 0
    try:
        for i in place_results['results']:
            try:
                place_detail = client.place(place_id=i['place_id'])
                for n in place_detail['result']['photos']:
                    jsonify['photos'].append(n['photo_reference'])
                
                
                add_data=({
                    "name": i['name'],
                    "googlelink" : place_detail['result']['url'],
                    "locationX" : i['geometry']['location']['lng'],
                    "locationY": i['geometry']['location']['lat'],
                    "website" : place_detail['result']['website'],
                    "adress": i['vicinity']
                })

                jsonify['data'].append(add_data)
                # jsonify['photos'].append(photoreference_array)
                if(key == 0):
                    return jsonify
            except:
                return 0
            pass
    except:
        return 0
        
    return jsonify
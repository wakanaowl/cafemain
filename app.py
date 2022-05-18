from crypt import methods
from flask import Flask
from flask_cors import CORS
from flask import request
from database_files.cafeinsert import cafe_insert
from mapapi_files.parsejson import parsejson
from mapapi_files.process import process
from database_files.createuser import create_user
from database_files.follow import follow
from database_files.love import love_cafes
from database_files.photorefe_to_cafeid import photorefe_to_cafeid
from database_files.search_user import search_users
from database_files.find_followee import find_followee
from database_files.useralldata import useralldata
from database_files.id_test import insert_users
from database_files.timeline_info import timeline_info
from database_files.follow_info import follow_infomation
from database_files.cafe_info import cafe_get_by_cafeid

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/testid',methods = ['POST'])
def insert():
    json_data = request.json
    insert_users(json_data)

    return json_data
    

@app.route('/insert_cafe', methods=['POST'])
def search_cafe():
    if request.method == 'POST':
        loc = request.json
    else:
        return "methodnotallowed"
    print(loc['loc'],loc['uid'])
    place_result = process(loc['loc'])
    json_data = parsejson(place_result)
    if(json_data == 0):
        return "近くにカフェがありません"
    dbdata = cafe_insert(json_data,loc['uid'])
    print(dbdata)
    return json_data


@app.route('/user_followings',methods=['POSt'])
def user_followings():
    json_data = request.json
    i = follow(json_data["followee"],json_data["follower"])
    return i 

@app.route('/follow_by_qr',methods=['GET'])
def follow_by_qr():
    folowee = request.args.get('followee', '')
    folower = request.args.get('follower','')
    print(folower)
    print(folowee)
    i = follow(folowee,folower)
    return i

@app.route('/love',methods=['POST'])
def love():
    json_data = request.json
    print(json_data)
    i = love_cafes(json_data)
    return i

@app.route('/createuser',methods=['POST'])
def cerate():
    json_data = request.json
    print(json_data)
    i = create_user(json_data)
    return i


@app.route('/serchuser',methods=['GET'])
def serchuser():
    uid = request.args.get('uid', '')
    i = search_users(uid)
    return i


@app.route('/findfollowee',methods=['POST'])
def find_followee123():
    if request.method == 'POST':
        return_json = find_followee(request.json["id_json"])
    return return_json

@app.route('/followinfo',methods=['POST'])
def get_info():
    if request.method == 'POST':
        return_json = follow_infomation(request.json["id_json"])
    return return_json

@app.route('/getcafe_by_cafeid',methods=['POST'])
def getdafe_by_cafeid():
    if request.method == 'POST':
        return_json = cafe_get_by_cafeid(request.json["cafeid"])
    return return_json

@app.route('/home_screen',methods=['POST'])
def get_timeline_info():
    if request.method == 'POST':
        return_json = timeline_info(request.json["id_json"])
    return return_json

@app.route('/useralldata', methods=['POST'])
def useralldatas():
    if request.method == 'POST':
        return_json = useralldata(request.json["uid"])
    return return_json

@app.route('/photorefe_to_cafe', methods=['POST'])
def photorefe_to_cafe():
    if request.method == 'POST':
        return_json = photorefe_to_cafeid(request.json["photorefe"])
    return return_json

# @app.route('/followeephoto',methods=['POST'])
# def get_flloweecafe_photo():
#     if request.method == 'POST':
#         floweeids = find_followeeee(request.json["id_json"])
#         fname = find_followee_name(request.json["id_json"])
#         cafeids = fllowee_visited_cafes(floweeids)
#         return_json = fllowee_cafe_photos(fname,cafeids)
#     return return_json


if __name__ == '__main__':
    app.run()
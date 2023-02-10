from flask import Flask, request, jsonify

from Adapter.databaseProcessor import DatabaseProcessor
from orm import Database

app = Flask(__name__)
dbConnector = Database()
databaseProcessor = DatabaseProcessor()


@app.route('/parkinglot', methods=['POST'])
def insert_parking_lot():
    if request.is_json:
        if databaseProcessor.insert_one_parking_field(request.get_json()):
            return jsonify({'status': 200, 'info': "Insert Success"})
        else:
            return jsonify({'status': 404, 'info': "Insert Fail"})
    else:
        return jsonify({'status': 404, 'info': "Body not json"})


@app.route("/user", methods=["POST"])
def insert_user():
    if request.is_json:
        if databaseProcessor.insert_one_user(request.get_json()):
            return jsonify({'status': 200, 'info': "Insert Success"})
        else:
            return jsonify({'status': 404, 'info': "Insert Fail"})
    else:
        return jsonify({'status': 404, 'info': "Body not json"})


@app.route("/car", methods=["POST"])
def insert_car():
    if request.is_json:
        if databaseProcessor.insert_one_car(request.get_json()):
            return jsonify({'status': 200, 'info': "Insert Success"})
        else:
            return jsonify({'status': 404, 'info': "Insert Fail"})
    else:
        return jsonify({'status': 404, 'info': "Body not json"})


@app.route("/all-user", methods=["GET"])
def get_users():
    result = databaseProcessor.get_all_user()
    if result:
        return {"data": result, 'status': 200, 'info': "Search Success"}
    else:
        return jsonify({'status': 404, 'info': "Search Fail"})


@app.route("/check-user", methods=["POST"])
def check_user():
    if request.is_json:
        result = databaseProcessor.check_user_exist(request.get_json())[0]
        if result:
            return jsonify({"data": [{"exist": result}], 'status': 200, 'info': "Search Success"})
        else:
            return jsonify({'status': 404, 'info': "Search Fail"})
    else:
        return jsonify({'status': 404})


@app.route("/user-password", methods=["POST"])
def user_password():
    if request.is_json:
        reqJson = request.get_json()
        result = dbConnector.get_password(reqJson['data'][0]["email"])
        print(result)
        return jsonify({"data": [{
            "exist": result
        }],
            'status': 200})
    else:
        return jsonify({'status': 304})


@app.route("/available", methods=["POST"])
def find_available():
    if request.is_json:
        reqJson = request.get_json()
        lot = reqJson["data"][0]["parking_lot"]
        result = dbConnector.find_available_spots(lot)
        return jsonify({'result': result, 'status': 200})
    else:
        return jsonify({'status': 404})


if __name__ == "__main__":
    app.run()

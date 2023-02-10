from flask import Flask, request, jsonify

from Adapter.databaseProcessor import DatabaseProcessor
from orm import Database

app = Flask(__name__)
dbConnector = Database()
databaseProcessor = DatabaseProcessor()


@app.route('/parking/field', methods=['POST'])
def insert_parking_field():
    if request.is_json:
        if databaseProcessor.insert_one_parking_field(request.get_json()):
            return jsonify({'status': 200, 'info': "Insert Success"})
        else:
            return jsonify({'status': 404, 'info': "Insert Fail"})
    else:
        return jsonify({'status': 404, 'info': "Body not json"})


@app.route('/parking/field', methods=['GET'])
def get_parking_field():
    result = databaseProcessor.get_parking_field()
    if result:
        return jsonify({'data': result, 'status': 200, 'info': "Search Success"})
    else:
        return jsonify({'status': 404, 'info': "Search Fail"})


@app.route("/user", methods=["POST"])
def insert_user():
    if request.is_json:
        if databaseProcessor.insert_one_user(request.get_json()):
            return jsonify({'status': 200, 'info': "Insert Success"})
        else:
            return jsonify({'status': 404, 'info': "Insert Fail"})
    else:
        return jsonify({'status': 404, 'info': "Body not json"})


@app.route("/user/<userID>/car", methods=["GET"])
def find_cars_by_id(userID):
    result = databaseProcessor.get_cars_by_userId(userID)
    if result is not False:
        return jsonify({'data': result, 'status': 200, 'info': "search Success"})
    else:
        return jsonify({'status': 404, 'info': "search Fail"})


@app.route("/user/<userID>/car/<plate>", methods=["POST"])
def insert_car(userID, plate):
    if databaseProcessor.insert_one_car(userID, plate):
        return jsonify({'status': 200, 'info': "Insert Success"})
    else:
        return jsonify({'status': 404, 'info': "Insert Fail"})


@app.route("/user/all", methods=["GET"])
def get_users():
    result = databaseProcessor.get_all_user()
    if result:
        return {"data": result, 'status': 200, 'info': "Search Success"}
    else:
        return jsonify({'status': 404, 'info': "Search Fail"})


@app.route("/user/<email>/check", methods=["GET"])
def check_user(email):
    result = databaseProcessor.check_user_exist(email)
    if result:
        result = result[0]
        return jsonify({"data": [{"exist": result}], 'status': 200,
                        'info': "Search Success"})
    else:
        return jsonify({'status': 404, 'info': "Search Fail"})


@app.route("/user/<email>/password", methods=["GET"])
def user_password(email):
    result = databaseProcessor.get_one_user_password(email)
    if result:
        return jsonify({"data": [{"exist": result}],
                        'status': 200})
    else:
        return jsonify({'status': 404, 'info': "Get Fail"})


@app.route("/parking/slot/<field>/available", methods=["GET"])
def find_available(field):
    result = databaseProcessor.get_one_available_packing_slot_in_field(field)
    if result:
        return jsonify({'data': [{"parking_slot": result}], 'status': 200, 'info': "Search Success"})
    else:
        return jsonify({'status': 404, 'info': "Search Fail"})


@app.route("/user/search/<account>", methods=["GET"])
def search_user(account):
    result = databaseProcessor.search_one_user(account)
    return jsonify({'data': result, 'status': 200, 'info': "Search Success"})


@app.route("/parking/field/in/<name>", methods=["PATCH"])
def parking_field_minus(name):
    if databaseProcessor.parking_lots_minus(name):
        return jsonify({'status': 200, 'info': "Change Success"})
    else:
        return jsonify({'status': 400, 'info': "Change Failed"})


@app.route("/parking/field/out/<name>", methods=["PATCH"])
def parking_field_add(name):
    if databaseProcessor.parking_lots_add(name):
        return jsonify({'status': 200, 'info': "Change Success"})
    else:
        return jsonify({'status': 400, 'info': "Change Failed"})


@app.route("/parking/history", methods=["POST"])
def insert_parking_history():
    if request.is_json:
        if databaseProcessor.insert_much_parking_history(request.get_json()):
            return jsonify({'status': 200, 'info': "Insert Success"})
        else:
            return jsonify({'status': 404, 'info': "Insert Fail"})
    else:
        return jsonify({'status': 404, 'info': "Body not json"})


@app.route("/parking/history", methods=["PATCH"])
def update_much_parking_history():
    if request.is_json:
        if databaseProcessor.update_much_parking_history(request.get_json()):
            return jsonify({'status': 200, 'info': "Update Success"})
        else:
            return jsonify({'status': 404, 'info': "Update Fail"})
    else:
        return jsonify({'status': 404, 'info': "Body not json"})


@app.route("/parking/slot", methods=["PATCH"])
def update_parking_place():
    if request.is_json:
        if databaseProcessor.update_much_parking_place(request.get_json()):
            return jsonify({'status': 200, 'info': "Update Success"})
        else:
            return jsonify({'status': 404, 'info': "Update Fail"})
    else:
        return jsonify({'status': 404, 'info': "Body not json"})


@app.route("/parking/slot", methods=["GET"])
def get_current_parking_slot():
    result = databaseProcessor.get_current_parking_list()
    if result is not False:
        return jsonify({'data': result, 'status': 200, 'info': "Search Success"})
    else:
        return jsonify({'status': 400, 'info': "Search Failed"})


if __name__ == "__main__":
    app.run()

import uuid

from orm import Database


class DatabaseProcessor:
    def __init__(self):
        self.dbConnector = Database()

    def insert_one_parking_field(self, json_input):
        try:
            self.dbConnector.insert_parking_lots(json_input)
            places = {"data": []}
            for i in range(json_input['data'][0]["availableSpots"]):
                num = str(i + 1)
                if len(num) == 1:
                    num = "00" + num
                elif len(num) == 2:
                    num = "0" + num

                places["data"].append({
                    "parkingLotName": json_input['data'][0]["parkingLotName"],
                    "parkingNumber": num,
                    "licensePlate": None
                })
            self.dbConnector.insert_parking_places(places)
            return True
        except:
            return False

    def insert_one_user(self, json_input):
        try:
            json_input["data"][0]["userID"] = uuid.uuid4()
            self.dbConnector.insert_users(json_input)
            return True
        except:
            return False

    def insert_one_car(self, userID, plate):
        try:
            query = {
                "data": [
                    {
                        "licensePlate": plate,
                        "userID": userID,
                    }
                ]
            }
            self.dbConnector.insert_cars(query)
            return True
        except:
            return False

    def get_all_user(self):
        try:
            return self.dbConnector.get_all_user_account_email_phone_identity_plate()
        except:
            return False

    def check_user_exist(self, email):
        try:
            if len(email) == 0:
                return False
            result = self.dbConnector.if_user_exist(email)
            return [result]
        except:
            return False

    def get_one_user_password(self, email):
        try:
            if len(email) == 0:
                return False
            result = self.dbConnector.get_password(email)
            return result
        except:
            return False

    def get_one_available_packing_slot_in_field(self, field):
        try:
            if len(field) == 0:
                return False
            result = self.dbConnector.find_available_spots(field)
            print(result)
            return field + result[0]
        except:
            return False

    def search_one_user(self, account):
        try:
            result = self.dbConnector.search_user(account)
            return result
        except:
            pass

    def get_parking_field(self):
        try:
            result = self.dbConnector.get_parking_lots_data()
            return result
        except:
            return False

    def get_cars_by_userId(self, userId):
        try:
            query = {
                "data": [
                    {
                        "userID": userId
                    }
                ]
            }
            result = self.dbConnector.find_cars(query)
            return result
        except:
            return False

    def parking_lots_minus(self, name):
        try:
            self.dbConnector.update_minus_parking_lots(name)
            return True
        except:
            return False

    def parking_lots_add(self, name):
        try:
            self.dbConnector.update_plus_parking_lots(name)
            return True
        except:
            return False

    def insert_much_parking_history(self, json_input):
        try:
            self.dbConnector.insert_parking_history(json_input)
            return True
        except:
            return False

    def update_much_parking_place(self, json_input):
        try:
            self.dbConnector.update_parking_places(json_input)
            return True
        except:
            return False

    def get_current_parking_list(self):
        try:
            return self.dbConnector.get_current_parking_list()
        except:
            return False

    def update_much_parking_history(self, json_input):
        try:
            self.dbConnector.update_parking_history(json_input)
            return True
        except:
            return False

    def get_userid_by_email(self, email):
        try:
            return self.dbConnector.get_user_id_by_email(email)
        except:
            return False

    def get_parking_history_by_place(self, name, number):
        try:
            result = self.dbConnector.get_parking_history(name, number)
            print(result)
            return result
        except:
            return False

    def insert_reserve(self, json_input):
        try:
            self.dbConnector.insert_VIP(json_input)
            return True
        except:
            return False

    def black_cond_one(self, plate):
        try:
            return self.dbConnector.violation_situation_one(plate)
        except:
            return False

    def black_cond_two(self, plate):
        try:
            return self.dbConnector.violation_situation_two(plate)
        except:
            return False

    def black_cond_three(self, plate):
        try:
            return self.dbConnector.violation_situation_three(plate)
        except:
            return False

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
            self.dbConnector.insert_users(json_input)
            return True
        except:
            return False

    def insert_one_car(self, json_input):
        try:
            self.dbConnector.insert_cars(json_input)
            return True
        except:
            return False

    def get_all_user(self):
        try:
            return self.dbConnector.get_all_user_account_email_phone_identity_plate()
        except:
            return False

    def check_user_exist(self, json_input):
        try:
            email = json_input['data'][0]["email"]
            if len(email) == 0:
                return False
            result = self.dbConnector.if_user_exist(email)
            return [result]
        except:
            return False

    def get_one_user_password(self,json_input):
        try:
            email = json_input['data'][0]["email"]
            if len(email) == 0:
                return False
            result = self.dbConnector.get_password(email)
            return result
        except:
            return False

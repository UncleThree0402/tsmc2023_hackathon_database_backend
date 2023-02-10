import os

# https://github.com/GoogleCloudPlatform/cloud-sql-python-connector

from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./environment/bsid-user-group2-sa-key.json"

class Database:
    def __init__(self):
        self.connector = Connector()
        self.pool = sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=self.getconn,
        )


    def getconn(self) -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = self.connector.connect(
        "tsmchack2023-bsid-grp2:asia-east1:tsmchack2023-bsid-mysql-db",
        "pymysql",
        user="root",
        password="NMDsH2PK",
        db="parking_db"
        )
        return conn

 # insert into parking_lots table
    def insert_parking_lots(self, json_input):
        for one in json_input['data']:
            ParkingLotName = one['parkingLotName']
            AvailableSpots = one['availableSpots']
            LongitudeAndLatitude = one['longitudeAndLatitude']

            # insert statement
            insert_stmt = sqlalchemy.text("INSERT INTO ParkingLots (ParkingLotName, LongitudeAndLatitude, AvailableSpots)"
            + "VALUES (:ParkingLotName, NULLIF(:LongitudeAndLatitude, ''), :AvailableSpots)")

            with self.pool.connect() as db_conn:
                db_conn.execute(
                    insert_stmt,
                    ParkingLotName=ParkingLotName,
                    LongitudeAndLatitude=LongitudeAndLatitude,
                    AvailableSpots=AvailableSpots
                )

    # parking lots input
    # obj = {
    # "data": [
    #     {
    #         "parkingLotName": "E",
    #         "longitudeAndLatitude": "",
    #         "availableSpots": 300
    #     }
    # ]
    # }

    # insert into users table
    def insert_users(self, json_input):
        for one in json_input['data']:
            UserID = one['userID']
            Account = one['account']
            Password = one['password']
            Email = one['email']
            PhoneNumber = one['phoneNumber']
            Identity = one['identity']

            # insert statement
            insert_stmt = sqlalchemy.text("INSERT INTO Users (UserID, Account, Password, Email, PhoneNumber, Identity)"
            + "VALUES (:UserID, NULLIF(:Account, ''), NULLIF(:Password, ''), NULLIF(:Email, ''), NULLIF(:PhoneNumber, ''), :Identity)")

            with self.pool.connect() as db_conn:
                db_conn.execute(
                    insert_stmt,
                    UserID=UserID,
                    Account=Account,
                    Password=Password,
                    Email=Email,
                    PhoneNumber=PhoneNumber,
                    Identity=Identity
                )
    # user input
    # obj = {
    #     "data": [
    #         {
    #             "userID": "abc123",
    #             "account": "lebromjames",
    #             "password": "hahaiamidiot",
    #             "email": "stu30405@gmail.com",
    #             "phoneNumber": "0935774796",
    #             "identity": "User"   
    #         }
    #     ]
    # }

    # insert into cars table
    def insert_cars(self, json_input):
        for one in json_input['data']:
            LicensePlate = one['licensePlate']
            UserID = one['userID']

            # insert statement
            insert_stmt = sqlalchemy.text("INSERT INTO Cars (LicensePlate, UserID)"
            + "VALUES (:LicensePlate, :UserID)")

            with self.pool.connect() as db_conn:
                    db_conn.execute(
                        insert_stmt,
                        LicensePlate=LicensePlate,
                        UserID=UserID,
                    )

    # car input
    # obj = {
    #     "data": [
    #         {
    #             "licensePlate": "1234ZZ",
    #             "userID": "abc123",
    #         }
    #     ]
    # }

    # insert parking_place table
    def insert_parking_places(self, json_input):
        for one in json_input['data']:
            ParkingLotName = one['parkingLotName']
            ParkingNumber = one["parkingNumber"]
            LicensePlate = one["licensePlate"]

            # insert statement
            insert_stmt = sqlalchemy.text("INSERT INTO ParkingPlaces (ParkingLotName, ParkingNumber, LicensePlate)"
            + "VALUES (:ParkingLotName, :ParkingNumber, NULLIF(:LicensePlate, ''))")

            with self.pool.connect() as db_conn:
                    db_conn.execute(
                        insert_stmt,
                        ParkingLotName=ParkingLotName,
                        ParkingNumber=ParkingNumber,
                        LicensePlate=LicensePlate,
                    )

    # parking place input
    # obj = {
    #     "data": [
    #         {
    #             "parkingLotName": "D",
    #             "parkingNumber": "002",
    #             "licensePlate": "9282ZN"
    #         }
    #     ]
    # }

    def insert_black_lists(self, json_input):
        for one in json_input['data']:
            LicensePlate = one['licensePlate']
            BlackStartTime = one["blackStartTime"]
            BlackEndTime = one["blackEndTime"]

            # insert statement
            insert_stmt = sqlalchemy.text("INSERT INTO BlackLists (LicensePlate, BlackStartTime, BlackEndTime)"
            + "VALUES (:LicensePlate, :BlackStartTime, :BlackEndTime)")

            with self.pool.connect() as db_conn:
                    db_conn.execute(
                        insert_stmt,
                        LicensePlate=LicensePlate,
                        BlackStartTime=BlackStartTime,
                        BlackEndTime=BlackEndTime,
                    )

    # black list input
    # obj = {
    #     "data": [
    #         {
    #             "licensePlate": "9282ZN",
    #             "blackStartTime": '2023-01-01 08:10:00',
    #             "blackEndTime": '2023-01-02 08:10:00'
    #         }
    #     ]
    # }

    def insert_VIP(self, json_input):
        for one in json_input['data']:
            LicensePlate = one['licensePlate']
            ReservationStartTime = one["reservationStartTime"]
            ReservationEndTime = one["reservationEndTime"]
            ReservationName = one["reservationName"]
            ReservationNumber = one["reservationNumber"]

            # insert statement
            insert_stmt = sqlalchemy.text("INSERT INTO VIP (LicensePlate, ReservationStartTime, ReservationEndTime, ReservationName, ReservationNumber)"
            + "VALUES (:LicensePlate, :ReservationStartTime, :ReservationEndTime, :ReservationName, :ReservationNumber)")

            with self.pool.connect() as db_conn:
                    db_conn.execute(
                        insert_stmt,
                        LicensePlate=LicensePlate,
                        ReservationStartTime=ReservationStartTime,
                        ReservationEndTime=ReservationEndTime,
                        ReservationName=ReservationName,
                        ReservationNumber=ReservationNumber
                    )

    # VIP input
    # obj = {
    #     "data": [
    #         {
    #             "licensePlate": "9282ZN",
    #             "reservationStartTime": "2023-01-01 08:10:00",
    #             "reservationEndTime": "2023-01-02 08:10:00",
    #             "reservationName": "D",
    #             "reservationNumber": "002"
    #         }
    #     ]
    # }

    def insert_parking_history(self, json_input):
        for one in json_input['data']:
            ParkingLotName = one['parkingLotName']
            ParkingNumber = one["parkingNumber"]
            LicensePlate = one["licensePlate"]
            ParkingStartTime = one['parkingStartTime']
            ParkingEndTime = one['parkingEndTime']

            # insert statement
            insert_stmt = sqlalchemy.text("INSERT INTO ParkingHistory (ParkingLotName, ParkingNumber, LicensePlate, ParkingStartTime, ParkingEndTime)"
            + "VALUES (:ParkingLotName, :ParkingNumber, :LicensePlate, :ParkingStartTime, NULLIF(:ParkingEndTime, ''))")

            with self.pool.connect() as db_conn:
                    db_conn.execute(
                        insert_stmt,
                        ParkingLotName=ParkingLotName,
                        ParkingNumber=ParkingNumber,
                        LicensePlate=LicensePlate,
                        ParkingStartTime=ParkingStartTime,
                        ParkingEndTime=ParkingEndTime
                    )

    # insert history input
    #     obj = {
    #     "data": [
    #         {
    #             "parkingLotName": "X",
    #             "parkingNumber": "001",
    #             "licensePlate": "1111PP",
    #             "parkingStartTime": "2023-01-01 08:10:00",
    #             "parkingEndTime": ""
    #         }
    #     ]
    # }

    # get user data
    def get_all_user_account_email_phone_identity_plate(self):
        result = []
        with self.pool.connect() as db_conn:
            basic_data = db_conn.execute("SELECT UserID, Account, Email, PhoneNumber, Identity FROM Users").fetchall()

            for row in basic_data:
                # this is car instance, not a list
                cars = db_conn.execute("SELECT LicensePlate FROM Cars WHERE UserID= %s", row[0]).fetchall() 
                data = {
                    "userId": row[0],
                    "account": row[1],
                    "email": row[2],
                    "tele": row[3],
                    "group": row[4],
                    "cars": []
                }
                # so we should turn it into list
                for car in cars:
                    data['cars'].append([c for c in car])

                result.append(data)

        return result

    def if_user_exist(self, email):
        users = []
        with self.pool.connect() as db_conn:
            userId = db_conn.execute("SELECT UserID FROM Users WHERE Email= %s", email).fetchall()
            
            for id in userId:
                users.append([i for i in id])

            return True if len(users) > 0 else False

    def get_password(self, email):
        result = []
        with self.pool.connect() as db_conn:
            password = db_conn.execute("SELECT Password FROM Users WHERE Email= %s", email).fetchall()

            result.append([pas for pas in password[0]])

            return result[0][0]


    def search_user(self, account):
        users = []
        with self.pool.connect() as db_conn:
            basic_data = db_conn.execute("SELECT UserID, Account, Email, PhoneNumber, Identity FROM Users WHERE Account= %s", account).fetchall()

            for row in basic_data:
                cars = db_conn.execute("SELECT LicensePlate FROM Cars WHERE UserID= %s", row[0]).fetchall() 
                data = {
                    "userId": row[0],
                    "account": row[1],
                    "email": row[2],
                    "tele": row[3],
                    "group": row[4],
                    "cars": []
                }
                # so we should turn it into list
                for car in cars:
                    data['cars'].append([c for c in car])

                users.append(data)

        return users

    def if_plate_exist(self, license_plate):
        result = []
        with self.pool.connect() as db_conn:
            plates = db_conn.execute("SELECT LicensePlate FROM Cars WHERE LicensePlate= %s", license_plate).fetchall()
            
            for plate in plates:
                result.append([p for p in plate])

            return True if len(result) > 0 else False

    
    # give ParkingLot name, parking number, and license plate, will set the license, if no car, input ""
    def update_parking_places(self, json_input):
        for one in json_input['data']:
            name = one['parkingLotName']
            number = one['parkingNumber']
            plate = one['licensePlate']
            with self.pool.connect() as db_conn:
                db_conn.execute("UPDATE ParkingPlaces SET LicensePlate = NULLIF(%s, '') WHERE ParkingLotName= %s AND ParkingNumber= %s", plate, name, number)

    # update parking places input
    # obj = {
    #     "data": [
    #         {
    #             "parkingLotName": "Q",
    #             "parkingNumber": "000",
    #             "licensePlate": ""
    #         },
    #         {
    #             "parkingLotName": "Q",
    #             "parkingNumber": "001",
    #             "licensePlate": ""
    #         }
    #     ]
    # }

    # give ParkingLot name, let its AvailableSpots += 1
    def update_plus_parking_lots(self, name):
        with self.pool.connect() as db_conn:
            current = db_conn.execute("SELECT AvailableSpots FROM ParkingLots WHERE ParkingLotName= %s", name).fetchall()
            db_conn.execute("UPDATE ParkingLots SET AvailableSpots= %s WHERE ParkingLotName= %s", current[0][0]+1, name)

    # give ParkingLot name, let its AvailableSpots -= 1
    def update_minus_parking_lots(self, name):
        with self.pool.connect() as db_conn:
            current = db_conn.execute("SELECT AvailableSpots FROM ParkingLots WHERE ParkingLotName= %s", name).fetchall()
            db_conn.execute("UPDATE ParkingLots SET AvailableSpots= %s WHERE ParkingLotName= %s", current[0][0]-1, name)
    
    # give ParkingLot name, return a parking number
    def find_available_spots(self, name):
        result = []
        with self.pool.connect() as db_conn:
            spot = db_conn.execute("SELECT ParkingNumber FROM ParkingPlaces WHERE ParkingLotName= %s AND ISNULL(LicensePlate)", name).fetchone()
            result.append([s for s in spot])

        return result[0]        

    def find_cars(self, json_input):
        result = []
        for one in json_input['data']:
            UserID = one['userID']
            with self.pool.connect() as db_conn:
                cars = db_conn.execute("SELECT LicensePlate FROM Cars WHERE UserID= %s", UserID).fetchall()
                for car in cars:
                    name = db_conn.execute("SELECT ParkingLotName FROM ParkingPlaces WHERE LicensePlate= %s", car[0]).fetchall()
                    number = db_conn.execute("SELECT ParkingNumber FROM ParkingPlaces WHERE LicensePlate= %s", car[0]).fetchall()
                    try:
                        data = {
                            "car": car[0],
                            "parking_place": name[0][0] + number[0][0]
                        }
                        result.append(data)
                    except:
                        result = []
        return result


    def get_parking_lots_data(self):
        result = []
        with self.pool.connect() as db_conn:
            basic_data = db_conn.execute("SELECT ParkingLotName, LongitudeAndLatitude, AvailableSpots FROM ParkingLots").fetchall()

            for row in basic_data:
                data = {
                    "parking_lot_name": row[0],
                    "remain": row[2],
                    "longitude_and_latitude": row[1]
                }

                result.append(data)

        return result


    def get_current_parking_list(self):
        result = []
        with self.pool.connect() as db_conn:
            cars = db_conn.execute("SELECT ParkingLotName, ParkingNumber, LicensePlate FROM ParkingPlaces WHERE LicensePlate IS NOT NULL").fetchall()

            for car in cars:
                entry_time = db_conn.execute("SELECT ParkingStartTime FROM ParkingHistory WHERE LicensePlate= %s", car[2]).fetchall()
                user_id = db_conn.execute("SELECT UserID FROM Cars WHERE LicensePlate= %s", car[2]).fetchall()
                account = db_conn.execute("SELECT Account FROM Users WHERE UserID= %s", user_id[0][0]).fetchall()
                email = db_conn.execute("SELECT Email FROM Users WHERE UserID= %s", user_id[0][0]).fetchall()
                try:
                    data = {
                        "license_plate": car[2],
                        "parking_place": car[0]+car[1],
                        "entry_time": entry_time[0][0],
                        "user_id": user_id[0][0],
                        "account": account[0][0],
                        "email": email[0][0]
                    }

                    result.append(data)
                except:
                    continue

        return result

    def get_parking_history(self, name, number):
        result = []
        with self.pool.connect() as db_conn: 
            histories = db_conn.execute("SELECT LicensePlate, ParkingStartTime, ParkingEndTime FROM ParkingHistory WHERE ParkingLotName= %s AND ParkingNumber = %s", name, number).fetchall()
            for history in histories:
                user_id = db_conn.execute("SELECT UserID FROM Cars WHERE LicensePlate= %s", history[0]).fetchall()
                account = db_conn.execute("SELECT Account FROM Users WHERE UserID= %s", user_id[0][0]).fetchall()
                email = db_conn.execute("SELECT Email FROM Users WHERE UserID= %s", user_id[0][0]).fetchall()
                try:
                    data = {
                        "license_plate": history[0],
                        "entry_time": history[1],
                        "leave_time": history[2],
                        "user_id": user_id[0][0],
                        "account": account[0][0],
                        "email": email[0][0]
                    }
                    
                    result.append(data)
                except:
                    continue
        
        return result
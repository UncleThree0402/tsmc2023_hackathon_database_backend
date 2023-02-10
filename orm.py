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

    # insert into parking_space table
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
            ParkingStartTime = one['parkingStartTime']
            ParkingEndTime = one['parkingEndTime']

        # insert statement
        insert_stmt = sqlalchemy.text("INSERT INTO Cars (LicensePlate, UserID, ParkingStartTime, ParkingEndTime)"
        + "VALUES (:LicensePlate, :UserID, NULLIF(:ParkingStartTime, ''), NULLIF(:ParkingEndTime, ''))")

        with self.pool.connect() as db_conn:
                db_conn.execute(
                    insert_stmt,
                    LicensePlate=LicensePlate,
                    UserID=UserID,
                    ParkingStartTime=ParkingStartTime,
                    ParkingEndTime=ParkingEndTime
                )

    # car input
    # obj = {
    #     "data": [
    #         {
    #             "licensePlate": "1234ZZ",
    #             "userID": "abc123",
    #             "parkingStartTime": "2023-01-01 08:10:00",
    #             "parkingEndTime": "2023-01-01 08:44:00"
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



# # https://github.com/GoogleCloudPlatform/cloud-sql-python-connector

# from google.cloud.sql.connector import Connector
# import sqlalchemy
# import pymysql
# import json
# import models
# # ParkingLots (ParkingLotName char(255) NOT NULL, LongitudeAndLatitude char(255), AvailableSpots int, PRIMARY KEY (ParkingLotName));
# # Users (UserID char(255) NOT NULL , Account char(255), Password char(255), Email char(255), PhoneNumber char(255), Identity char(20), PRIMARY KEY (UserID));
# # Cars (LicensePlate char(10) NOT NULL, UserID char(255) NOT NULL, PRIMARY KEY (LicensePlate), FOREIGN KEY (UserID) REFERENCES Users(UserID));
# # ParkingPlaces (ParkingLotName char(255) NOT NULL, ParkingNumber char(10) NOT NULL, ParkingStartTime TIME ,LicensePlate char(10), CONSTRAINT ParkingID PRIMARY KEY (ParkingLotName, ParkingNumber), FOREIGN KEY (LicensePlate) REFERENCES Cars(LicensePlate));
# # BlackLists (BlackID int NOT NULL AUTO_INCREMENT, UserID char(255), BlackStartTime TIME, BlackEndTime TIME, foreign key(UserID) references Users(UserID), primary key (BlackID));
# # VIP (VIPID int NOT NULL AUTO_INCREMENT, LicensePlate char(10), ReservationStartTime TIME, ReservationEndTime TIME, ReservationName char(255), ReservationNumber char(10), primary key (VIPID), foreign key (LicensePlate) references Cars(LicensePlate));
# # ViolateList (ViolateID int NOT NULL AUTO_INCREMENT, LicensePlate char(10), primary key (ViolateID), foreign key (LicensePlate) references Cars(LicensePlate));
# # ParkingHistory (HistoryID int NOT NULL AUTO_INCREMENT, ParkingLotName char(255), ParkingNumber char(10), LicensePlate char(10), ParkingEndTime Time, primary key(HistoryID), constraint ParkingID foreign key(ParkingLotName, ParkingNumber) references ParkingPlaces(ParkingLotName, ParkingNumber));

# # def getconn() -> pymysql.connections.Connection:
# #     conn: pymysql.connections.Connection = connector.connect(
# #         "tsmchack2023-bsid-grp2:asia-east1:tsmchack2023-bsid-mysql-db",
# #         "pymysql",
# #         user="root",
# #         password="NMDsH2PK",
# #         db="parking_db"
# #     )
# #     return conn

# class Database:
#     def __init__(self):
#         self.connector = Connector()
#         self.pool = sqlalchemy.create_engine(
#             "mysql+pymysql://",
#             creator=self.getconn,
#         )


#     def getconn(self) -> pymysql.connections.Connection:
#         conn: pymysql.connections.Connection = self.connector.connect(
#         "tsmchack2023-bsid-grp2:asia-east1:tsmchack2023-bsid-mysql-db",
#         "pymysql",
#         user="root",
#         password="NMDsH2PK",
#         db="parking_db"
#         )
#         return conn


# # initialize Connector object
# # connector = Connector()

# # function to return the database connection


# # create connection pool
# # pool = sqlalchemy.create_engine(
# #     "mysql+pymysql://",
# #     creator=getconn,
# # )

# # query parking_space table
# def query_all_parking():
#     r = []
#     with pool.connect() as db_conn:
#         result = db_conn.execute("SELECT * from parking_db").fetchall()
        
#         # Do something with the results
#         for row in result:
#             r.append({
#                 "number_plate": row[0], 
#                 "start_parking_time": row[1],
#                 "end_parking_time": row[2],
#                 "parking_space": row[3]

#             })
#     return r

# # insert into parking_space table
# def insert_parking(floor, zone, parking_number, l_p):
#     # insert statement
#     insert_stmt = sqlalchemy.text(
#         "INSERT INTO parking.parking_space (floor, zone, parking_number, license_plate) "
#         + "VALUES (:floor, :zone, :parking_number, :license_plate)")

#     with pool.connect() as db_conn:
#         db_conn.execute(
#             insert_stmt,
#             floor=floor,
#             zone=zone,
#             parking_number=parking_number,
#             license_plate=l_p)

# def insert_parking_lots( ParkingLotName, AvailableSpots, LongitudeAndLatitude=None):
#     insert_stmt = sqlalchemy.text("INSERT INTO ParkingLots (ParkingLotName, LongitudeAndLatitude, AvailableSpots)"
#     + "VALUES (:ParkingLotName, :LongitudeAndLatitude, :AvailableSpots)")

#     with pool.connect() as db_conn:
#         db_conn.execute(
#             insert_stmt,
#             ParkingLotName=ParkingLots,
#             LongitudeAndLatitude=LongitudeAndLatitude,
#             AvailableSpots=AvailableSpots
#         )

# def get_user_data():
#     r = []
#     with pool.connect() as db_conn:
#         result = db_conn.execute("SELECT UserID, Account, Email, PhoneNumber from parking where Identity = 'User'").fetchall()
#         for row in result:
#             value = {
#                 "UserID": row[0],
#                 "Account": row[1],
#                 "Email": row[2],
#                 "PhoneNumber": row[3]
#             }
#             r.append(json.dumps(value))
#     return r

# def insert_black_list():
#     pass




# from google.cloud.sql.connector import Connector
# import sqlalchemy
# import pymysql
# import json
# import models
import os

# https://github.com/GoogleCloudPlatform/cloud-sql-python-connector

from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/joeysmith/bsid-user-group2-sa-key.json"

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

    # # query parking_space table
    # def query_all_parking():
    #     r = []
    #     with pool.connect() as db_conn:
    #         result = db_conn.execute("SELECT * from parking.parking_space").fetchall()
            
    #         # Do something with the results
    #         for row in result:
    #             r.append({
    #                 "floor": row[0],
    #                 "zone": row[1],
    #                 "parking_number": row[2],
    #                 "license_plate": row[3],
    #                 "is_available": row[4]
    #             })
    #     return r

    # insert into parking_space table
    def insert_parking_lots(self, json_input):
        for one in json_input['data']:
            ParkingLotName = one['ParkingLotName']
            AvailableSpots = one['AvailableSpots']
            LongitudeAndLatitude = one['LongitudeAndLatitude']
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
# {
#     data : [
#         {
#             park :　""
#         },{

#         }
#     ],

# }


# insert_parking_lots('D', 400)

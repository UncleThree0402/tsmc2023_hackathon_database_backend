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
    # parking lots input
    # obj = {
    # "data": [
    #     {
    #         "ParkingLotName": "E",
    #         "LongitudeAndLatitude": "",
    #         "AvailableSpots": 300
    #     }
    # ]
    # }



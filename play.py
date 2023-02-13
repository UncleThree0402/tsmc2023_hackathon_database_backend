import datetime
import time
import uuid

import pandas as pd
import requests


def add_user():
    name = str(uuid.uuid4())
    password = str(uuid.uuid4())
    email = str(uuid.uuid4())
    buf = {
        "data": [
            {
                "userID": "test20",
                "account": name,
                "password": password,
                "email": f"{email}@gmail.com",
                "phoneNumber": "123456",
                "identity": "User"
            }
        ]
    }

    requests.post("http://165.22.58.21:3000/user/new",
                  json=buf)

    id = requests.get(f"http://165.22.58.21:3000/user/{email}@gmail.com/userID",
                      headers={'Accept': 'application/json'}).json()["data"][0]["userID"]

    return id


df_start = pd.read_csv("entry_scenario.csv")
df_exit = pd.read_csv("exit_scenario.csv")

start = 0
end = 0

init_time = time.mktime(datetime.datetime.strptime("11/02/2023", "%d/%m/%Y").timetuple())

# 2023-02-11 00:04:00

test = time.mktime(datetime.datetime.strptime("2023-02-11 00:04:00", "%Y-%m-%d %H:%M:%S").timetuple())

for i in range(1440):
    cur_time = init_time + 60 * i
    while True:
        buf = df_exit["exit_time"][end]
        buf_time = time.mktime(datetime.datetime.strptime(buf, "%Y-%m-%d %H:%M:%S").timetuple())
        if cur_time >= buf_time:
            number = str(df_exit["packing_number"][end])
            if len(number) == 1:
                number = "00" + number
            elif len(number) == 2:
                number = "0" + number

            files = {'image': open("Data/public_scenario_images/" + df_exit["image_path"][end], 'rb')}
            res = requests.post("http://178.128.119.142:3001/detect",
                                files=files,
                                headers={'Accept': 'application/json'})
            plate = res.json()["number"].strip()

            buf = {
                "data": [
                    {
                        "parkingLotName": str(df_exit["packing_lots"][end]),
                        "parkingNumber": number,
                        "licensePlate": plate,
                        "parkingExitTime": str(df_exit["exit_time"][end])
                    }
                ]
            }
            print("EXIT ", buf)
            requests.post("http://165.22.58.21:3000/exit", json=buf)
            end += 1
        else:
            break

    while True:
        buf = df_start["entry_time"][start]
        buf_time = time.mktime(datetime.datetime.strptime(buf, "%Y-%m-%d %H:%M:%S").timetuple())
        if cur_time >= buf_time:
            id = add_user()
            files = {'image': open("Data/public_scenario_images/" + df_start["image_path"][start], 'rb')}
            res = requests.post("http://178.128.119.142:3001/detect",
                                files=files,
                                headers={'Accept': 'application/json'})
            print(res.json())
            plate = res.json()["number"].strip()
            requests.post(f"http://165.22.58.21:3000/user/{id}/{plate}")

            number = str(df_start["packing_number"][start])
            if len(number) == 1:
                number = "00" + number
            elif len(number) == 2:
                number = "0" + number

            buf = {
                "data": [
                    {
                        "parkingLotName": str(df_start["packing_lots"][start]),
                        "parkingNumber": number,
                        "licensePlate": str(plate),
                        "parkingStartTime": str(df_start["entry_time"][start])
                    }
                ]
            }
            print("ENTRY ", buf)
            requests.post("http://165.22.58.21:3000/entry", json=buf)
            start += 1
        else:
            break

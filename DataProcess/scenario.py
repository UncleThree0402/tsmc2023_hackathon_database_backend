import pandas as pd

df = pd.read_csv("Data/reference_data/public_scenario_data_groundtruth.csv")

data = {
    "packing_lots": [],
    "packing_number": [],
    "entry_time": [],
    "exit_time": []
}

for idx in range(len(df)):
    filename = df["output_filename"][idx]
    name = filename[:-4]
    name = name.split("_")
    name[0] = name[0].split("-")
    name[-2] = name[-2][:2] + ":" + name[-2][2:] + ":00"
    name[-1] = name[-1][:2] + ":" + name[-1][2:] + ":00"
    data["packing_lots"].append(name[0][0])
    data["packing_number"].append(name[0][1])
    data["entry_time"].append(name[1])
    data["exit_time"].append(name[2])

df = pd.DataFrame(data)
df.to_csv(f"./scenario.csv", index=False)

df['entry_time'] = pd.to_datetime(df['entry_time'])
df['exit_time'] = pd.to_datetime(df['exit_time'])
df_entry = df.sort_values(by='entry_time')
df_exit = df.sort_values(by='exit_time')
print(df_entry)
print(df_exit)

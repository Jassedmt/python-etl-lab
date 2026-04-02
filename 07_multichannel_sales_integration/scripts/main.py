import os
import json
import csv
from datetime import datetime

def extract_data(file_path, file_type):
    raw_data = []

    with open(file_path, "r", encoding='utf-8') as file:

        if file_type == "csv":
            reader = csv.DictReader(file)
            for row in reader:
                row[data_path] = os.path.basename(file_path)
                raw_data.append(row)

        elif file_type == "json":
            data = json.load(file)
            for row in data:
                row[data_path]= os.path.basename(file_path)
                raw_data.append(row)

        return raw_data
    

data_path = "07_multichannel_sales_integration/data/"
all_extracted_data = []

for file_name in os.listdir(data_path):
    if file_name.endswith(('.csv', '.json')):
        full_path = os.path.join(data_path, file_name)

        if file_name.endswith(".csv"):
            file_type = "csv"
        else:
            file_type = "json"

        data_from_file = extract_data(full_path, file_type)

        all_extracted_data.extend(data_from_file)

print(f"Filas totales: {len(all_extracted_data)}")


def normalize_dates(date_str):
    formats = ["%d/%m/%Y", "%Y/%m/%d"]

    for format in formats:
        try:
            date_obj = datetime.strptime(date_str, format)
            return date_obj.strftime("%Y-%m-%d")
        except:
            continue

    return None

for row in all_extracted_data:

    row["Fecha"] = normalize_dates(row["Fecha"])

    print(row)


def normalize_channel(channel):

    if not channel:
        return None

    channel = channel.strip().lower()

    mapping = {
        "store": "Tienda",
        "web": "Ecommerce",
        "app": "App"
    }

    return mapping.get(channel, None)

for row in all_extracted_data:

    row["Canal"] = normalize_channel(row["Canal"])
    print(row)
from io import StringIO
import requests
import csv

CSV_URL = "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv"


def load_coffee_shops():
    try:
        response = requests.get(CSV_URL, timeout=10)
        response.raise_for_status()
        csv_data = StringIO(response.text)
        return parse_coffee_shops(csv_data)
    except Exception as e:
        print(f"[data_loader] Error: {e}")
        return []


def parse_coffee_shops(csv_file):
    coffee_shops = []
    reader = csv.reader(csv_file)
    for row in reader:
        name, x, y = row[0], row[1], row[2]
        name = name.strip().strip('"').strip("'")
        try:
            x = float(x.strip())
            y = float(y.strip())
            coffee_shops.append({"Name": name, "X": x, "Y": y})
        except ValueError:
            continue

    # print(f"Loaded {len(coffee_shops)} coffee shops")
    # for shop in coffee_shops:
    #     print(f"DEBUG: {shop['Name']} - {shop['X']}, {shop['Y']}")
    return coffee_shops

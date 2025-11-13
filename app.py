from flask import Flask, request
from services.data_loader import load_coffee_shops
from services.distance import euclidean_distance

app = Flask(__name__)

@app.get("/closest_coffee_shops")
def closest_coffee_shops():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    shops = load_coffee_shops()

    results = []
    for shop in shops:
            shop_x = float(shop["X"])
            shop_y = float(shop["Y"])
            distance = euclidean_distance(x, y, shop_x, shop_y)
            results.append({
                "name": shop["Name"],
                "x": shop_x,
                "y": shop_y,
                "distance": distance
            })

    results.sort(key = lambda x: x["distance"])
    return results[:3]

if __name__ == "__main__":
    app.run(debug=True)
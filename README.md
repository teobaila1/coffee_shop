# Coffee shops API Overview

This is a REST API short application that receives some user coordinates and returns a
list of the three closest coffee shops, from the closest to the furthest.

## Datas

The coffee shops are stored in a remote CSV having columns such as: Name, X and Y. The quality of the data can vary, they can be malformed.

link: https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv

## Expected output

The response should be the 3 closest coffee shops in a JSON list (name, location, distance from the user), 
sorted from the closest tot the furthest by distance. The distances must be rounded to 4 decimal
places and all coordinates must lie on a 2D plane (we used Euclidean Distance).

### Example

For coordinates X = 47.6 and Y = -122.4, the output should be:

Starbucks Seattle2,
Starbucks Seattle,
Starbucks SF

## Technologies used

Python, Flask, requests.

## How to run the application

1) Clone the repository: git clone ...
2) Open a console in the root project
3) Write down: python app.py and press Enter
4) The application will start running on 127.0.0.1:5000
5) To verify if the app works fine, in your browser write:
   #### https://127.0.0.1:5000/closest_coffee_shops?x=47.6&y=-122.4
6) Instead of those X and Y, you can enter any coordinates


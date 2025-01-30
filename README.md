
Installation 

Run the command `docker compose build` to build the app and with run via `docker compose up`

If It run successfully, got to the following request to get the optimal fuel stations

http://127.0.0.1:8080/route/stations/?start=12&end=13


```py
data = {
    "stations": [
        {"address": "A", "distance": 150, "price": 3.50},
        {"address": "B", "distance": 180, "price": 3.20},
        {"address": "C", "distance": 200, "price": 3.80},
        {"address": "D", "distance": 320, "price": 3.90},
        {"address": "E", "distance": 350, "price": 3.30},
        {"address": "F", "distance": 380, "price": 3.60},
        {"address": "G", "distance": 480, "price": 3.40},
        {"address": "H", "distance": 510, "price": 3.70},
        {"address": "I", "distance": 530, "price": 3.20},
        {"address": "J", "distance": 650, "price": 3.80},
        {"address": "K", "distance": 670, "price": 3.50},
        {"address": "L", "distance": 690, "price": 3.90},
    ],
    "distance": 800,
}
```

Since I could not find a free map API in the given time I return above dummy data from client.
So If you change the start and end params value in the query the result will not change because
I return a dummy data to find optimal stations. The result is the same all the time but it is calculated not just returned.

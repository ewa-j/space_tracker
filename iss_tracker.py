import json, turtle, urllib.request, time

# Astronauts in space
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("There are currently " + str(result["number"]) + " astronauts in space:")
print("")

people = result["people"]

for p in people:
    print(p["name"] + " on board of " + p["craft"])

'''map
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("world_map.gif")

iss = turtle.Turtle()
iss.shape("triangle")
iss.setheading(45)
iss.penup()'''

# JSON request for current location
while True:
    url2 = "http://api.open-notify.org/iss-now.json"
    req = urllib.request.urlopen(url2)
    resp = json.loads(req.read())

    location = resp["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]
    print("\nLatitude: " + str(lat))
    print("Longitude: " + str(lon))

    # iss.goto(lon, lat)
    time.sleep(5)
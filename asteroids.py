import json, urllib.request
from datetime import timedelta, date, time


# Asteroids near Earth in next 7 days
def asteroids_seven_days():
    today = date.today()
    end_date = date.today() + timedelta(days=7)

    url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + str(today) + "&end_date=" + str(
        end_date) + "&api_key=DEMO_KEY"

    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    print("Start date: " + str(today))
    print("End date: " + str(end_date))
    print("In the next 7 days " + str(result["element_count"]) + " asteroids will be passing near Earth.\n")

    asteroids = result["near_earth_objects"]
    for asteroid in asteroids:
        for field in asteroids[asteroid]:
            try:
                # name
                print("Object name: " + field["name"])
                # diameter min
                print("Minimal diameter in km: " + str(
                    field["estimated_diameter"]["kilometers"]["estimated_diameter_min"]))
                # diameter max
                print("Maximum diameter in km: " + str(
                    field["estimated_diameter"]["kilometers"]["estimated_diameter_max"]))
                # velocity
                print("Velocity [km/h]: " + str(
                    field["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]))
                # approach time
                print("Close Approach date and Time: " + field["close_approach_data"][0]["close_approach_date_full"])
                # distance from Earth when passing
                print("Object will pass Earth at distance of: " + str(
                    field["close_approach_data"][0]["miss_distance"]["kilometers"]) + " km")

                if field["is_potentially_hazardous_asteroid"]:
                    print("This object may pose a threat to Earth!")
                else:
                    print("This object should not be dangerous to our planet. We are safe.")

            except Exception as e:
                print(e)
            finally:
                print("....................................")


# Asteroids near Earth from today until given date

def asteroids_today_given_days():
    today = date.today()
    # start = input("Enter start date in format YYYY-MM-DD: ")
    x = input("Enter number of days since today that you want to check: ")
    end_date = date.today() + timedelta(days=int(x))

    url2 = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + str(today) + "&end_date=" + str(
        end_date) + "&api_key=DEMO_KEY"
    response2 = urllib.request.urlopen(url2)
    result2 = json.loads(response2.read())

    print("Start date: " + str(today))
    print("End date: " + str(end_date))
    print("Between " + str(today) + " and " + str(end_date) + " " + str(
        result2["element_count"]) + " asteroids will be passing near Earth.")
    print("")

    asteroids = result2["near_earth_objects"]
    for asteroid in asteroids:
        for field in asteroids[asteroid]:
            try:
                # name
                print("Object name: " + field["name"])
                # diameter min
                print("Minimal diameter in km: " + str(
                    field["estimated_diameter"]["kilometers"]["estimated_diameter_min"]))
                # diameter max
                print("Maximum diameter in km: " + str(
                    field["estimated_diameter"]["kilometers"]["estimated_diameter_max"]))
                # velocity
                print("Velocity [km/h]: " + str(
                    field["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]))
                # approach time
                print("Close Approach date and Time: " + field["close_approach_data"][0]["close_approach_date_full"])
                # distance from Earth when passing
                print("Object will pass Earth at distance of: " + str(
                    field["close_approach_data"][0]["miss_distance"]["kilometers"]) + " km")

                if field["is_potentially_hazardous_asteroid"]:
                    print("This object may pose a threat to Earth!")
                else:
                    print("This object should not be dangerous to our planet. We are safe.")

            except Exception as e:
                print(e)
            finally:
                print("....................................")


# Asteroids near Earth between given days

def asteroids_given_days():
    start_str = input("Enter start date in format YYYY-MM-DD: ")
    start = date.fromisoformat(start_str)

    end_str = input("Enter end date in format YYYY-MM-DD: ")
    end = date.fromisoformat(end_str)

    url3 = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + str(start) + "&end_date=" + str(
        end) + "&api_key=DEMO_KEY"
    response3 = urllib.request.urlopen(url3)
    result3 = json.loads(response3.read())

    print(start)
    print(end)
    print("Between " + str(start) + " and " + str(end) + " " + str(
        result3["element_count"]) + " asteroids will be passing near Earth.")
    print("")

    asteroids = result3["near_earth_objects"]
    for asteroid in asteroids:
        for field in asteroids[asteroid]:
            try:
                # name
                print("Object name: " + field["name"])
                # diameter min
                print("Minimal diameter in km: " + str(
                    field["estimated_diameter"]["kilometers"]["estimated_diameter_min"]))
                # diameter max
                print("Maximum diameter in km: " + str(
                    field["estimated_diameter"]["kilometers"]["estimated_diameter_max"]))
                # velocity
                print("Velocity [km/h]: " + str(
                    field["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]))
                # approach time
                print("Close Approach date and Time: " + field["close_approach_data"][0]["close_approach_date_full"])
                # distance from Earth when passing
                print("Object will pass Earth at distance of: " + str(
                    field["close_approach_data"][0]["miss_distance"]["kilometers"]) + " km")

                if field["is_potentially_hazardous_asteroid"]:
                    print("This object may pose a threat to Earth!")
                else:
                    print("This object should not be dangerous to our planet. We are safe.")

            except Exception as e:
                print(e)
            finally:
                print("....................................")


def which():
    q = input(
        "Enter 1 if you want to check objects passing Earth in the next 7 days. Enter 2 if you want to check specific number of days since today. Enter 3 if you want to specify start date and aend date. ")
    if q == "1":
        asteroids_seven_days()
        restart()
    elif q == "2":
        asteroids_today_given_days()
        restart()
    elif q == "3":
        asteroids_given_days()
        restart()
    else:
        print("Invalid input. Try again.")
        which()


def restart():
    again = input("Do you want to check another date? Y/N ")
    if again.lower() == "y":
        which()
        restart()
    elif again.lower() == "n":
        print("Bye!")
    else:
        print("Invalid input. Try again.")
        restart()


which()
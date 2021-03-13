import json

filename = ("robocity.json")


def read(filename):
    with open(filename) as file:

        data = json.load(file)

        city = data["city"]
        print(f"City name is : {city}")

        population = data["population"]
        print(f"Population name is : {population}")

        # it locates the bot section of the json file("data")
        for bot in data["bots"]:
            # and uses it for iteration range using background built-in iteration function. You have to mention that you want it to look in the bot section of the json file ["bots"]
            name = bot["name"]
            stats = bot["stats"]

            print(f"{name} has the following stats {stats}")


def run():
    read(filename)


if __name__ == "__main__":
    run()

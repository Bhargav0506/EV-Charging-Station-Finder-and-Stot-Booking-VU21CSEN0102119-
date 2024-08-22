class ChargingStation:
    def __init__(self, name, location, available_slots):
        self.name = name
        self.location = location
        self.available_slots = available_slots

    def book_slot(self):
        if self.available_slots > 0:
            self.available_slots -= 1
            return True
        return False

    def __str__(self):
        return f"{self.name} located at {self.location} with {self.available_slots} slots available."


class ChargingStationFinder:
    def __init__(self):
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)

    def find_stations(self, city):
        return [station for station in self.stations if station.location.lower() == city.lower()]

    def display_stations(self, city):
        found_stations = self.find_stations(city)
        if found_stations:
            print("Available Charging Stations:")
            for index, station in enumerate(found_stations, start=1):
                print(f"{index}. {station}")
        else:
            print("No charging stations found in this city.")

    def book_station_slot(self, station_index):
        if 0 <= station_index < len(self.stations):
            station = self.stations[station_index]
            if station.book_slot():
                print(f"Successfully registered a slot at {station.name}.")
                return
            else:
                print(f"No available slots at {station.name}.")
                return
        print("Station not found.")


def main():
    finder = ChargingStationFinder()
    
    # Adding charging stations in various cities of Andhra Pradesh
    finder.add_station(ChargingStation("ChargeFinder", "Visakhapatnam", 2))
    finder.add_station(ChargingStation("Tata Power - Croma", "Visakhapatnam", 1))
    finder.add_station(ChargingStation("IOCL - Simhadri", "Visakhapatnam", 0))
    
    finder.add_station(ChargingStation("Alternative Fueling Station Locator", "Vijayawada", 3))
    finder.add_station(ChargingStation("Tata Power - Tristar Auto", "Vijayawada", 2))
    finder.add_station(ChargingStation("IOCL - Swagat", "Vijayawada", 1))

    finder.add_station(ChargingStation("PlugShare", "Tirupati", 1))
    finder.add_station(ChargingStation("Tata Power - Daspalla", "Tirupati", 2))
    finder.add_station(ChargingStation("Good Morning Resort", "Tirupati", 0))

    finder.add_station(ChargingStation("Werego", "Guntur", 0))
    finder.add_station(ChargingStation("IOCL - Usha Petroleum", "Guntur", 1))
    finder.add_station(ChargingStation("IOCL - Swagat Anakapalle", "Guntur", 2))

    finder.add_station(ChargingStation("EV Charging Station Finder", "Nellore", 4))
    finder.add_station(ChargingStation("TML - Shiv Shankar Motors", "Nellore", 1))
    finder.add_station(ChargingStation("Tata Power - East Point", "Nellore", 0))

    # List of cities in Andhra Pradesh
    cities = [
        "Visakhapatnam",
        "Vijayawada",
        "Guntur",
        "Tirupati",
        "Nellore",
        "Kurnool",
        "Rajahmundry",
        "Kadapa",
        "Anantapur"
    ]

    print("List of cities in Andhra Pradesh:")
    for index, city in enumerate(cities, start=1):
        print(f"{index}. {city}")

    city_choice = int(input("Select your city by number: "))
    selected_city = cities[city_choice - 1]

    finder.display_stations(selected_city)

    station_choice = int(input("Enter the number of the station you want to book a slot at: ")) - 1
    finder.book_station_slot(station_choice)


if __name__ == "__main__":
    main()
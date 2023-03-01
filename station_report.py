import sys


class StationReport:
    def __init__(self):
        self.stations = {}
        self.connections = {}

        # Load stations and IDs from file
        try:
            with open('rubb.txt', 'r') as f:
                for line in f:
                    station_name, station_id = line.strip().split(',')
                    self.stations[station_id] = station_name
        except FileNotFoundError:
            print('Stations file not found.')

            return  # exit the try block

        # Load connections from file
        try:
            with open('connections.txt', 'r') as f:
                for line in f:
                    station_a, station_b, miles = line.strip().split(',')
                    if station_a != station_b:  # ignore connections from a station to itself
                        key = tuple(sorted([station_a, station_b]))
                        if key not in self.connections or miles < self.connections[key][0]:
                            self.connections[key] = (
                                float(miles), station_a, station_b)
        except FileNotFoundError:
            print('Connections file not found.')
            return  # exit the try block

    def get_report(self, station_id):
        if station_id not in self.stations:
            print(f'Station {station_id} not found.')
            return  # exit the method (instance of a class)

        connected_stations = []
        total_distance = 0

        for key, value in self.connections.items():
            if station_id in key:
                other_station = key[1] if key[0] == station_id else key[0]
                distance, station_a, station_b = value
                connected_stations.append(
                    (distance, other_station, station_a, station_b))
                total_distance += distance

        connected_stations.sort(key=lambda x: x[0])  # sort by distance

        print(
            f'{self.stations[station_id]} ({station_id}) is closely connected to:')
        for distance, other_station, station_a, station_b in connected_stations:
            print(
                f'  {self.stations[other_station]} ({other_station}), distance {distance} miles')
        print(f'Total distance along the route: {total_distance:.1f} miles')


report = StationReport()
report.get_report(sys.argv[1])

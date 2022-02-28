# TASK: Air management system
"""
    Your goal is to build an airplanes' traffic management system.
    Your program should rely on four classes: Company, Airplane, Flight and Airport.
    Consider every plane can fly only once per day.

    Here is a description of those classes:
    0. Company
    Attributes:
        - id (str) A two letters code
        - name (str)
        - planes (List of Plane) Every plane that belong to this airlines


    1) Airplane
    Attributes:
        - id (int)
        - current_location (Airport)
        - company (Company) The airlines
        - next_flights (List of Flight) Every future flight of the airplane, this list should always be sorted by datetime.

    Methods:
        - fly(self, destination)
        - location_on_date(self, date) Returns where the plane will be on this date
        - available_on_date(self, date, location) Returns True if the plane can fly from this location on this date
            (it can fly if it is in this location on this date and if it didn't already have a flight planned).


    2) Flight
    Attributes:
        - date (datetime.Date)
        - destination (Airport) The destination airport.
        - origin (Airport) The origin airport.
        - plane (Plane)
        - id (str) The ID is an encoded string composed of the destination, the airlines code and the date.

    Methods
    (Those methods are here only to update the rest of the system,
        for example, to change the location of the plane when he arrives):
        - take_off(self)
        - land(self)


    3) Airport
    Attributes:
        - city (str) The code of the city where the airport is
        - planes (List of Airplane) A list of every plane that is currently in this airport
        - scheduled_departures (List of Flight) Every future flight from this airport, sorted by date
        - scheduled_arrivals (List of Flight) Every future arrival to this airport, sorted by date

    Methods:
        - schedule_flight(self, destination, datetime) This method finds when an available airplane from an airline
            that serve the origin and the destination and schedule a flight for it.
        - info(self, start_date, end_date) Display every scheduled flight from start_date to end_date.


    You are free to add any class/method/attribute to your code, be sure to document everything you write.
    Write a small code to test your program.
"""
from datetime import datetime


class Company:
    def __init__(self, name: str):
        self.name = name
        self.planes = []

    def __repr__(self):
        return self.name


class Airplane:
    def __init__(self, name: str):
        self.name = name
        self.current_location = None
        self.company = None
        self.next_flights = []

    def __repr__(self):
        return self.name

    def fly(self, destination):
        pass

    def location_on_date(self, date):
        """
            Returns where the plane will be on this date
        """
        return self.next_flights[date]

    def available_on_date(self, date, location):
        """
            Returns True if the plane can fly from this location on this date
            (it can fly if it is in this location on this date and if it didn't already have a flight planned).
        """
        if date not in self.next_flights and self.current_location == location:
            return True
        else:
            return False


class Flight:
    def __init__(self, identity: str, date: datetime.date):
        self.identity = identity
        self.date = date
        self.plane = None
        self.origin = None
        self.destination = None

    def __repr__(self):
        return self.identity

    def take_off(self):
        print(f"flight number {self.identity} from {self.origin} to {self.destination} is taking off!")

    def land(self):
        print(f"flight number {self.identity} from {self.origin} to {self.destination} is landing!")


class Airport:
    def __init__(self, country: str):
        self.country = country
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def __repr__(self):
        return self.country

    def schedule_flight(self, destination, date):
        """
            This method finds when an available airplane from an airline
            that serve the origin and the destination and schedule a flight for it.
        """
        for plane in self.planes:
            if date not in plane.next_flights:
                plane.next_flights[date] = destination
                break

    def info(self, start_date, end_date):
        """
        Display every scheduled flight from start_date to end_date.
        """
        for departure in self.scheduled_departures:
            if start_date <= departure <= end_date:
                print(departure)


elal = Company("Elal")

F5325 = Flight("F5325", datetime.strptime("5/3/2022", "%d/%m/%Y"))
F2553 = Flight("F2553", datetime.strptime("18/3/2022", "%d/%m/%Y"))

B7371 = Airplane("B737-1")
B7372 = Airplane("B737-2")

israel = Airport("Israel")

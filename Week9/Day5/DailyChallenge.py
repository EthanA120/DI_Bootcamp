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
import time
from datetime import datetime
from random import randint


class Company:
    def __init__(self, name: str):
        self.name = name
        self.planes = []

    def __repr__(self):
        return self.name


class Airplane:
    def __init__(self, name: str, company: Company):
        self.name = name
        self.company = company
        self.current_location = None
        self.next_flights = {}

    def __repr__(self):
        return self.name

    def fly(self, destination):
        print(f"{self} is flying from {self.current_location} to {destination}")
        self.current_location = destination
        destination.planes.append(self)

    def location_on_date(self, date):
        """
            Returns where the plane will be on this date
        """
        if date in self.next_flights:
            return self.next_flights[date].destination
        else:
            return "There is no scheduled flights on this date"

    def available_on_date(self, date, location):
        """
            Returns True if the plane can fly from this location on this date
            (it can fly if it is in this location on this date and if it didn't already have a flight planned).
        """
        date = datetime.strptime(date, "%d/%m/%Y")
        nf = self.next_flights
        nf_keys = list(nf.keys())
        reference_date = datetime.today()

        if date not in nf:
            if not nf or date < nf_keys[0]:
                current_location = self.current_location
            else:
                for day in nf_keys:
                    if day < date:
                        reference_date = day
                current_location = self.next_flights[reference_date].destination
        else:
            print("Date already taken")
            return False

        if current_location == location:
            return True
        else:
            print("Plane isn't available in this location")
            return False


class Airport:
    def __init__(self, country: str, planes: list[Airplane]):
        self.country = country
        self.planes = planes
        self.scheduled_departures = []
        self.scheduled_arrivals = []

        for plane in planes:
            plane.current_location = self
            self.scheduled_departures += plane.next_flights

    def __repr__(self):
        return self.country

    def schedule_flight(self, date, destination):
        """
            This method finds when an available airplane from an airline
            that serve the origin and the destination and schedule a flight for it.
        """
        for plane in self.planes:
            if plane.available_on_date(date, destination):
                plane.next_flights[date] = Flight("F" + str(randint(1000, 9999)), date, plane, self, destination)

                self.scheduled_departures.append(plane.next_flights[date])
                destination.scheduled_arrivals.append(plane.next_flights[date])
                break

    def info(self, start_date, end_date):
        """
        Display every scheduled flight from start_date to end_date.
        """
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")

        for departure in self.scheduled_departures:
            if start_date <= departure.date <= end_date:
                print(departure)


class Flight:
    def __init__(self, identity: str, date: str, plane: Airplane, origin: Airport, destination: Airport):
        self.identity = identity
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.plane = plane
        self.origin = origin
        self.destination = destination

        plane.next_flights.update({self.date: self})
        plane.next_flights = {k: v for k, v in sorted(plane.next_flights.items(), key=lambda item: item[0])}

        origin.scheduled_departures.append(self)
        destination.scheduled_arrivals.append(self)

    def __repr__(self):
        return self.identity

    def take_off(self):
        print(f"flight number {self.identity} from {self.origin} to {self.destination} is taking off!")
        time.sleep(5)
        self.land()
        self.plane.fly(self.destination)

    def land(self):
        print(f"flight number {self.identity} from {self.origin} to {self.destination} is landing!")
        self.plane.next_flights.pop(self)


elal = Company("Elal")

B7371 = Airplane("B737-1", elal)
B7372 = Airplane("B737-2", elal)

israel = Airport("Israel", [B7371])
china = Airport("China", [B7372])
france = Airport("France", [])

F5325 = Flight("F5325", "25/3/2022", B7371, israel, france)
F5340 = Flight("F5340", "5/3/2022", B7371, china, israel)
F5335 = Flight("F5335", "2/3/2022", B7371, israel, china)
F5330 = Flight("F5330", "18/3/2022", B7371, france, israel)

print(f"{B7371.name} of {B7371.company} is at {B7371.current_location}, {B7371.next_flights}")
B7371.fly(france)
print(f"B7371 current_location: {B7371.current_location}")
print(f"France planes: {france.planes}")
B7371.fly(israel)
print(f"Location on date: {B7371.location_on_date('5/3/2023')}")
print(f"Available on date: {B7371.available_on_date('19/3/2022', israel)}")
israel.schedule_flight("3/3/2022", china)
china.info("1/3/2022", "30/3/2022")

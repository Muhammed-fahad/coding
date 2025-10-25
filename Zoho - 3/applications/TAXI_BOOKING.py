class Taxi:
    def __init__(self, id):
        self.id = id
        self.location = 'A' 
        self.earnings = 0
        self.available_time = 0

    def book_taxi(self, pickup, drop, pickup_time):
        distance = abs(ord(drop) - ord(pickup)) * 15
        fare = 100 + (distance - 5) * 10 if distance > 5 else 100
        travel_time = (distance // 15) * 60
        self.available_time = pickup_time + travel_time
        self.location = drop
        self.earnings += fare
        return fare, travel_time

class TaxiService:
    def __init__(self, num_taxis=4):
        self.taxis = []
        for i in range(num_taxis):
            taxi = Taxi(i + 1)
            self.taxis.append(taxi)

    def find_nearest_taxi(self, pickup, pickup_time):
        available_taxis = [taxi for taxi in self.taxis if taxi.available_time <= pickup_time]
        if not available_taxis:
            return None
        available_taxis.sort(key=lambda t: (abs(ord(t.location) - ord(pickup)), t.earnings))
        return available_taxis[0]
    
    def book_taxi(self, pickup, drop, pickup_time):
        taxi = self.find_nearest_taxi(pickup, pickup_time)
        if taxi:
            fare, travel_time = taxi.book_taxi(pickup, drop, pickup_time)
            return f"Taxi {taxi.id} booked. Fare: Rs.{fare}, Travel time: {travel_time} mins"
        return "No taxis available at this time. Booking rejected."

# Example Usage
taxi_service = TaxiService(4) # No of Taxies 
print(taxi_service.book_taxi('A', 'C', 9))   
print(taxi_service.book_taxi('B', 'E', 11))  
print(taxi_service.book_taxi('C', 'E', 10))  
print(taxi_service.book_taxi('D', 'E', 11))
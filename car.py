from vehicle import Vehicle
class Car(Vehicle):

    def __init__(self, brand, model, year, rental_price_per_day, seats):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seats = seats

    def display_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seats}, Rental Price: ${self.rental_price}/day"

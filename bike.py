from vehicle import Vehicle
class Bike(Vehicle):

    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}, Rental Price: ${self.__rental_price_per_day}/day"

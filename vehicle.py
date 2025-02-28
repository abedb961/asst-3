class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def getRental_price_per_day(self):
        return self.__rental_price_per_day

    def setBrand(self, newBrand):
        self.brand = newBrand

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days
    
    def display_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day"
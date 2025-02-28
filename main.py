from car import Car
from bike import Bike

def show_vehicle_info(vehicle):
    vehicle.display_info()

def main():
    car = Car("Toyota", "Corolla", 2020, 50, 5)
    bike = Bike("Yamaha", "R1", 2019, 30, 998)

    show_vehicle_info(car)
    show_vehicle_info(bike)

    print(f"Rental cost for {car.brand} {car.model} for 3 days: ${car.calculate_rental_cost(3)}")
    print(f"Rental cost for {bike.brand} {bike.model} for 5 days: ${car.calculate_rental_cost(5)}")

    print(f"Updated rental price for Toyota Corolla: ${car.get_rental_price_per_day(55)}/day")
main()
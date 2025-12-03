class Car:
    """A class representing a car."""

    def __init__(self, make, model, year, price, mileage):
        """Initialize the car's attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year} {self.price} {self.mileage}"
        # Title-case and replace underscores with spaces for readability.
        return long_name.title().replace("_", " ")


if __name__ == "__main__":
    my_new_car = Car("audi", "RS4", 2022, 141526, 22000)
    # Create a new car instance with the given make, model, year, price, and mileage.
    print(my_new_car.get_descriptive_name())
    """ prints ny car """
        








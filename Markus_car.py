class Car: 
    """A class representing a car."""

    def _init_(self,make, model, year, price, horsepower):
        """Initialize the car's attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.horsepower = horsepower
   
    def get descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year} {self.price} {self.horsepower}"

        return long_name.title().replace("_"," ")

        

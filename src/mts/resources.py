class Driver:
    def __init__(self, name: str, matricule: str):
        self.name: str = name
        self.matricule: str = matricule
        self.hourly_drive_counter: int = 0

    def drive(self):
        if self.hourly_drive_counter >= 10:
            print("Le chauffeur ne peux encore conduire.")
        else:
            self.hourly_drive_counter += 1

class Tank:
    def __init__(self, max_capacity: float):
        self.max_capacity: float = max_capacity
        self.current_capacity: float = max_capacity
    
    def fill(self, amount: float):
        self.current_capacity += amount
        if self.current_capacity > self.max_capacity:
            self.current_capacity = self.max_capacity

    def empty(self, amount: float):
        self.current_capacity -= amount
        if self.current_capacity < 0:
            self.current_capacity = 0

class PowerSupply:
    def __init__(self, max_power: float):
        self.max_power: float = max_power
        self.current_power: float = max_power

    def consume(self, amount: float):
        self.current_power -= amount
        if self.current_power < 0:
            self.current_power = 0
    
    def generate(self, amount: float):
        self.current_power += amount
        if self.current_power > self.max_power:
            self.current_power = self.max_power

class Vehicle:
    def __init__(self, id: str, passengers_capacity: int):
        self.id: str = id
        self.passengers_capacity: int = passengers_capacity
        self.current_passengers: int = 0
        self.odometer: int = 0
        self.tank: Tank = Tank(100)
        self.power_supply: PowerSupply = PowerSupply(100)
        self.is_out_of_usage: bool = False

    def drive(self, distance: int):
        if not self.is_out_of_usage:
            self.odometer += distance
            if self.odometer > 3000:
                self.is_out_of_usage = True


    def compute_fuel_usage(self) -> float:
        return 0.0
    
    def add_passengers(self, amount: int):
        self.current_passengers += amount
        if self.current_passengers > self.passengers_capacity:
            self.current_passengers = self.passengers_capacity

    def remove_passengers(self, amount: int):
        self.current_passengers -= amount
        if self.current_passengers < 0:
            self.current_passengers = 0
        
    def consume_energy(self, amount: float):
        self.tank.empty(amount * self.current_passengers)
        self.power_supply.consume(amount * self.current_passengers)
    

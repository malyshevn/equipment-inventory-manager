class Equipment:
    def __init__(self, id, name, type, serial_number):
        self.id = id
        self.name = name
        self.type = type
        self.serial_number = serial_number

    def __str__(self):
        return f"{self.id}: {self.name} ({self.type}) - SN: {self.serial_number}"


class Computer(Equipment):
    def __init__(self, id, name, serial_number, cpu, ram, storage):
        super().__init__(id, name, "Computer", serial_number)
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return super().__str__() + f", CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"


class Peripheral(Equipment):
    def __init__(self, id, name, serial_number, peripheral_type):
        super().__init__(id, name, "Peripheral", serial_number)
        self.peripheral_type = peripheral_type

    def __str__(self):
        return super().__str__() + f", Type: {self.peripheral_type}"

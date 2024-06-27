import json

class InventoryManager:
    def __init__(self):
        self.equipment_list = []

    def add_equipment(self, equipment):
        self.equipment_list.append(equipment)

    def view_equipment(self):
        for eq in self.equipment_list:
            print(eq)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([eq.__dict__ for eq in self.equipment_list], file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                if item['type'] == 'Computer':
                    equipment = Computer(**item)
                elif item['type'] == 'Peripheral':
                    equipment = Peripheral(**item)
                else:
                    equipment = Equipment(**item)
                self.add_equipment(equipment)
